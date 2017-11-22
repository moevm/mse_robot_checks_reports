class ConfigReader:
    path = 0

    def __init__(self, path):
        self.path = path

    def read_configs(self):
        string_array = 0
        with open(self.path) as file:
            string_array = [row.strip() for row in file]

        result_string = ""
        for element in string_array:
            result_string += element
        return result_string
