# 🧱 Python Socket Programming — Zero to Hero
## Lesson 2: Building Your First TCP Server

In Lesson 1 we learned:

- what sockets are
- client vs server
- TCP vs UDP
- how to create a socket

Now we will build our **first real TCP server**.

We will learn these important functions:

```
socket()
bind()
listen()
accept()
recv()
send()
close()
```

Each one has a **specific role in network communication**.

---

# 🌐 How a TCP Server Works

A server follows a simple workflow:

```
Create Socket
     ↓
Bind Address
     ↓
Listen for Connections
     ↓
Accept Client
     ↓
Receive Data
     ↓
Send Response
     ↓
Close Connection
```

---

# 🖥 Step 1 — Import the Socket Library

### Code

```python
import socket
```

### What it does

This loads Python’s **socket networking module**.

Without it, Python cannot create network connections.

---

# ⚙ Step 2 — Create a Socket

### Code

```python
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### Explanation

This line creates a **TCP socket**.

Parameter meanings:

| Parameter | Meaning |
|----------|---------|
| `socket.AF_INET` | IPv4 addressing |
| `socket.SOCK_STREAM` | TCP protocol |

So this line means:

```
Create a TCP socket using IPv4
```

### Visual

```
Python Program
      │
      ▼
Creates Socket
      │
      ▼
Operating System Networking Stack
```

---

# 📍 Step 3 — Bind the Socket to an Address

### Code

```python
server_socket.bind(("127.0.0.1", 5000))
```

### What bind() Does

`bind()` assigns an **IP address and port** to the server.

This tells the server:

```
Which network interface to use
Which port to listen on
```

### Parameters

```
("IP Address", Port)
```

Example:

```
127.0.0.1 → localhost
5000 → application port
```

Meaning:

```
The server will run on localhost port 5000
```

### Visual

```
Server Socket
      │
      ▼
Bound to
127.0.0.1:5000
```

---

# 👂 Step 4 — Listen for Connections

### Code

```python
server_socket.listen(5)
```

### What listen() Does

This tells the server:

```
Start waiting for client connections
```

The number `5` means:

```
Maximum number of queued connection requests
```

Example queue:

```
Client1
Client2
Client3
Client4
Client5
```

After that the server may reject new connections.

---

# 🤝 Step 5 — Accept Client Connections

### Code

```python
client_socket, client_address = server_socket.accept()
```

### What accept() Does

This function waits until a **client connects**.

When a client connects:

- a **new socket** is created for that client
- the server can communicate with it

### Returned Values

| Value | Meaning |
|------|--------|
| `client_socket` | communication socket |
| `client_address` | client IP + port |

Example output:

```
Client connected from ('127.0.0.1', 53421)
```

### Visual

```
Client --------connects-------> Server
                                    │
                                    ▼
                         New socket created
```

---

# 📩 Step 6 — Receive Data From Client

### Code

```python
message = client_socket.recv(1024)
```

### What recv() Does

This receives data sent from the client.

Parameter:

```
1024
```

Means:

```
Receive up to 1024 bytes of data
```

### Example Data

Client sends:

```
Hello server
```

Server receives:

```
b'Hello server'
```

Note: Data arrives as **bytes**.

---

# 📤 Step 7 — Send Data to Client

### Code

```python
client_socket.send(b"Hello from server")
```

### What send() Does

Sends data back to the client.

Important rule:

```
Network data must be sent as bytes
```

Example:

```
b"Hello"
```

The `b` means **byte string**.

---

# 🔚 Step 8 — Close the Connection

### Code

```python
client_socket.close()
server_socket.close()
```

### What close() Does

Closes the connection and releases resources.

Why important?

```
Prevents memory leaks
Frees network ports
```

---

# 💻 Full TCP Server Code

Now let's combine everything.

```python
import socket

# Step 1: Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind address and port
server_socket.bind(("127.0.0.1", 5000))

# Step 3: Start listening
server_socket.listen(5)

print("Server is running...")

# Step 4: Accept client
client_socket, client_address = server_socket.accept()

print("Client connected:", client_address)

# Step 5: Receive data
message = client_socket.recv(1024)

print("Client says:", message.decode())

# Step 6: Send response
client_socket.send(b"Hello from server")

# Step 7: Close connection
client_socket.close()
server_socket.close()
```

---

# 🧪 Example Program Output

Server terminal:

```
Server is running...
Client connected: ('127.0.0.1', 53421)
Client says: Hello server
```

---

# 📊 Communication Diagram

```
Client                       Server

        connect()  ----------->
                          accept()

        send()     ----------->
                          recv()

                     <----------- send()

        close()     ----------->
                          close()
```

---

# 🧠 Key Functions Summary

| Function | Purpose |
|--------|---------|
| socket() | create socket |
| bind() | assign IP + port |
| listen() | wait for clients |
| accept() | accept connection |
| recv() | receive data |
| send() | send data |
| close() | close socket |

---

# 🎯 What You Learned

You now understand how to:

- create a TCP server
- bind to an address
- listen for clients
- accept connections
- send and receive messages

This is the **foundation of real network servers**.

---

# 🚀 Next Lesson (Lesson 3)

Next we will build the **TCP Client** that connects to this server.

You will learn:

```
connect()
send()
recv()
```

And run a **real client-server chat between two programs**.

---