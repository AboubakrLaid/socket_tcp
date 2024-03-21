import socket
import time as timer

def split_data(data,operantion):
    num1, num2 = data.split(operantion)
    print('Calculating...')
    return (num1, num2)

def calculate(data):
    result = "Invalid operation"
    print('Checking the operation type ...')
    timer.sleep(2)
    
    if '+' in data:
        num1, num2 = split_data(data,'+')
        result= float(num1) + float(num2)
    elif '-' in data:
        num1, num2 = split_data(data,'-')
        result= float(num1) - float(num2)
    elif '*' in data:
        num1, num2 = split_data(data,'*')
        result= float(num1) * float(num2)
    elif '/' in data:
        num1, num2 = split_data(data,'/')
        try:
            result= float(num1) / float(num2)
        except ZeroDivisionError:
            result = 'Division by zero is not allowed'
    else:
        print('Invalid operation')
        
    return result
# Create a tcp socket
channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = '127.0.0.1'
server_port = 8000
# assign the server address and port to the socket
channel.bind((server_address, server_port))

channel.listen(2)
print('Listening....')

s, source_address = channel.accept()
print('Connection established with', source_address)

msg = s.recv(1024).decode('utf-8')
result = calculate(msg)

s.send(str(result).encode('utf-8'))

channel.close()