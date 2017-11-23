class Subject:
    __name=""
    __numCourseWorks=0
    __numLabWorks=0
    __numIndepTasks=0

    def __init__(self,name,numCourseWorks,numLabWorks,numIndepTasks):
        self.__name=name
        self.__numCourseWorks=numCourseWorks
        self.__numLabWorks=numLabWorks
        self.__numIndepTasks=numIndepTasks

    def getName(self):
        return self.__name

    def getNumCourseWorks(self):
        return self.__numCourseWorks

    def getNumLabWorks(self):
        return self.__numLabWorks

    def getNumIndepTasks(self):
        return self.__numIndepTasks

    def setName(self,name):
        self.__name=name
        
    def setNumCourseWorks(self,numCourseWorks):
        self.__numCourseWorks=numCourseWorks

    def setNumLabWorks(self,numLabWorks):
        self.__numLabWorks=numLabWorks

    def setNumIndepTasks(self, numIndepTasks):
        self.__numCourseWorks = numIndepTasks