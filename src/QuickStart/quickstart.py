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

def connect():
    """connect connects the Client to the pubsubsql server.
    address string has the form host:port."""
    print("connect...")
    host = socket.gethostname()
    port = 7777
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    #s.send('Hello, world')
    #data = s.recv(1024)
    #print 'Received', repr(data)
    return sock

def disconnect(sock):
    """disconnect disconnects the Client from the pubsubsql server."""
    print("disconnect...")
    sock.close()

def main():
    print("Quick Start")
    sock = connect()
    time.sleep(5) # seconds
    disconnect(sock)
    print("Done.")

main()
