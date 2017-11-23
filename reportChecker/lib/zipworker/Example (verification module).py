import os.path
from zipworker.archiver import Archiver
from zipworker.subject import Subject

list = []
subject = Subject("ПРОГ", 1, 2 ,4)
list.append(subject);
obj = Archiver('6754-ПРОГ-МАРТЫНОВУШКИН-МАКСИМ.zip',list)
var = obj.check_archive()
print(var)
print(obj.getInfoMessage(var))

list2 = []
subject3 = Subject("БД", 1, 2 ,4)
list2.append(subject3)
obj2 = Archiver('6754-ПРОГ-МАРТЫНОВУШКИН-МАКСИМ.zip',list2)
var2 = obj2.check_archive()
print(var2)
print(obj2.getInfoMessage(var2))



