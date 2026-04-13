---
layout: assignment
due: 2026-04-14 23:59:59 -0700
permalink: assignments/lab06.html
title: lab06 - HTTP server part 1 ping-pong
github_url: https://classroom.github.com/a/UWCjkvqR
published: true
---

## Requirements

In project05, you will be implementing an [HTTP server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server), i.e. a program that handles an HTTP request and sends back an HTTP response. HTTP requests and responses are sent over TCP. In preparation for project05, you will implement a simple server on TCP.
- The server should listen for incoming TCP connections on port 8000 (because port 80 is a privileged port)
- When a client connects, the server should wait for incoming data from the client.
- If the incoming message is "PING", the server should respond with "PONG" and close the TCP connection.
- If the incoming message is any other message, the server should respond with "INVALID" and close the TCP connection.

## Implementation

You may use the following libraries:

- `<sys/socket.h>` for socket programming.
	- Create a TCP socket using `socket()` function. 
	- Bind the socket to a specified port using `bind()` function. (`man 2 bind`)
	- Start listening for incoming TCP connections using `listen()` function. 
	- When a client connects, accept the connection using `accept()` function.
	- Receive data from the client using `recv()` function.
	- If the incoming message is "PING", send "PONG" message back to the client using `send()` function.
	- If the incoming message is any other message, send "INVALID" message back to the client using `send()` function.
- < unistd.h> for closing connection.
	- Close the connection using `close()` function.	

## Example Output

If you run your server in the background using `&`, note the process ID (pid)
```sh
$ ./lab06 -p 8000 &
[1] 14205
```
Use `telnet` to connect to your server 
```sh
$ telnet localhost 8000
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
```
Type `PING` and your server should respond with `PONG` 
```sh
PING
PONG
Connection closed by foreign host.
```
You can stop your server using the `pkill` command
```sh
$ pkill -x lab06
```

## Implementation Notes

### Starting your server

1. When your server starts, it should use `getaddrinfo()` to get a list of possible socket parameters from the operating system
	1. You should loop over the linked list of results using `ai_next`, trying 
		```
		hints.ai_family = AF_INET;
		hints.ai_socktype = SOCK_STREAM;
		hints.ai_flags = AI_PASSIVE
		hints.ai_protocol = IPPROTO_TCP
		```
	1. For each result, you should call `socket()` with the `ai_family`, `ai_socktype`, and `ai_protocol` for the result. If `socket()` returns -1, keep looking through the results list.
1. Once you have a valid (not -1) socket, you should configure the socket for a server
	1. `setsockopt(fd, SOL_SOCKET, SO_REUSEADDR...)` tells the operating system that it's ok for more than one server to accept connections on this IP address 
	1. `ioctl(fd, FIONBIO...)` tells the operating system that we will use "non-blocking I/O" 
1. Then we can use `bind()` to connect the network socket with the port and protocol for the matching result (from `getaddrinfo()`)
1. Finally we can use `listen()` to tell the operating system that any connection requests should come through the port we just bound.

### Connection Requests

1. When clients try to connect to our server, the socket we listened on will be readable
1. When that happens, we will call `accept()` to create a new socket for the client to talk to. Therefore, we have only one listener socket, but a new socket for each accepted connection.

## Handling Traffic

1. When a client sends network traffic to our server, we can `read()` (or `recv()`) the readable socket.
1. We can `send()` our response to the client and (for this lab) `close()` the connection

## Debugging Tips 

1. When debugging your server, you may run it in the background (using `&`) or in the foreground if you want to run it in `gdb` or watch `printf()` output
1. If you try to run your server and get an error like this:
	```sh
	$ bind: Address already in use
	```
	that means your server is still bound to the port and you need to kill it.
	```sh
	$ ps ax |grep lab06
	14280 pts/0    S      0:00 ./lab06 -p 8000
	14283 pts/0    S+     0:00 grep --color=auto lab06
	$ kill 14280
	```

## Connection Steps

1. Develop and debug your server on a `clab` container as usual. For consistency, use port 8000.
2. Use `ip a` to learn the container's IPv4 address. It will start with `172.17.0`
3. Open a new terminal tab or window and create an ssh tunnel like this:

    `ssh -J stargate -L 8000:172.17.0.7:8000 your_usf_username@medusa`
4. Open another new terminal tab or window and telnet to your server

    `telnet localhost 8000`

## Rubric

1. Since the SSH tunnel doesn't integrate nicely with autograder, we will grade the socket labs and project by hand.
2. For this assignment, we will test the tunnel and PING/PONG steps as shown here.
