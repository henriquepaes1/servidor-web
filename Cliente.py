import socket
import sys

MAX_LINE = 256

def main():
    if len(sys.argv) == 4:
        host = sys.argv[1]
        port = sys.argv[2]
        filename = sys.argv[3]
    elif len(sys.argv) == 3:
        host = sys.argv[1]
        port = sys.argv[2]
        filename = ""

    else:
        print("usage: simplex-talk host")
        sys.exit(1)

    try:
        hp = socket.gethostbyname(host) 
    except socket.gaierror:
        print(f"simplex-talk: unknownn host: {host}")
        sys.exit(1)

    sin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sin.connect((hp, int(port)))

    request = "GET /{0} HTTP/1.1\r\nHost: {1}\r\n\r\n".format(filename, host)
    sin.sendall(request.encode())

    # Print received response from server
    print(sin.recv(6000).decode())

    sin.close()

if __name__ == "__main__":
    main()

