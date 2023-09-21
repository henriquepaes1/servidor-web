import socket
import sys

SERVER_PORT = 5432
MAX_LINE = 256

def main():
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        print("usage: simplex-talk host")
        sys.exit(1)

    try:
        hp = socket.gethostbyname(host) 
    except socket.gaierror:
        print(f"simplex-talk: unknownn host: {host}")
        sys.exit(1)

    sin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sin.connect((hp, SERVER_PORT))

    # Print connection confirmation from the server
    print(sin.recv(1024).decode())

    # Main loop: get and send lines of text
    while True:
        message = input()
        sin.sendall(message.encode())

if __name__ == "__main__":
    main()

