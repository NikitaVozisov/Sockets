import socket
def Main():
    host="127.0.0.1"
    port=5000
    sock=socket.socket()
    sock.bind((host,port))

    sock.listen(1) #listen to one connection

    connection,address=sock.accept()
    print("Connection from: "+str(address))
    while True:
        data=connection.recv(1024).decode("utf-8") #recieve 1024 bytes
        if not data:
                break
        print("From connected user: "+data)
        data=data.upper()
        print("Sending: "+data)
        connection.send(data.encode("utf-8"))
    connection.close()
if __name__=="__main__":
    Main()