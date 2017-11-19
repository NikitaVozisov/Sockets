import socket

def Main():
    host = "127.0.0.1"
    port = 5000 # port which server is running on
    sock=socket.socket()
    sock.connect((host,port))

    message=input("->")
    while message !="q":
        try:
            sock.send(message.encode("utf-8"))
            data=sock.recv(1024).decode("utf-8")
            print("Recieved from server: "+data)
            message=input("->")
        except ConnectionAbortedError:
                print("Connection is Aborted")
                sock.close()
                break;
        except OSError:
                print("Attempt to do an operation on object, which is not a socket")
                sock.close()
                break;
    sock.close()
if __name__=="__main__":
        Main()



