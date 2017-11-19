import socket

def Main():
    host = "127.0.0.1"
    port = 5001
    server=("127.0.0.1",5000)
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((host,port))
    message=input("->")
    while message !="q":
        try:
            sock.sendto(message.encode("utf-8"),server)
            data,addr=sock.recvfrom(1024)
            data=data.decode("utf-8")
            print("Server address is: "+str(addr))
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



