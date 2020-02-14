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

import socket
import threading
import socket
import threading
import time
import select
import com2raspberry
import csv
from ast import literal_eval
from datetime import datetime


host = ""
port = 12800
s = None
CLIENT_IP = list()
all_connection = list()
my_lock = threading.RLock()

# create a socket(connect two computer)
def create_socket():
    try:
        global host
        global port
        global s  # socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Socket exception error:" + str(msg))


# binding the socket and listenning for connexion
def bind_socket():
    """set all the parameters needed to bind the socket"""
    try:
        global host
        global port
        global s
        print("Binding the port " + str(port))
        s.bind((host, port))
        s.listen(5)
        print("Bindind Done..")
    except socket.error as msg:
        print("Socket bindin Error  " + str(msg) + ".Retrying...")
        time.sleep(10)
        bind_socket()


        # establish the connection with the client (socket must be listenning)


def socket_accept():
    """socket accept is a multithreading and async function type that can allow many device to connect to server"""
    global all_connection
    while True:
        asked_connection, wlist, xlist = select.select([s], [], [], 0.05)
        for connexion in asked_connection:
            conn, address = connexion.accept()
            all_connection.append(conn)
            CLIENT_IP.append(address)
            print("connexion has been establish with | " + str(address) + " | IP_list:" + str(CLIENT_IP[:]))
            # #print( (CLIENT_IP[0])[1] )
            # for var in CLIENT_IP:
            #     print("mac: "+ str( get_mac_address( ip=var[0] ) ) )
            send_command(conn, "MonitorYourself")


        try:
            client_a_lire, wlist, xlist = select.select(all_connection, [], [], 0.05)
        except select.error:
            pass
        else:
            thr_recv = threading.Thread(target=receive_command)
            thr_recv.start()

# send commad to the client/victim or a friend
def send_command(conn, msg):
    """The sender function send a message that he've encode in bytes type to be transfer on the network"""
    msg2send = msg.encode()
    conn.send(msg2send)


def receive_command():
    """The receiver command receive bytes data decode them and send them to the interpreter to analyse"""
    global all_connection
    with my_lock:
        for conn in all_connection:
            msg_recu = conn.recv(2048)
            msg_recu = msg_recu.decode()
            interpreter(conn, str(msg_recu))

def interpreter(conn, msg):
    now = datetime.now()
    try:
        
        newDict = literal_eval(msg)
        # if newDict['AlertType'] == 'RAM Memory Alert':
        # elif newDict['AlertType'] == 'cpu Alert':
        # elif newDict['AlertType'] == 'Disk Storage Alert':
        # elif newDict['AlertType'] == 'FreqClock Cpu Alert':
        
        with open('monitorDB.csv', mode='a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=newDict.keys())
            #writer.writeheader()
            writer.writerow(newDict)
    finally:
        print("---------------------MONITORING ALERT FROM AGENT-------")
        print("|")
        print("|")
        print("|")
        print("|  " + msg)
        print("|")
        print("|")
        print("|")
        print("-------------------------------------------------------")


def main():
    global all_connection
    global s
    create_socket()
    bind_socket()
    socket_accept()

    for clients in all_connection:
        clients.close()
    s.close()



def quit_gracefully(conn):
    """close a specific client connection(conn)"""
    conn.close()
    object_2_delete = all_connection.index(conn)
    del all_connection[object_2_delete]



if __name__ == '__main__':
    main()


