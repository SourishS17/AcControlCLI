import requests
import sys


def getCurr():
    response = requests.get(f"http://{ip}/aircon/get_control_info")
    return response.text
    
def updateAll():
    return defVals["pow"], defVals["mode"], defVals["stemp"], defVals["f_rate"], defVals["f_dir"], defVals["shum"]

def up():
    print(requests.get(f"http://{ip}/aircon/set_control_info?lpw=&dh3=0&dt3=18.0&pow={poww}&mode={mode}&stemp={stemp}&f_rate={f_rate}&f_dir={f_dir}&shum={shum}").text)

def getTemps():
    response = requests.get(f"http://{ip}/aircon/get_sensor_info").text
    response = response.split(",")

    print("INSIDE:", response[1][6:])
    print("OUTSIDE:", response[3][6:])



defVals = {}


poww = ""
mode = ""
stemp = ""
f_rate = ""
f_dir = ""
shum = ""


ip = "192.168.1.###"



defs = getCurr()
defs = defs.split(",")

for thing in defs:
    thing = thing.split("=")
    if len(thing) == 2:
        defVals[thing[0]] = thing[1]
    
poww, mode, stemp, f_rate, f_dir, shum = updateAll()


args = sys.argv
arg = 1

while arg < len(args):

    carg = args[arg]
    try:
        narg = args[arg + 1]
    except:
        pass

    if carg == "t":
        stemp = narg
    elif carg == "p":
        poww = narg
    elif carg == "m":
        mode = narg
    elif carg == "s":
        f_rate = narg
    elif carg == "d":
        f_dir = narg
    elif carg == "gt":
        getTemps()

    arg += 1


up()
