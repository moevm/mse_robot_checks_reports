import json

class ConfigReader:
    __path = 0
    __config={}

    def __init__(self, path):
        self.path = path

    def read_configs(self):
        string_array = 0
        with open(self.path) as file:
            string_array = [row.strip() for row in file]

        result_string = ""
        for element in string_array:
            result_string += element
        self.__config = json.loads(result_string)
        return result_string


    def get_disciplines_for_group(self, group):
        groups = self.__config.get("groups")
        for group_number in groups:
            if group == group_number.get("group_number"):
                return group_number.get("disciplines")
        print("Группа не найдена")



    def get_discepline_props(self, group, disc):
        disc_for_group = self.get_disciplines_for_group(group)
        for disc_name in disc_for_group:
            if disc == disc_name.get("name"):
                return disc_name
        print("У группы",group,"нет дисциплины:",disc)


    def get_labs_from_disc(self, group, disc):
        disc_for_group = self.get_discepline_props(group, disc)
        if disc_for_group is None:
            return 0
        else:
            return disc_for_group.get("labs")

    def get_course_works_from_disc(self, group, disc):
        disc_for_group = self.get_discepline_props(group, disc)
        if disc_for_group is None:
            return 0
        else:
            return disc_for_group.get("course_works")

    def get_ind_tasks_from_disc(self, group, disc):
        disc_for_group = self.get_discepline_props(group, disc)
        if disc_for_group is None:
            return 0
        else:
            return disc_for_group.get("ind_tasks")

    def get_email_address(self):
        return self.__config.get("authentication").get("email")


    def get_emai_password(self):
        return self.__config.get("authentication").get("password")






# config = ConfigReader("../resources/config.json")
# test_string = config.read_configs()
# print(test_string)
# print()
# print("Атрибуты почты:")
# print("Address:", config.get_email_address())
# print("Password:", config.get_emai_password())
# print()
# testObj = json.loads(test_string)
# print(config.get_disciplines_for_group(5303))
# print()
# print(config.get_discepline_props(5303, "БД"))
# print(config.get_labs_from_disc(5303, "БД"))
# print(config.get_course_works_from_disc(5303, "БД"))
# print(config.get_ind_tasks_from_disc(5303, "БД"))
# print()
# print(config.get_discepline_props(5303, "ПРОГ"))
# print(config.get_labs_from_disc(5303, "ПРОГ"))
# print(config.get_course_works_from_disc(5303, "ПРОГ"))
# print(config.get_ind_tasks_from_disc(5303, "ПРОГ"))
# print()
# print(config.get_discepline_props(5303, "АУКЧ"))
# print(config.get_labs_from_disc(5303, "АУКЧ"))
# print(config.get_course_works_from_disc(5303, "АУКЧ"))
# print(config.get_ind_tasks_from_disc(5303, "АУКЧ"))
