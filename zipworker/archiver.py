from zipfile import*
import re

class Archiver:
    __path=""
    __zFile=None
    __listName=None
    __count = 0
    __num_docx=18
    def __init__(self,path_to_archieve):
        self.__path = path_to_archieve
        if is_zipfile(path_to_archieve):
            self.__zFile = ZipFile(path_to_archieve, 'r')
            self.__listName=self.__zFile.namelist()
        else:
            print('Не zip файл')

    def getNameList(self):
        return self.__zFile.namelist()

    def response(self,num):
        if(num==0):
            return "Файл принят"
        if(num==1):
            return "Вы прислали не все .docx файлы"

    def check_archive(self):
        '''print(self.__listName)'''
        for elem in self.__listName:
            result = re.findall(r'\.docx', elem)
            self.__count = self.__count+len(result)
        if(self.__count==self.__num_docx):
            return self.response(0)
        else:
            return self.response(1)









