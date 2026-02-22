# Programming Assignment 1: Socket Programming

## Author
* Student: Bilol  
* Course Name: Computer Networking  
* Instructor Name: Habib Safarov  
* Date: 23.02.2026  

---

## Overview

This project implements a TCP client-server application using Python socket programming.

The client:
- Accepts an integer between 1 and 100
- Connects to the server using TCP
- Sends its name and integer value
- Receives the server’s name and integer
- Computes and displays the sum

The server:
- Listens for incoming client connections
- Receives client name and integer
- Displays client and server information
- Computes and displays the sum
- Sends its name and chosen integer back to the client
- Terminates if an out-of-range integer is received

---

## How It Works

### Protocol Format

Messages are formatted as:

Client → Server: