# 🧱 Python Socket Programming — Zero to Hero
## Lesson 4: Interactive TCP Chat Application

Now that we have a working **server and client**, let’s make them **communicate continuously** like a real chat program.

---

# 🌐 How a Chat Application Works

```
Client1                           Server
   │                                │
   ├─ connect() ------------------> socket()
   │                                │
   ├─ send("Hello") --------------> recv()
   │                                │
   <------ send("Hi") ------------- recv()
   │                                │
Repeat until one closes the connection
```

---

# 🖥 Step 1 — Create a TCP Server with Continuous Listening

```python
import socket

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind address
server_socket.bind(("127.0.0.1", 5000))

# Listen for clients
server_socket.listen(1)

print("Server is running... Waiting for a client.")

# Accept client connection
client_socket, client_address = server_socket.accept()
print("Client connected:", client_address)

# Continuous chat
while True:
    # Receive message
    message = client_socket.recv(1024)
    if not message:
        # Client disconnected
        print("Client disconnected")
        break
    print("Client says:", message.decode())

    # Send reply
    reply = input("Server: ")
    client_socket.send(reply.encode())

# Close connections
client_socket.close()
server_socket.close()
```

---

# 🔎 Step 1 Explanation

1. **Create socket**

```python
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- TCP socket, IPv4

2. **Bind address**

```python
server_socket.bind(("127.0.0.1", 5000))
```

- Bind to localhost and port 5000

3. **Listen**

```python
server_socket.listen(1)
```

- Wait for a client  
- `1` = max queued connections

4. **Accept client**

```python
client_socket, client_address = server_socket.accept()
```

- Creates a new socket for client communication

5. **Continuous chat**

```python
while True:
    message = client_socket.recv(1024)
    if not message:
        break
    print("Client says:", message.decode())
    reply = input("Server: ")
    client_socket.send(reply.encode())
```

- `recv()` receives client messages  
- `input()` takes server reply  
- `send()` sends reply to client  
- `break` exits if client disconnects

6. **Close connections**

```python
client_socket.close()
server_socket.close()
```

---

# 🖥 Step 2 — Create TCP Client for Chat

```python
import socket

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(("127.0.0.1", 5000))

print("Connected to server. Start chatting!")

# Continuous chat
while True:
    message = input("Client: ")
    client_socket.send(message.encode())

    # Receive server reply
    reply = client_socket.recv(1024)
    if not reply:
        print("Server disconnected")
        break
    print("Server says:", reply.decode())

# Close connection
client_socket.close()
```

---

# 🔎 Step 2 Explanation

1. **Create socket**

```python
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- TCP socket

2. **Connect to server**

```python
client_socket.connect(("127.0.0.1", 5000))
```

- Connects client to server socket

3. **Continuous chat**

```python
while True:
    message = input("Client: ")
    client_socket.send(message.encode())
    reply = client_socket.recv(1024)
    if not reply:
        break
    print("Server says:", reply.decode())
```

- `input()` for message  
- `send()` to server  
- `recv()` to get server reply  
- Exit if server disconnects

4. **Close connection**

```python
client_socket.close()
```

---

# 🧪 Example Execution

### Server Terminal

```
Server is running... Waiting for a client.
Client connected: ('127.0.0.1', 53421)
Client says: Hello
Server: Hi there!
Client says: How are you?
Server: I'm good, thanks!
```

### Client Terminal

```
Connected to server. Start chatting!
Client: Hello
Server says: Hi there!
Client: How are you?
Server says: I'm good, thanks!
```

---

# 📊 Communication Diagram

```
Client                         Server
  │                               │
  │ connect() -----------------> socket()
  │ send("Hello") ------------> recv()
  │ <------------ send("Hi")  recv()
  │ send("How are you?") ----> recv()
  │ <----------- send("I'm good, thanks!") recv()
  │
Repeat until disconnect
```

---

# 🧠 Key Takeaways

- `while True` allows **continuous communication**
- `recv()` waits for messages
- `send()` sends bytes
- `input()` lets user type replies
- Proper `close()` is important to release resources
- You now have a **working interactive TCP chat**

---

# 🚀 Next Steps

- Implement **multiple clients** connecting to a single server  
- Learn **threading in Python** to handle multiple clients simultaneously  
- Explore **UDP chat** and compare TCP vs UDP in real scenarios

---