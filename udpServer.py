import socket

def Main():
    host = "127.0.0.1"
    port = 5000 # port which server is running on
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # SOCK_DGRAM means UDP
    sock.bind((host,port))

    print("Server Started")
    while True:
        try:
            data,addr=sock.recvfrom(1024)
            data=data.decode("utf-8")
            print("Message From: "+str(addr))
            print("From connected user: " + data)
            data=data.upper()
            print("Sending: "+data)
            sock.sendto(data.encode("utf-8"),addr)
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



