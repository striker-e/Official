import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Creates a socket named server

server_socket.bind(('localhost',7010)) #Bound to an actual address and port (door)

server_socket.listen()

client_1,client1addr = server_socket.accept() # Accepts 1st connection
print("Connected to Player 1 on ",client1addr)
client_2,client2addr = server_socket.accept() # Accepts 2nd conection
print("Connected to Player 2 on ",client2addr)

#Send start message to clients.
client_1.sendall("START".encode())
client_2.sendall("START".encode())

#Server game loop
running = True
while running:
    #Receive player position from both clients
    player_1_pos = client_1.recv(1024).decode()
    player_2_pos = client_2.recv(1024).decode()
    
    #Send player positions to both clients
    client_1.sendall(player_2_pos.encode())
    client_2.sendall(player_1_pos.encode())

#Closing all socket connections
client_1.close()
client_2.close()
server_socket.close()