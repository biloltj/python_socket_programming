# 🧱 Python Socket Programming — Zero to Hero
## Lesson 3: Building the TCP Client

In Lesson 2 we created a **TCP Server**.

Now we will create a **TCP Client** that connects to that server.

After this lesson you will have a **complete working network program**.

---

# 🌐 Client–Server Communication Overview

```
Client                          Server

Create socket              Create socket
Connect -----------------> Bind
Send message ------------> Listen
Receive response <------- Accept
Close connection          Send response
```

---

# 🎯 Goal of This Lesson

We will create a client that:

1. Connects to the server
2. Sends a message
3. Receives a reply
4. Closes the connection

---

# Step 1 — Import the Socket Library

### Python Code

```python
import socket
```

### What it does

This loads Python's **socket networking module**.

Without this module Python cannot create network connections.

---

# Step 2 — Create a Socket

### Python Code

```python
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### Explanation

This creates a **TCP socket**.

Parameters used:

| Parameter | Meaning |
|----------|---------|
socket.AF_INET | Use IPv4 addresses |
socket.SOCK_STREAM | Use TCP protocol |

Meaning:

```
Create a TCP socket using IPv4
```

---

# Step 3 — Connect to the Server

### Python Code

```python
client_socket.connect(("127.0.0.1", 5000))
```

### What `connect()` Does

This function tells the client:

```
Connect to server at IP 127.0.0.1 on port 5000
```

Explanation:

| Value | Meaning |
|------|--------|
127.0.0.1 | localhost (same computer) |
5000 | server port |

---

# Step 4 — Send a Message to the Server

### Python Code

```python
client_socket.send(b"Hello server")
```

### What `send()` Does

This sends data to the server.

Important rule:

```
Data must be sent as bytes
```

Example:

```
b"Hello server"
```

The `b` means **byte string**.

---

# Step 5 — Receive Response from Server

### Python Code

```python
response = client_socket.recv(1024)
```

### What `recv()` Does

This receives data from the server.

Parameter:

```
1024
```

Means:

```
Receive up to 1024 bytes of data
```

---

# Step 6 — Print the Server Response

### Python Code

```python
print("Server says:", response.decode())
```

### Explanation

`decode()` converts **bytes → normal text**.

Example:

```
b"Hello from server"
```

becomes

```
Hello from server
```

---

# Step 7 — Close the Connection

### Python Code

```python
client_socket.close()
```

### What `close()` Does

Closes the socket connection.

Why important?

- frees system resources
- prevents port conflicts

---

# 💻 Full TCP Client Code

Here is the **complete working client program**.

```python
import socket

# Step 1: Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to server
client_socket.connect(("127.0.0.1", 5000))

# Step 3: Send message
client_socket.send(b"Hello server")

# Step 4: Receive response
response = client_socket.recv(1024)

# Step 5: Print response
print("Server says:", response.decode())

# Step 6: Close connection
client_socket.close()
```

---

# 🧪 Example Execution

## Start the Server First

Run the server program from Lesson 2.

Server output:

```
Server is running...
```

---

## Then Run the Client

Client output:

```
Server says: Hello from server
```

---

# 📊 Communication Diagram

```
Client                               Server

socket()                        socket()

connect()  -------------------> accept()

send("Hello server") ---------> recv()

                         <------ send("Hello from server")

recv()                   <------

close()                  close()
```

---

# 🧠 Function Summary

| Function | Purpose |
|--------|---------|
socket() | create socket |
connect() | connect to server |
send() | send data |
recv() | receive data |
close() | close connection |

---

# 🎯 What You Learned

You now understand how to:

- build a TCP client
- connect to a server
- send messages
- receive responses
- close network connections

You now have a **complete working client-server system**.

---

# 🚀 Next Lesson

Next we will build a **Real Chat Application** using sockets.

New concepts:

```
while loops
multiple messages
continuous communication
```

Your program will look like:

```
Client: Hello
Server: Hi
Client: How are you?
Server: I'm good
```

You will create your **first real networking application**.

---