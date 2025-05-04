import socket 
import threading

print("Welcome to PortHunter")

TARGET = input("Target IP: ")
START_PORT = int(input("Start PORT: "))
END_PORT = int(input("End PORT: "))

def scanner(PORT):
    target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target.settimeout(0.5)
    CONNECTIVITY = target.connect_ex((TARGET, PORT))

    if CONNECTIVITY == 0:
        print(f"Port {PORT} is active.")

for ports in range(START_PORT, END_PORT):
    thread = threading.Thread(target=scanner, args=(ports,))
    thread.start()
