import socket

target = "PUT THE IP NUMBER YOU WANT TO SCAN"


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


for port in range(1, 1001):
    result = portscan(port)
    if result:
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))


print(portscan(80))
