from reportChecker.lib.database import DatabaseDAO

database = DatabaseDAO()
k = "/home/dmitriy/store.7z"
file = open(k, 'rb')
database.saveDoc("Test", "Programm", file)

