from qhue import Bridge
import yaml
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

username = config.get("DEFAULT","username")
print ("username",username)
bridgeAddress = config.get("DEFAULT","bridgeAddress")
print("brdge at",bridgeAddress)

# misc actions

b = Bridge(bridgeAddress, username)
# This should give you something familiar from the API docs:
print (b.url)

lights = b.lights   # Creates a new Resource with its own URL
print (lights.url)    # Should have '/lights' on the end

# Let's actually call the API and print the results
print (lights())
# Get information about light 1

print (b.lights[1])

b.lights[1].state(bri=128, hue=30000, sat=200, alert="select")


#i = 0
#while i <=256:
#    b.lights[1].state(bri=i, hue=9000, sat=200)
#    time.sleep(.1)
#    print(i)
#    i+=10

#i = 0
#while i <=65260:
#    b.lights[1].state(bri=128, hue=i)
#    time.sleep(.1)
#    print(i)
#    i+=1000

#b.lights[1].state(on=True)
print (yaml.safe_dump(b.groups(), indent=4))
