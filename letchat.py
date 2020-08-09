# Let's Chat for Termux / Linux / Windows
# If you want to create a server Select S to setup the Server
# Select C if you want to chat as Client
# Enjoy 
# Usage -> python letchat.py


import socket
def send_text(sending_socket, text):
    data = text.encode()
    sending_socket.send(data)

def get_text(receiving_socket):
    data = receiving_socket.recv(1024)
    return data.decode()

def server_setup():
    print("\n Enter the IP Address You want to Use : e.g -> 127.0.0.1")
    ip_address = input("Enter your IP address: ")
    if ip_address == "":
        ip_address = '127.0.0.1'
    print("\n Enter the Port you want to Use : e.g -> 80")
    port_number = input("Enter a port number: ")
    if port_number == '':
        port_number = 8081
    else:
        port_number = int(port_number)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip_address, port_number))

    #wait for connection
    server_socket.listen()
    print("Waiting for connection")
    my_socket, address = server_socket.accept()
    return my_socket, server_socket

def client_setup():
    print("\nPlease enter the IP address of the server in the format x.x.x.x or press ENTER to listen choose your localhost address.")
    ip_address = input("Enter server IP address: ")        
    if ip_address == "":
        ip_address = '127.0.0.1'
    print("\nPlease enter the port number you wish to use or press ENTER to use 8081.")
    port_number = input("Enter a port number: ")
    if port_number == '':
        port_number = 8081
    else:
        port_number = int(port_number)
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((ip_address, port_number))
    server_socket = None
    return my_socket, server_socket

def main():
    print("Chat Program")

    #get choice for client or server
    print("\nAre you going to be the server or the client?")
    choice = ""
    while choice not in ("S","s","C","c"):
        choice = input("Enter S or C: ")
    choice = choice.lower()

    #setup client or server
    if choice == "s":
        my_socket,server_socket = server_setup()
        message = "Welcome to the chat room!"
        send_text(my_socket, message)
    else:
        #setup client
        my_socket,server_socket = client_setup()

    #wait for messages and process
    running = True
    while running:
        
        #wait for message and display
        print("Receiving Message . . .")
        message = get_text(my_socket)
        print(message)
        
        #get response and send
        print('\nEnter your message to send. A blank messages quits the program.')
        message = input("Enter message: ")
        if message != '':
            send_text(my_socket, message)
        else:
            running = False;
            #exit program

    my_socket.close()
    if server_socket !=None:
        server_socket.close()


if __name__ == '__main__':
    main()