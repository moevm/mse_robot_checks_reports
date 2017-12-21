#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json

class ConfigReader:
    __path = 0
    __config={}

    def __init__(self, path):
        self.path = path

    def read_configs(self):
        string_array = 0
        with open(self.path,mode='r') as file:
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



    def get_discipline_props(self, group, disc):
        disc_for_group = self.get_disciplines_for_group(group)
        for disc_name in disc_for_group:
            if disc == disc_name.get("name"):
                return disc_name
        print("У группы",group,"нет дисциплины:",disc)


    def get_labs_from_disc(self, group, disc):
        disc_for_group = self.get_discipline_props(group, disc)
        if disc_for_group is None:
            return 0
        else:
            return disc_for_group.get("labs")

    def get_course_works_from_disc(self, group, disc):
        disc_for_group = self.get_discipline_props(group, disc)
        if disc_for_group is None:
            return 0
        else:
            return disc_for_group.get("course_works")

    def get_ind_tasks_from_disc(self, group, disc):
        disc_for_group = self.get_discipline_props(group, disc)
        if disc_for_group is None:
            return 0
        else:
            return disc_for_group.get("ind_tasks")

    def get_email_address(self):
        return self.__config.get("authentication").get("email")


    def get_email_password(self):
        return self.__config.get("authentication").get("password")

    def get_groups(self):
        groups = []
        for group_number in self.__config.get("groups"):
            groups.append(group_number.get("group_number"))
        return groups


#config = ConfigReader("/root/Documents/se_project/mse_robot_checks_reports/reportChecker/resources/config.json")
#test_string = config.read_configs()
# print(test_string)
# print(config.get_groups())

# print("Атрибуты почты:")
# print("Address:", config.get_email_address())
# print("Password:", config.get_email_password())

#print(config.get_disciplines_for_group(5303))

# print(config.get_discipline_props(5303, "БД"))
# print(config.get_labs_from_disc(5303, "БД"))
# print(config.get_course_works_from_disc(5303, "БД"))
# print(config.get_ind_tasks_from_disc(5303, "БД"))

# print(config.get_discipline_props(5303, "ПРОГ"))
# print(config.get_labs_from_disc(5303, "ПРОГ"))
# print(config.get_course_works_from_disc(5303, "ПРОГ"))
# print(config.get_ind_tasks_from_disc(5303, "ПРОГ"))

# print(config.get_discipline_props(5303, "АУКЧ"))
# print(config.get_labs_from_disc(5303, "АУКЧ"))
# print(config.get_course_works_from_disc(5303, "АУКЧ"))
# print(config.get_ind_tasks_from_disc(5303, "АУКЧ"))
