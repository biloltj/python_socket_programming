

import socket

# Configuration
SERVER_HOST = "127.0.0.1"  # Change to server IP if remote
SERVER_PORT = 5001
CLIENT_NAME =input("Enter your name:")

def main():
    # Get integer input from user
    number = int(input("Enter an integer between 1 and 100: "))

    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    print("[INFO] Connecting to server...")
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("[INFO] Connected to server.\n")

    # Send message in format: "ClientName|Integer"
    message = f"{CLIENT_NAME}|{number}"
    client_socket.send(message.encode())
    print(f"[INFO] Sent message: {message}")

    # Receive server response
    response = client_socket.recv(1024).decode()
    print(f"[INFO] Received response: {response}")

    # Parse response
    server_name, server_number = response.split("|")
    server_number = int(server_number)

    # Display required output
    print("\n--- RESULTS ---")
    print(f"Client Name: {CLIENT_NAME}")
    print(f"Server Name: {server_name}")
    print(f"Client Number: {number}")
    print(f"Server Number: {server_number}")
    print(f"Sum: {number + server_number}")

    # Close socket
    client_socket.close()
    print("\n[INFO] Connection closed.")


if __name__ == "__main__":
    main()