
from verifier import Archiver
from verifier import Subject

list = [] #список предметов для группы 5555
list2 = [] #список предметов для группы 6666
tuplelist = []
subject1 = Subject("ПРОГ", 1, 2, 4) #предмет для группы 5555
subject2 = Subject("БД", 2, 2, 2) #предмет для группы 5555
subject3 = Subject("АЛГ", 1, 0, 0) #предмет для группы 5555
subject4 = Subject("УКК", 1, 2, 2) #предмет для группы 6666
subject5 = Subject("ФСН", 1, 2, 3) #предмет для группы 6666
subject6 = Subject("ГКД", 1, 0, 1) #предмет для группы 6666
list.append(subject1)
list.append(subject2)
list.append(subject3)
list2.append(subject4)
list2.append(subject5)
list2.append(subject6)
tuple1 = ('5555',list)
tuple2 = ('6666', list2)
tuplelist.append(tuple1)
tuplelist.append(tuple2)


obj = Archiver('5555-БД-МАРТЫНОВ-МАКСИМ.zip',tuplelist)
var = obj.check_archive()
print(var)
print(obj.getInfoMessage(var))
