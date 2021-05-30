import socket
import win32api

Ip = socket.gethostbyname(socket.gethostname())
print(Ip)
Port = int(input("port:"))

currentposx, currentposy = win32api.GetCursorPos()


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((Ip, Port))
while True:
    posx = 0
    posy = 0
    data, addr = server.recvfrom(1024)
    data = data.decode()
    data = data.split(",")
    if data[0] == "a":
        tilt_side = data[1]
        tilt_front = data[2]
        tilt_side = round(float(tilt_side))
        tilt_front = round(float(tilt_front))
        if tilt_side <= -4:
            posx = 1
        elif tilt_side >= 4:
            posx = -1
        if tilt_front <= -4:
            posy = 1
        elif tilt_front >= 4:
            posy = -1
        currentposx += posx
        currentposy += posy
        win32api.SetCursorPos((currentposx, currentposy))
