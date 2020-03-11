import socket
def Main():
    host="127.0.0.1"
    port=5001
    mySocket=socket.socket()
    mySocket.connect((host,port))
    message=input("Enter Message: ")
    while message!='q':
        mySocket.send(message.encode())
        data=mySocket.recv(1024).decode()
        print("Server Says: "+data)
        message=input("Enter Message: ")
    mySocket.close()
if __name__=='__main__':
    Main()
