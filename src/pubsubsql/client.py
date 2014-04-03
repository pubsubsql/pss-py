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

CONNECTION_TIMEOUT_SEC = 500.0 / 1000

def disconnect(sock):
    """Disconnects the Client from the pubsubsql server.
    """
    sock.close()

def connect(address):
    """Connects the Client to the pubsubsql server.
    
    The address string has the form host:port.
    """
    #disconnect()
    # set host and port 
    host, separator, port = address.partition(":")
    # validate address
    if not separator:
        raise ValueError("Invalid network address")
    elif not host:
        raise ValueError("Host is not provided")
    elif not port:
        raise ValueError("Port is not provided")
    else:
        port = int(port)
        if not port:
            raise ValueError("Invalid port")
    # connect
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(CONNECTION_TIMEOUT_SEC)
    sock.connect((host, port))
    sock.settimeout(None)
    return sock