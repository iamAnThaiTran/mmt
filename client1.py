import socket

# Tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối đến server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

while True:
    # Nhập tin nhắn để gửi đến server
    message = input("Nhập tin nhắn: ")
    
    # Gửi tin nhắn đến server
    client_socket.sendall(message.encode())

    # Kiểm tra nếu client muốn kết thúc kết nối
    if message.lower() == 'bye':
        break

    # Nhận phản hồi từ server
    response = client_socket.recv(1024).decode()
    print(f"Phản hồi từ server: {response}")

# Đóng kết nối
client_socket.close()
