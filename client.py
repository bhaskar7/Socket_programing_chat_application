import threading
import os
import socket
os.system('tput setaf 6')
print("""
                    -----------------------------
                         !!  CHAT PROGRAM !!
                    -----------------------------
        """)
os.system('tput setaf 7')
def receive():
    s = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM )
    s.bind(("192.168.1.36",1234))
    while True:
        x = s.recvfrom(5000)
        y = x[0].decode()
        sender_ip = x[1][0]
        os.system('tput setaf 3')
        print("""
                                    receive {0}: {1}""".format(sender_ip,y))
        os.system('tput setaf 7')


#ip = input("Receiver IP: ")
#port = int(input("Receiver port: "))

def send():
    s = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM )
    while True:
        #msg = input()
        os.system("tput setaf 2")
        x = s.sendto(input("sender 192.168.1.36: ").encode(),('192.168.1.39',2345))
        os.system("tput setaf 7")


send1 = threading.Thread( target=send )
receive1 = threading.Thread( target=receive )

send1.start()
receive1.start()
