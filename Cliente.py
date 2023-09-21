import socket
import sys

SERVER_PORT = 5432
MAX_LINE = 5

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

    # Main loop: get and send lines of text
    while True:
        buf = input()
        # buf = buf[:MAX_LINE - 1]
        buf = buf.encode()
        sin.sendall(buf)

if __name__ == "__main__":
    main()

