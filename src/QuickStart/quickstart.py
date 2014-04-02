#! /usr/bin/env python
"""
Copyright (C) 2014 CompleteDB LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the Apache License Version 2.0 http://www.apache.org/licenses.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""

import socket
import time

def disconnect(sock):
    """disconnect disconnects the Client from the pubsubsql server."""
    print("disconnect...")
    sock.close()

def connect(address):
    """connect connects the Client to the pubsubsql server.
    address string has the form host:port."""
    print("connect...")
    #disconnect()
    # set host and port 
    host, sep, port = address.partition(":")
    # validate address
    if not sep:
        raise ValueError("Invalid network address")
    elif not host:
        raise ValueError("Host is not provided")
    elif not port:
        raise ValueError("Port is not provided")
    else:
        port = int(port)
        if 0 == port:
            raise ValueError("Invalid port")
    # connect
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock

def main():
    print("Quick Start")
    sock = connect("localhost:7777")
    #sock.send('Hello, world')
    #data = sock.recv(1024)
    #print 'Received', repr(data)
    time.sleep(5) # seconds
    disconnect(sock)
    print("Done.")

main()
