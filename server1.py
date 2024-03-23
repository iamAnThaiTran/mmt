import socket

# Tạo socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Gán cổng cho socket
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Lắng nghe các kết nối đến
server_socket.listen(1)

print("Đang chờ kết nối...")

# Chấp nhận kết nối từ client
client_socket, client_address = server_socket.accept()

print(f"Kết nối từ: {client_address}")

while True:
    # Nhận tin nhắn từ client
    message = client_socket.recv(1024).decode()
    print(f"Tin nhắn từ client: {message}")

    # Kiểm tra nếu client muốn kết thúc kết nối
    if message.lower() == 'bye':
        break

    # Gửi phản hồi cho client
    response = input("Nhập phản hồi: ")
    client_socket.sendall(response.encode())

# Đóng kết nối
client_socket.close()
server_socket.close()
