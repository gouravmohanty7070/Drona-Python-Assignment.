import socket
import threading


def receiver():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 12345))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")


def sender():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12345))
        s.sendall(b'Hello, world')
        s.close()


if __name__ == "__main__":
    # Start the receiver in a new thread
    threading.Thread(target=receiver).start()

    # Wait for the server to start
    input("Press Enter to start sender...")

    # Start the sender
    sender()

