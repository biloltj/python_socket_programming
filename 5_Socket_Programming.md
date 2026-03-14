# 🧱 Python Socket Programming — Zero to Hero
## Lesson 5: Multi-Client TCP Server with Threading

So far, our server could only handle **one client at a time**.  
Now we will create a server that can handle **multiple clients simultaneously** using **threading**.

---

# 🌐 How Multi-Client Server Works

```
Client1 ---> Thread1 ---> Server
Client2 ---> Thread2 ---> Server
Client3 ---> Thread3 ---> Server
```

Each client runs in a **separate thread**.  
This allows all clients to **send and receive messages independently**.

---

# 🖥 Step 1 — Import Libraries

```python
import socket
import threading
```

- `socket` → networking  
- `threading` → handle multiple clients at the same time

---

# 🐍 Step 2 — Define Client Handler Function

```python
def handle_client(client_socket, client_address):
    print(f"Client {client_address} connected.")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                print(f"Client {client_address} disconnected.")
                break
            print(f"Client {client_address} says: {message.decode()}")
            reply = input(f"Server to {client_address}: ")
            client_socket.send(reply.encode())
        except ConnectionResetError:
            print(f"Client {client_address} disconnected unexpectedly.")
            break
    client_socket.close()
```

### Explanation:

1. **`while True`** → keeps client connected until they disconnect  
2. **`recv(1024)`** → receives messages from this client  
3. **`send()`** → sends reply  
4. **`try-except`** → handles sudden client disconnects  
5. **`client_socket.close()`** → cleanly closes connection

---

# 🖥 Step 3 — Create Server Socket

```python
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5000))
server_socket.listen(5)
print("Server running and waiting for clients...")
```

- TCP socket  
- IPv4  
- Bind to localhost:5000  
- Listen for up to 5 queued connections

---

# 🧵 Step 4 — Accept Clients and Start Threads

```python
while True:
    client_socket, client_address = server_socket.accept()
    # Create a new thread for each client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
```

### Explanation:

1. **`accept()`** → waits for a new client  
2. **`threading.Thread()`** → creates a new thread for this client  
3. **`target=handle_client`** → function to run in thread  
4. **`args=(client_socket, client_address)`** → pass the client socket and address to the function  
5. **`start()`** → starts the thread, allowing simultaneous clients

---

# 💻 Full Multi-Client Server Code

```python
import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Client {client_address} connected.")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                print(f"Client {client_address} disconnected.")
                break
            print(f"Client {client_address} says: {message.decode()}")
            reply = input(f"Server to {client_address}: ")
            client_socket.send(reply.encode())
        except ConnectionResetError:
            print(f"Client {client_address} disconnected unexpectedly.")
            break
    client_socket.close()

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5000))
server_socket.listen(5)
print("Server running and waiting for clients...")

while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
```

---

# 🐍 Client Code (Same as Lesson 4)

```python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5000))
print("Connected to server. Start chatting!")

while True:
    message = input("Client: ")
    client_socket.send(message.encode())
    reply = client_socket.recv(1024)
    if not reply:
        print("Server disconnected")
        break
    print("Server says:", reply.decode())

client_socket.close()
```

---

# 🧪 Example Execution

### Server Terminal

```
Server running and waiting for clients...
Client ('127.0.0.1', 53421) connected.
Client ('127.0.0.1', 53422) connected.
Client ('127.0.0.1', 53421) says: Hello
Server to ('127.0.0.1', 53421): Hi Client1
Client ('127.0.0.1', 53422) says: Hey Server
Server to ('127.0.0.1', 53422): Hello Client2
```

### Client Terminals

**Client1:**
```
Connected to server. Start chatting!
Client: Hello
Server says: Hi Client1
```

**Client2:**
```
Connected to server. Start chatting!
Client: Hey Server
Server says: Hello Client2
```

---

# 📊 Communication Diagram

```
Client1 --------> Thread1 --------> Server
Client2 --------> Thread2 --------> Server
Client3 --------> Thread3 --------> Server
```

Each client is handled independently in **its own thread**.

---

# 🧠 Key Takeaways

- Use **threading** to handle multiple clients  
- Each client has its own **socket and thread**  
- The server can communicate with **many clients simultaneously**  
- `recv()` and `send()` still work the same way  
- Always **close sockets** after disconnects

---

# 🚀 Next Steps

- Implement **broadcasting messages** to all connected clients  
- Learn **UDP multi-client communication**  
- Explore **real-time chat with GUI** (Tkinter or PyQt)  
- Optimize server for **hundreds of simultaneous connections**

---