import socket

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

# 创建客户端套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接到服务器
sock.connect((HOST, PORT))

try:
    message = "Hello"
    # 发起数据给服务器
    sock.sendall(message)
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        # 接收服务器返回的数据
        data = sock.recv(10)
        amount_received += len(data)
        print
        'Client Received: {}'.format(data)

except socket.errno as e:
    print('Socket error:', e)
except Exception as e:
    print('Otherexception:', e)
finally:
    print('Closing connection to the server')
    sock.close()
