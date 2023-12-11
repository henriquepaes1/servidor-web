import socket
import sys
from threading import *


SERVER_PORT = 5431
MAX_PENDING = 5
MAX_LINE = 1024
NOT_FOUND = "HTTP/1.1 404 ERRO\r\n"

def main():
    try:
        server_host = sys.argv[1]

        if(server_host.__contains__(":")):
        # Build address data structure
            server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)  
        else:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        server_socket.bind((server_host, SERVER_PORT))
        server_socket.listen(MAX_PENDING)

        print(f"Server on host {server_host} listening on port {SERVER_PORT}")

        while True:
            client_connection, addr = server_socket.accept()
            thread = Thread(target = createClientThread, args = [client_connection, addr])
            thread.daemon = True
            thread.start()
            
    
    except KeyboardInterrupt:
        print("\nServer terminated.")
        sys.exit(0)
        
# Create a worker thread to handle request
def createClientThread(clientSocket, addr):
    print(f"Connected by {addr} using thread {current_thread().name}")
            
    data = clientSocket.recv(MAX_LINE).decode()
    print(data)
    if data:
        file_path = data.split("\r\n")[0].split(" ")[1][1:]
        try: 
            with open(file_path, 'r') as file:
                file_text = file.read()
                content_length = len(file_text)
                content_type = "text/html"
                response = f"HTTP/1.1 200 OK\r\nContent-Length={content_length}\r\nContent-Type={content_type}\r\n\r\n{file_text}"
                clientSocket.sendall(response.encode())      
        except FileNotFoundError:
                clientSocket.sendall(NOT_FOUND.encode()) 
        finally:
                clientSocket.close()
                print(f"Connection closed by {addr}")

if __name__ == "__main__":
    main()
