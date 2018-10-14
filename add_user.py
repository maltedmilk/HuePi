from qhue import create_new_username
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

bridgeAddress = config.get("DEFAULT","bridgeAddress")
print("brdge at",bridgeAddress)

username = create_new_username(bridgeAddress)
print (username)


