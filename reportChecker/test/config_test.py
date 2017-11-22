from reportChecker.lib.config import ConfigReader

config = ConfigReader("../resources/config.json")
test_string = config.read_configs();
print(test_string)