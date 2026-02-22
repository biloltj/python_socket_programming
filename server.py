"""
server.py
TCP Server for Programming Assignment 1 - Socket Programming

This server:
1. Waits for client connections
2. Receives client name and integer
3. Displays client/server info and computes sum
4. Sends server name and integer back to client
5. Terminates if client sends integer out of range (1–100)
"""

import socket

# Configuration
SERVER_HOST = "0.0.0.0"   # Listen on all interfaces
SERVER_PORT = 5001        # Must be > 1023
SERVER_NAME = "Server of Bilol"
SERVER_NUMBER = 50        # Server-chosen integer (can be constant)

def main():
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow reuse of address (prevents "Address already in use" error)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind socket to host and port
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    print(f"[INFO] Server bound to port {SERVER_PORT}")

    # Listen for incoming connections
    server_socket.listen(5)
    print("[INFO] Server is listening for connections...\n")

    while True:
        # Accept incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"[INFO] Connection established with {client_address}")

        # Receive data from client (decode bytes to string)
        data = client_socket.recv(1024).decode()
        print(f"[INFO] Received message from client: {data}")

        # Expected format: "ClientName|Integer"
        try:
            client_name, client_number = data.split("|")
            client_number = int(client_number)
        except:
            print("[ERROR] Invalid message format.")
            client_socket.close()
            continue

        # If number out of range, terminate server
        if not (1 <= client_number <= 100):
            print("[WARNING] Out-of-range number received. Shutting down server.")
            client_socket.close()
            server_socket.close()
            break

        # Display required output
        print(f"Client Name: {client_name}")
        print(f"Server Name: {SERVER_NAME}")
        print(f"Client Number: {client_number}")
        print(f"Server Number: {SERVER_NUMBER}")
        print(f"Sum: {client_number + SERVER_NUMBER}\n")

        # Send response back to client
        response = f"{SERVER_NAME}|{SERVER_NUMBER}"
        client_socket.send(response.encode())
        print("[INFO] Response sent to client.\n")

        # Close client connection
        client_socket.close()
        print("[INFO] Client connection closed.\n")


if __name__ == "__main__":
    main()