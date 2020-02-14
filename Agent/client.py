# -*- encoding:utf-8 -*-
# Copyright 2019 The Bayo. All Rights Reserved.
#
# Licensed under the Bayobrain License, Version 1.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.bayobrain.org/licenses/LICENSE-1.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""A client module that connect to the server and make to perform send/receive.

    IMPORTS :
        -   socket

    FUNCTIONS :
        -   socket_bind_connect()

        -   receiver_from_host(msg)

        -   socket_close()

        -   main()
"""

import socket
import psutil, os, time, datetime, sys, socket, requests, platform
from decimal import Decimal
import probeReader
from datetime import datetime

###########################################################################################################################################################
###############################################################################################################################################
###########################################################################################################################

### These values may be changed. Please read the notes !!! ###
# Refresh = default refresh rate, aka the time for intervals (in seconds). Can be float, e.g. 0.2
# But I like 0.5 !
refresh =2.0
# At the bottom are some waves, at least, it aims to be.
# Set this to (True) to enable, or (False) to disable this amazing feature. I mean. Why should you?
dowave = True
# The top and bottom banners (Title / Wavey thingy) change color. Same as before:
# Set this to (True) to enable, or (False) to disable this amazing feature.
changeColor = True
# Below setting is for getting your external IP address.
# To disable calling to the outside world, disable this.
USESERVICES = True

# The following setting will change the character used to define the look
# The outer edges, as seen when running the script, are made of:
eC = '\033[97m╳'
eL = '\033[97m╲'
eF = '\033[97m╱'
# Get your ascii codes here : https://theasciicode.com.ar #

if len(sys.argv) > 1:
    try:
        cls()
        refresh = float(sys.argv[1])
    except:
        print("Argument for refresh-rate needs to be a float, e.g. '2.5' or '0.3'.")
        #print(f'Not "{sys.argv[1]}". For now, the default of {refresh} will be used')
        time.sleep(5)
        pass


go = True
tab = '\t'
nwl = '\n'
bck = '\b'
locIP = None
outIP = None
color = time.localtime()[:-1]
colors = None
ostype = platform.platform()
oslen = None
cWave = ["⁓", "~", "⁓", "⍨", "⁓", "~"]
iWave = 0
cpu_user_av = float(0)
cpu_system_av = float(0)
cpu_idle_av = float(0)
cpu_user_prev = float(0)
cpu_system_prev = float(0)
cpu_idle_prev = float(0)


hote = 'localhost'
port = 12800
msg_a_envoyer = b""
connexion_avec_server = None

###########################################################################################################################################################
###############################################################################################################################################
###########################################################################################################################


def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class pClr:
    P = '\033[95m'
    B = '\033[94m'
    G = '\033[92m'
    Y = '\033[93m'
    R = '\033[91m'
    E = '\033[0m'
    b = '\033[1m'
    u = '\033[4m'
    i = '\033[3m'

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Converts value FROM=leftMin, leftMax | TO=rightMin,rightMax
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def progBar(input, length, *reverse):
    ftab = ''
    space = length - 5
    progress = translate(input, 0, 100, 0, int(space))
    inputlen = int(len(str(input)))
    # seperate = 5 - inputlen
    # oT = round((seperate / 2) - 0.2)
    # oF = round((seperate / 2) - 0.2)
    # fS = ' ' * oT
    # lS = ' ' * oF
    if reverse:
        fill = '░' * int(progress)
        space = '▓' * (int(space) - int(progress))
    elif not reverse:
        fill = '▓' * int(progress)
        space = '░' * (int(space) - int(progress))

    if inputlen == 5:
        ftab = ''
    elif inputlen == 4:
        ftab = tab
    elif inputlen == 3:
        ftab = f"{tab} "
    msg = f"{fill}{space}{ftab}{input}%{tab}"
    return str(msg)


def k2m(input):
    """Memory"""
    global kb2
    kb = int(input)
    kb2 = int(input)
    if len(str(kb)) > 11:
        mb = int(kb / 1000 / 1000)
        mb = str(mb)
        mb = f"{mb[:-3]}.{mb[-2:]}"
        st = 'GB'
    else:
        mb = int(kb / 1000 / 1000)
        mb = f"{mb}"
        st = "MB"
    return mb, st

def getIP():
    if USESERVICES == True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("1.1.1.1", 80))
            ipaddr = (s.getsockname()[0])
            s.close
        except:
            ipaddr = 'No network'
    else:
        ipaddr = 'Disabled'
    return ipaddr

def outerIP():
    if USESERVICES == True:
        try:
            ip = requests.get('https://api.ipify.org?format=json').text
            ip = ip[7:-2]
        except:
            ip = 'No network'
    else:
        ip = 'Disabled'
    return ip

def c2g(input):
    """Processor"""
    kh = float(input)
    if len(str(kh)) > 4:
        gh = str(kh / 1000)
        gh = f"{gh[:4]} Ghz"
    else:
        gh = str(kh / 1000)
        gh = f"{gh} Mhz"
    return gh


def getTemp():
    try:
        temps = psutil.sensors_temperatures()
        for mon in temps:
            return int(temps[mon][0][1])
    except:
        return int('0')

def add0(data):
    data = str(data)
    if int(len(data)) < 2:
            output = f"0{data}"
    else:
        output = data
    return str(output)

def osLen():
    ostype = platform.platform()
    oslen = int(len(ostype))
    maxlen = 47
    seperate = maxlen - oslen
    oT = round((seperate / 2) + 0.2)
    oF = round((seperate / 2) - 0.2)
    total = int(len(str(ostype))) + oT + oF
    if int(len(str(ostype))) > 47:
        ostype = f"{ostype[:46]}…"
    if int(len(str(total))) > 47:
        oF -= 1
        total = int(len(str(ostype))) + oT + oF
    oT = int(oT)
    oF = int(oF)
    return ostype, oT, oF, int(total)

def enObject():
    ## END OF OBJECT ##
    global go
    global tab 
    global nwl
    global bck 
    global locIP 
    global outIP 
    global color 
    global colors
    global ostype 
    global oslen 
    global cWave
    global iWave 
    global cpu_user_av 
    global cpu_system_av
    global cpu_idle_av 
    global cpu_user_prev
    global cpu_system_prev 
    global cpu_idle_prev

    go = True
    tab = '\t'
    nwl = '\n'
    bck = '\b'
    locIP = getIP()
    outIP = outerIP()
    color = time.localtime()[:-1]
    colors = [pClr.P, pClr.B, pClr.G, pClr.Y, pClr.R]
    ostype = platform.platform()
    oslen = osLen()
    cWave = ["⁓", "~", "⁓", "⍨", "⁓", "~"]
    iWave = 0
    cpu_user_av = float(0)
    cpu_system_av = float(0)
    cpu_idle_av = float(0)
    cpu_user_prev = float(0)
    cpu_system_prev = float(0)
    cpu_idle_prev = float(0)

def averager(cputype, value):
    global cpu_idle_av, cpu_system_av, cpu_system_prev, cpu_user_prev, cpu_system_prev, cpu_idle_prev
    if cputype == 'u':
        calc = (value + cpu_user_prev) / 2
        cpu_user_av = calc
        cpu_user_prev = value
    elif cputype == 'i':
        calc = (value + cpu_idle_prev) / 2
        cpu_idle_av = calc
        cpu_idle_prev = value
    elif cputype == 's':
        calc = (value + cpu_system_prev) / 2
        cpu_system_av = calc
        cpu_system_prev = value
    # calc = value + cpuvar[1]
    # cpuvar[0] = calc
    # cpuvar[1] = value
    calc = Decimal(calc).quantize(Decimal('.1'))
    return calc

def tWave():
    global iWave, cWave, sWave, leWave, dowave
    # sWave = f"{cWave[iWave::1]}{cWave[:iWave:1]}"
    sWave = ''.join(str(e) for e in cWave[iWave::1])
    sWave += ''.join(str(e) for e in cWave[:iWave:1])
    leWave = ''.join(str(e) for e in sWave)
    theWave = leWave * 7
    theWave = theWave[1::]
    if iWave == 5:
        iWave = 0
    else:
        if dowave == True:
            iWave += 1
    return str(theWave)


def defineAlerts(mem, cpuf, cputp, disk):
    
    # try to define Alert conditions
    print("\n")
    print(mem)
    print("meme \n")
    print(cpuf)
    print("cpuf  \n")
    print(cputp)
    print("cputp \n")
    print(disk)
    print("disk \n")
    print("\n")
    print("temp: "+str(getTemp()))
    print("\n")

    #proberead = probeReader.main()
    print("cputp " + str(cputp[0]))
    print("AVerage" + str(averager('u', cputp[0])))
    if (cputp[0]>70) or (cputp[2]>70):
        error = {"datetime":"{}".format(datetime.now()), "AlertType":"cpu Alert", "cputp[0]-user":cputp[0], "cputp[1]-system":cputp[2], "cputp[2]-Idle":cputp[3], "RAM[0]-total":k2m(mem[0]), "RAM[3]-used":k2m(mem[3]), "RAM[2]-percent":mem[2], "Disk[0]-total":k2m(disk[0]), "Disk[1]-used":k2m(disk[1]), "Disk[3]-percent":disk[3], "Freq[0]-used":c2g(cpuf[0]), "Freq[2]-total":c2g(cpuf[2]), "temp-limit":getTemp()}
        #error = error + "|$|" + proberead
        send_to_hostPC(str(error))
    elif (mem[2]>50):
        error = {"datetime":"{}".format(datetime.now()), "AlertType":"RAM Memory Alert", "cputp[0]-user":cputp[0], "cputp[1]-system":cputp[2], "cputp[2]-Idle":cputp[3], "RAM[0]-total":k2m(mem[0]), "RAM[3]-used":k2m(mem[3]), "RAM[2]-percent":mem[2], "Disk[0]-total":k2m(disk[0]), "Disk[1]-used":k2m(disk[1]), "Disk[3]-percent":disk[3], "Freq[0]-used":c2g(cpuf[0]), "Freq[2]-total":c2g(cpuf[2]), "temp-limit":getTemp()}
        #error = error + "|$|" + proberead
        send_to_hostPC(str(error))
    elif (disk[3]>97):
        error = {"datetime":"{}".format(datetime.now()), "AlertType":"Disk Storage Alert", "cputp[0]-user":cputp[0], "cputp[1]-system":cputp[2], "cputp[2]-Idle":cputp[3], "RAM[0]-total":k2m(mem[0]), "RAM[3]-used":k2m(mem[3]), "RAM[2]-percent":mem[2], "Disk[0]-total":k2m(disk[0]), "Disk[1]-used":k2m(disk[1]), "Disk[3]-percent":disk[3], "Freq[0]-used":c2g(cpuf[0]), "Freq[2]-total":c2g(cpuf[2]), "temp-limit":getTemp()}
        #error = error + "|$|" + proberead
        send_to_hostPC(str(error))
    elif(cpuf[0]>2500):
        error = {"datetime":"{}".format(datetime.now()), "AlertType":"FreqClock Cpu Alert", "cputp[0]-user":cputp[0], "cputp[1]-system":cputp[2], "cputp[2]-Idle":cputp[3], "RAM[0]-total":k2m(mem[0]), "RAM[3]-used":k2m(mem[3]), "RAM[2]-percent":mem[2], "Disk[0]-total":k2m(disk[0]), "Disk[1]-used":k2m(disk[1]), "Disk[3]-percent":disk[3], "Freq[0]-used":c2g(cpuf[0]), "Freq[2]-total":c2g(cpuf[2]), "temp-limit":getTemp()}
        #error = error + "|$|" + proberead
        send_to_hostPC(str(error))
    elif(getTemp()>26):
        error = {"datetime":"{}".format(datetime.now()), "AlertType":"temp Cpu Alert", "cputp[0]-user":cputp[0], "cputp[1]-system":cputp[2], "cputp[2]-Idle":cputp[3], "RAM[0]-total":k2m(mem[0]), "RAM[3]-used":k2m(mem[3]), "RAM[2]-percent":mem[2], "Disk[0]-total":k2m(disk[0]), "Disk[1]-used":k2m(disk[1]), "Disk[3]-percent":disk[3], "Freq[0]-used":c2g(cpuf[0]), "Freq[2]-total":c2g(cpuf[2]), "temp-limit":getTemp()}
        #error = error + "|$|" + proberead
        send_to_hostPC(str(error))

def printer() :
    global go
    print("Loading. Please wait. Just grabbing stuff here, hold on buddy!")
    while go == True:
        try:
            mem = psutil.virtual_memory()
            cpuf = psutil.cpu_freq()
            cputp = psutil.cpu_times_percent()
            disk = psutil.disk_usage('/')
            defineAlerts(mem, cpuf, cputp, disk)

            if changeColor == True:
                color = translate(int(str(time.localtime()[5])), 0, 60, 0, 4)
            else:
                color = 1
            hour = add0(time.localtime()[3])
            mint = add0(time.localtime()[4])
            scnd = add0(time.localtime()[5])
            # if int(len(scnd)) < 2:
            #     scnd = f"0{str(int(scnd))}"
            second = str(scnd)[-1:]
            color = int(color)
            rndClr = colors[color]
            if second == 1 or second == 3 or second == 5 or second == 7 or second == 9:
                tS = ':'
            else:
                tS = ' '
            if  int(len(k2m(mem[1])[0])) < 5:
                mT = 2
            else:
                mT = 1
            
            cls()
            print(f"{eF}{eC*((6*8)-1)}{eL}")
            #print(f"{eC}{eF} {rndClr} Pywaremon -xJustiinsane- Exit with CTRL+C {pClr.E} {eL}{eC}")
            if os.name:
                print(f"{eC}{' ' * osLen()[1]}{pClr.b}{osLen()[0]}{pClr.E}{' ' * osLen()[2]}{eC}")
            print(f"{eC}{tab*6}{eC}")
            print(f"{eC} {pClr.R}Local time{tab}{hour}{tS}{mint}{tS}{scnd}{tab*3}{pClr.E}{eC}")
            print(f"{eC} {pClr.R}Date{tab*2}{time.localtime()[2]}-{time.localtime()[1]}-{time.localtime()[0]} Day {time.localtime()[6]}/7 {time.localtime()[7]}/365{tab}{pClr.E}{eC}")
            print(f"{eC}{tab*6}{eC}")
            if int(len(c2g(cpuf[0]))) < 8:
                sT = 2
            else:
                sT = 1
            print(f"{eC} {pClr.B}CPU{tab*2}Clock:{tab}{c2g(cpuf[0])}/{c2g(cpuf[2])}{pClr.E}{tab*sT}{eC}")
            print(f"{eC} {pClr.B}Usage{tab*2}User:{tab}{progBar(averager('u', cputp[0]), 20)}{pClr.E}{eC}{nwl}{eC}{pClr.B}{tab*2}System:{tab}{progBar(averager('s', cputp[2]), 20)}{pClr.E}{eC}{nwl}{eC}{pClr.B}{tab*2}Idle:{tab}{progBar(averager('i', cputp[3]), 20, True)}{pClr.E}{eC}")
            print(f"{eC}{tab*6}{eC}")
            print(f"{eC} {pClr.P}Memory{tab}Using:{tab}{k2m(mem[3])[0]}/{k2m(mem[0])[0]} {k2m(mem[0])[1]}{tab*2}{pClr.E}{eC}{nwl}{eC}{pClr.P}{tab*2}{progBar(mem[2], 28, True)}{pClr.E}{eC}")
            print(f"{eC}{tab*6}{eC}")
            if int(len(k2m(disk[1])[0])) < 7:
                sT = 2
            else:
                sT = 1
            if int(len(str(disk[3]))) < 4:
                sT2 = 2
            else:
                sT2 = 1
            print(f"{eC} {pClr.G}Storage{tab}Using:{tab}{k2m(disk[1])[0]}/{k2m(disk[0])[0]} {k2m(disk[0])[1]}{tab*sT}{pClr.E}{eC}{nwl}{eC}{pClr.G}{tab*2}{progBar(disk[3], 28, True)}{pClr.E}{eC}")
            print(f"{eC}{tab*6}{eC}")
            print(f"{eC} {pClr.Y}IP Addr{tab}Local:{tab}{locIP}{tab*2}{pClr.E}{eC}{nwl}{eC}{pClr.Y}{tab*2}Outer:{tab}{outIP}{tab*2}{pClr.E}{eC}")
            print(f"{eC}{tab*6}{eC}")
            if hasattr(psutil, "sensors_temperatures"):
                print(f"{eC} {pClr.R}Temp{tab*2}CPU:{tab}{getTemp()}°C {tab*3}{pClr.E}{eC}")
                print(f"{eC}{tab*6}{eC}")
            print(f"{eC}{eL} {rndClr} {tWave()} {pClr.E} {eF}{eC}")
            #print(f"{eC*3}{tab*5}      {eC*3}")
            print(f"{eL}{eC*((6*8)-1)}{eF}")
            time.sleep(refresh)
        except KeyboardInterrupt:
            go = False
            print("\a")
            sys.exit('Keyboard Interuption!')
        except:
            go = False
            print("Other error occured")
        #go = False


###########################################################################################################################################################
###############################################################################################################################################
###########################################################################################################################


def socket_bind_connect():
    """ Functions responsible to bind connection to a specific server await

        ARGS :
            -

        RETURNS :
            -
    """
    global connexion_avec_server
    connexion_avec_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_server.connect((hote, port))
    print("connexion etablite avec le port {}".format(port))


def receiver_from_host():
    global connexion_avec_server
    msg_recu = connexion_avec_server.recv(2048)
    if msg_recu.decode() == "MonitorYourself":
        enObject()
        printer()
            

def send_to_hostPC(message):
    global connexion_avec_server
    connexion_avec_server.send(message.encode())


def socket_close():
    """ Functions responsible to quit the server connection

        ARGS :
            -

        RETURNS :
            -
    """
    global connexion_avec_server
    connexion_avec_server.close()
    print("fermeture de la connexion avec le serveur ...")

def main():
    """ Functions responsible to ::
            - bind or connect to the server connection
            - and while is True perform an await function to see if a message has been sended or send a message

        ARGS :
            -

        RETURNS :
            -
    """
    socket_bind_connect()
    while True:
        receiver_from_host()








if __name__ == '__main__':
    main()