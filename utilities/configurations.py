import configparser

def __get_config():
    config = configparser.ConfigParser() #Creates a ConfigParser object
    config.read('utilities/config.ini') #Read the Data from the Config File mentioned in the path
    return config

def get_base_url():
    return __get_config()['API']['base_url'] #Gets the value of the base_url from the Config File under API Section