class ListSubjects:
    __list = []

    def appendSubject(self,subj):
        self.__list.append(subj)

    def getSubject(self,index):
        return self.__list[index]

    def insertSubject(self, index, subj):
        self.__list.insert(index, subj)

    def popSubject(self,index):
        self.__list.pop(index)

    def clearList(self):
        self.__list.clear()

    def getLenth(self):
        return self.__list.__len__()

    def getList(self):
        return  self.__list