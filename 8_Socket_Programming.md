# 🧱 Python Socket Programming — Zero to Hero
## Lesson 8: Multicast UDP

In this lesson, we will explore **UDP multicast**.  
Unlike **broadcasting**, which sends a message to **all clients** in the network, **multicasting** allows you to send messages to a **specific group** of clients.

### Key Points:
- **UDP Multicast** is a way to send data to a **specific group** of devices.
- It's used in applications like **IP TV**, **video conferencing**, and **real-time data distribution**.
- Multicast messages are sent to a special **multicast group address** (e.g., `224.0.0.1`).

---

# 🌐 How UDP Multicast Works

- A **server** sends messages to a specific **multicast group address**.
- **Clients** interested in receiving messages from that group can **join** the group.
- The server sends a single message that is received by all clients in the group, using the same **UDP socket**.

---

# 🧩 Multicast Group Address Range

Multicast IP addresses range from:

```
224.0.0.0 to 239.255.255.255
```

- Any IP address in this range is considered a **multicast address**.
- Clients who want to receive multicast messages **join** a group using one of these addresses.

---

# 🖥 Step 1 — Create Multicast UDP Server

### Code

```python
import socket
import time

# Multicast group address and port
MULTICAST_GROUP = "224.0.0.1"
PORT = 5000

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Allow sending to a multicast group
server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)

# Bind server to any address
server_socket.bind(("", PORT))

print("UDP multicast server started... Broadcasting messages.")

# Broadcast a message every 5 seconds
while True:
    message = "Hello Multicast Group!"
    server_socket.sendto(message.encode(), (MULTICAST_GROUP, PORT))
    print(f"Broadcasting: {message}")
    time.sleep(5)
```

---

### Explanation:

1. **Multicast group and port**:  
   ```python
   MULTICAST_GROUP = "224.0.0.1"
   PORT = 5000
   ```

   - `224.0.0.1` is a **multicast group address** that all clients can join.
   - Port `5000` is where the server will send messages.

2. **Create UDP socket**:  
   ```python
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   ```

   - Create a **UDP socket** (`SOCK_DGRAM`).

3. **Set socket options**:  
   ```python
   server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
   ```

   - **`IP_MULTICAST_TTL`** determines the **Time to Live (TTL)**, which controls the number of hops the multicast message can make. `255` means no limit.

4. **Bind server**:  
   ```python
   server_socket.bind(("", PORT))
   ```

   - **Bind** the server to any available interface (`""`) and the specified **port** (`5000`).

5. **Send multicast message**:  
   ```python
   server_socket.sendto(message.encode(), (MULTICAST_GROUP, PORT))
   ```

   - **`sendto()`** sends the message to the **multicast group**.

6. **Repeat every 5 seconds**:  
   ```python
   time.sleep(5)
   ```

   - The server broadcasts a message every 5 seconds.

---

# 🖥 Step 2 — Create Multicast UDP Client

### Code

```python
import socket
import struct

# Multicast group and port
MULTICAST_GROUP = "224.0.0.1"
PORT = 5000

# Create UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set socket to receive multicast messages
client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
                          struct.pack("4s4s", socket.inet_aton(MULTICAST_GROUP), socket.inet_aton("0.0.0.0")))

# Bind the socket to listen on any address and port
client_socket.bind(("", PORT))

print("UDP multicast client listening for messages...")

# Listen for messages from the multicast group
while True:
    message, server_address = client_socket.recvfrom(1024)
    print(f"Received multicast message: {message.decode()} from {server_address}")
```

---

### Explanation:

1. **Multicast group and port**:  
   ```python
   MULTICAST_GROUP = "224.0.0.1"
   PORT = 5000
   ```

   - Same as server, use the multicast group address `224.0.0.1` and port `5000`.

2. **Create UDP socket**:  
   ```python
   client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   ```

   - **Create a UDP socket** (`SOCK_DGRAM`).

3. **Join the multicast group**:  
   ```python
   client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
                            struct.pack("4s4s", socket.inet_aton(MULTICAST_GROUP), socket.inet_aton("0.0.0.0")))
   ```

   - This is the key difference. **`IP_ADD_MEMBERSHIP`** tells the client to **join** the specified multicast group.

4. **Bind the socket**:  
   ```python
   client_socket.bind(("", PORT))
   ```

   - **Bind** to any interface and port `5000` to listen for multicast messages.

5. **Receive multicast message**:  
   ```python
   message, server_address = client_socket.recvfrom(1024)
   ```

   - **`recvfrom()`** listens for incoming multicast messages.

---

# 🧪 Example Execution

### Server Terminal Output

```
UDP multicast server started... Broadcasting messages.
Broadcasting: Hello Multicast Group!
Broadcasting: Hello Multicast Group!
Broadcasting: Hello Multicast Group!
```

### Client Terminal Output

```
UDP multicast client listening for messages...
Received multicast message: Hello Multicast Group! from ('<server_ip>', 5000)
Received multicast message: Hello Multicast Group! from ('<server_ip>', 5000)
Received multicast message: Hello Multicast Group! from ('<server_ip>', 5000)
```

- **Multiple clients** on the same local network will receive the broadcasted message.

---

# 📊 Communication Diagram

```
Server ------------> UDP Multicast ---> Multicast Clients

Server sends to: "224.0.0.1:5000"
Clients listening on 5000 receive the message
```

---

# 🧠 Key Takeaways

- **Multicast** sends messages to a **specific group** of clients.
- Clients join the multicast group with **`IP_ADD_MEMBERSHIP`**.
- Multicast is useful for applications where multiple clients need to receive the same data (e.g., streaming, conferencing).
- It uses the **multicast IP address range** `224.0.0.0 to 239.255.255.255`.

---

# 🚀 Next Steps

- Learn about **multicast routing** and how routers handle multicast traffic.
- Implement a **real-time chat** using UDP multicast for group conversations.
- Explore **reliable UDP multicast** by implementing **acknowledgments**.

---