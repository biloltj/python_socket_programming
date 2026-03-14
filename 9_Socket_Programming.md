# 🧱 Python Socket Programming — Zero to Hero
## Lesson 9: Reliable UDP Communication

While **UDP** is fast, it does not guarantee delivery, ordering, or error checking.  
In this lesson, we’ll **add reliability** to **UDP** using a custom system that includes:

1. **Acknowledgments**: The receiver sends back a message to confirm that a packet was received.
2. **Retransmissions**: If an acknowledgment is not received within a timeout, the sender retransmits the message.
3. **Timeouts**: The sender waits for an acknowledgment for a limited time before retransmitting.

---

# 🌐 How Reliable UDP Works

1. **Sender** sends a message and waits for acknowledgment.
2. If the **acknowledgment** is received, it means the message was successfully received.
3. If the **acknowledgment** is not received within a **timeout period**, the sender **retransmits** the message.
4. **Receiver** sends an acknowledgment back after receiving each message.

This ensures that messages are **reliably transmitted**, even though UDP itself is unreliable.

---

# 🧩 Key Components:

- **Sender**: Sends data, waits for acknowledgment, retransmits if needed.
- **Receiver**: Sends acknowledgment back after receiving data.
- **Timeouts**: If acknowledgment is not received within the timeout, retransmit.

---

# 🖥 Step 1 — Create Reliable UDP Server

### Code

```python
import socket

# Server to handle receiving reliable UDP packets
PORT = 5000

# Create UDP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", PORT))

print("Reliable UDP server running...")

while True:
    # Receive message from client
    message, client_address = server_socket.recvfrom(1024)
    print(f"Received message from {client_address}: {message.decode()}")

    # Send acknowledgment
    ack_message = "ACK"
    server_socket.sendto(ack_message.encode(), client_address)
    print(f"Sent acknowledgment to {client_address}")
```

---

### Explanation:

1. **Create server socket**:  
   ```python
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   server_socket.bind(("", PORT))
   ```

   - Creates a **UDP server** socket and binds it to port `5000` to listen for messages.

2. **Receiving data**:  
   ```python
   message, client_address = server_socket.recvfrom(1024)
   ```

   - **`recvfrom()`** listens for incoming messages.

3. **Send acknowledgment**:  
   ```python
   ack_message = "ACK"
   server_socket.sendto(ack_message.encode(), client_address)
   ```

   - After receiving a message, the server sends back an **ACK** (acknowledgment) to the client.

---

# 🖥 Step 2 — Create Reliable UDP Client

### Code

```python
import socket
import time

# Client to send data and wait for acknowledgment
PORT = 5000
MAX_RETRIES = 5
TIMEOUT = 2  # Timeout in seconds

# Create UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ("127.0.0.1", PORT)

# Message to send
message = "Hello, Server!"

# Send message and wait for acknowledgment
retries = 0
while retries < MAX_RETRIES:
    # Send message
    client_socket.sendto(message.encode(), server_address)
    print(f"Sent: {message}")

    # Wait for acknowledgment
    client_socket.settimeout(TIMEOUT)
    try:
        ack_message, server = client_socket.recvfrom(1024)
        print(f"Received acknowledgment: {ack_message.decode()}")
        break  # Exit loop if acknowledgment is received
    except socket.timeout:
        print(f"Timeout! Retrying... ({retries + 1}/{MAX_RETRIES})")
        retries += 1

if retries == MAX_RETRIES:
    print("Max retries reached. Message delivery failed.")
else:
    print("Message delivered successfully.")

# Close the socket
client_socket.close()
```

---

### Explanation:

1. **Create client socket**:  
   ```python
   client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   ```

   - Creates a **UDP client** socket.

2. **Send message**:  
   ```python
   client_socket.sendto(message.encode(), server_address)
   ```

   - **`sendto()`** sends the message to the server.

3. **Wait for acknowledgment**:  
   ```python
   client_socket.settimeout(TIMEOUT)
   try:
       ack_message, server = client_socket.recvfrom(1024)
       print(f"Received acknowledgment: {ack_message.decode()}")
       break
   except socket.timeout:
       print(f"Timeout! Retrying... ({retries + 1}/{MAX_RETRIES})")
   ```

   - **`settimeout()`** makes the socket wait for a response within a certain time (`TIMEOUT`).
   - If **no acknowledgment** is received within the timeout, the message is **retransmitted**.
   
4. **Retries**:  
   ```python
   retries += 1
   ```

   - If an acknowledgment is not received, the client will retry until the maximum retries (`MAX_RETRIES`) are reached.

---

# 🧪 Example Execution

### Server Terminal Output

```
Reliable UDP server running...
Received message from ('127.0.0.1', 12345): Hello, Server!
Sent acknowledgment to ('127.0.0.1', 12345)
```

### Client Terminal Output

```
Sent: Hello, Server!
Received acknowledgment: ACK
Message delivered successfully.
```

- If the client doesn't receive the acknowledgment in time, it will retry the message up to `MAX_RETRIES`.

---

# 📊 Communication Diagram

```
Client ------------> UDP Socket ------------> Server
      send            sendto()                 recvfrom()
                      <------------------------- 
                         receive and ack
                <------------ ACK -------------
```

---

# 🧠 Key Takeaways

- **Reliable UDP** uses a custom system of **acknowledgments** and **timeouts** to ensure delivery.
- **`settimeout()`** is used to make the client wait for a response within a defined time.
- If no acknowledgment is received, the **sender retransmits** the message.
- This makes **UDP** more reliable, but not as efficient as TCP for all use cases.

---

# 🚀 Next Steps

- **UDP Congestion Control**: Implement basic **flow control** in a UDP system.
- **Real-Time UDP Applications**: Use reliable UDP for applications like **live streaming** or **gaming**.
- Learn how to implement a **handshake** in UDP for **secure connections**.

---
