#! /usr/bin/env python
# -*- coding: utf-8 -*-

from zipfile import*
import codecs, sys
import locale
import lib.subject
import os

class Archiver:
    __path=""
    __subject=None #объект с дисциплиной
    __fileName=""
    __zFile=None
    __listNames=[]
    __count = 0
    __responseStr="Файл не принят.\n"
    __listSubjects=None
    __number=-1 #Номер в списке названия дисциплины, которую будет ождать программа, следуя из названия архива

    def __init__(self,path_to_archieve, listSubjects):
        self.__path = path_to_archieve
        if is_zipfile(path_to_archieve):
            self.__zFile = ZipFile(path_to_archieve, 'r')
            templist=self.getNameList()
            if(templist!=None):
                for elem in templist:
                    try:
                        self.__listNames.append(elem.encode('cp437').decode('cp866'))
                    except UnicodeEncodeError:
                        self.__listNames.append(elem)
        self.__listSubjects=listSubjects

    def getNameList(self):
        return self.__zFile.namelist()

    def getInfoMessage(self,value):
        if(value==0):
            return "Файл принят."
        if (value == 1):
            return "Файл не принят.\n Архив должен быть zip архивом."
        if (value == 2):
            return "Файл не принят.\n Вы прислали пустой архив."
        if (value == 3):
            return self.__responseStr
        if (value == 4):
            return "Файл не принят.\n Неверное название архива."
        if(value == 5):
            return "Файл не принят.\n Название папки внутри архива и название архива должно быть одинаковым. Ожидалась папка с именем: " + self.__fileName
        if(value ==404):
            return "Не загружен список с предметами listSubject. Используйте метод setLislSubject(list)"




    def checkName(self, str):  # проверка названия файла  1 - когда название папки внури  архива (сюда же можно вставить проверку соответствует ли номер группе дисциплине)

        listStr = str.split('-')

        if (len(listStr) != 4 or not (listStr[0].isdigit()) or not self.isRightSubject(listStr[1]) or not (
        listStr[2].isalpha()) or not (listStr[2].isupper()) or not (listStr[3].split('.')[0].isalpha()) or not (
        listStr[3].split('.')[0].isupper())):
            return 4 #Если название архива неверно
        else:
            self.__fileName=str[0:len(str)-4] #если название папки внутри архива верно
            return  "$"


    def checkFileName(self):        
        # count = len(self.__path)-1 #Выделим имя файла из пути
        # s=self.__path[count]
        # strR=""
        # while(s!="/" and count > -1 ):
        #     strR+=s
        #     count-=1
        #     s=self.__path[count]
        # str=""
        # for i in range(len(strR)-1,-1,-1):
        #     str+=strR[i]

        #так полегче будет
        filename = os.path.basename(self.__path)
        return  self.checkName(filename)



    def isRightSubject(self, name): #правильно ли названа дисциплина
        for disc in self.__listSubjects:
            if(name==disc.getName()):
                self.__subject=disc    #получим объект с дисциплиной
                return True
        return False

    def finderNumSlash(self,str): # Возвращает количесвто слешей в строке до 3
        k=0
        for i in range(0, len(str)):
            if(str[i]=="/"):
                k+=1
            if(k>2):
                return 3
        return k


    def getTemplatesList(self): #получить список шаблонов
        list=[]
        i=0
        for i in range(1,self.__subject.getNumLabWorks()+1):
            strT1 = self.__fileName+"/"+ "ЛР_"+str(i)+"/"
            list.append(strT1)
        for i in range(1, self.__subject.getNumIndepTasks() + 1):
            strT1 = self.__fileName + "/" + "ИДЗ_" + str(i) + "/"
            list.append(strT1)
        for i in range(1, self.__subject.getNumCourseWorks() + 1):
            strT1 = self.__fileName + "/" + "КР_" + str(i) + "/"
            list.append(strT1)
        return list


    def isAllFound(self, listFound): #все ли строки найдены
        sum=0
        for x in listFound:
            sum = sum+x
        if(sum==len(listFound)):
            return True
        else:
            return  False

    def check_archive(self):

        if(self.__listSubjects==None):
            return 404;
        if(self.__zFile==None):
            return 1 #Если это не zip архив
        if(self.__listNames==None):
            return 2 #Если архив пуст
        resp = self.checkFileName() #проверка на имя архива
        if(resp!="$"):
            return resp #Если название архива неверно
        begin = self.__listNames[0]
        if(begin[len(begin)-1]=="/"):
            begin = begin[0:len(begin)-1]
        if(self.__fileName.find(begin)!=0):#проверка на имя папки
            return 5  #Несовпадает ли имя папки и архива

        workingListNames=[]
        i=0
        for str in self.__listNames: #Отбрасываем ненужные пути
            if(self.finderNumSlash(str) < 3 and (str[len(str)-1]=="/")):
                workingListNames.append(str)
            if (self.finderNumSlash(str) < 2 and (str[len(str)-1]!="/")):
                workingListNames.append(str)
        print(workingListNames)
        workingListNames.remove(self.__fileName+"/")
        listTamplates=self.getTemplatesList() #получаем список шаблонов для поиска
        listFound=[] #здесь будем помечаем найденные строки
        for i in range(len(listTamplates)):
            listFound.append(0)
        j=0
        for pathT in listTamplates:
            for path in workingListNames:
                if(path==pathT):
                    listFound[j]=1
                    workingListNames.remove(path)
            j+=1

        if(self.isAllFound(listFound) and len(workingListNames)==0):
            return 0 #Файл принят

        if(len(workingListNames)!=0):
            str1="В архиве обнаружены лишние директории: \n"
            for elem in workingListNames:
                str1+=elem+"\n"
            self.__responseStr += str1

        if (not self.isAllFound(listFound)):
            k=0
            str2 = "В архиве отсутствуют необходимые директории: \n"
            for x in listFound:
                if (x == 0):
                    str2 += listTamplates[k] + "\n"
                k+=1
            self.__responseStr += str2
        return 3 #Отсутсвуют директории













