import socket

# Create a tcp socket
channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


destination_address = '127.0.0.1'
destination_port = 8000

destination = (destination_address, destination_port)

# connect to the server
channel.connect(destination)
print('Connection established.')
operation = input('Enter the operation: ')
channel.send(operation.encode('utf-8'))

result = channel.recv(1024).decode('utf-8')
print(result)

channel.close()