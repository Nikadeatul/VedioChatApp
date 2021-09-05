import socket, cv2, pickle, struct

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP: ', host_ip)
port = 9999
address = (host_ip, port)
server_socket.bind(address)
server_socket.listen(5)
print("LISTENING AT: ", address)
while True:
    client_socket, addr = server_socket.accept()
    print("GOT CONNECTION FROM: ", addr)
    if client_socket:
        cap = cv2.VideoCapture(0)
        while (cap.isOpened()):
            img, photo = cap.read()
            a = pickle.dumps(photo)
            msg = struct.pack("Q", len(a))+a
            client_socket.sendall(msg)
            cv2.imshow("TRANSMITTING VIDEO", photo)
            key = cv2.waitKey(1) & 0xFF
            if key == ord ('q'):
                client_socket.close()