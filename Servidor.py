import socket
import sys

SERVER_PORT = 5432
MAX_PENDING = 5
MAX_LINE = 256

def main():
    try:
        # Build address data structure
        sin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sin.bind(('0.0.0.0', SERVER_PORT))
        sin.listen(MAX_PENDING)

        print(f"Server listening on port {SERVER_PORT}")

        while True:
            new_s, addr = sin.accept()
            print(f"Connected by {addr}")   

            while True:
                data = new_s.recv(MAX_LINE)
                if not data:
                    break
                sys.stdout.write(data.decode())
            
            new_s.close()
            print(f"Connection closed by {addr}")

    except KeyboardInterrupt:
        print("\nServer terminated.")
        sys.exit(0)

if __name__ == "__main__":
    main()