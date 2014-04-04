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
from pubsubsql.net.helper import Helper

class Client:
    """Client."""
    
    def __init__(self):
        self.__net = Helper() 
    
    def __CONNECTION_TIMEOUT_SEC(self):
        return 500.0 / 1000 
    
    def is_connected(self):
        """Returns true if the Client is currently connected to the pubsubsql server."""
        return self.__net.is_open()
    
    def disconnect(self):
        """Disconnects the Client from the pubsubsql server."""
        self.__net.close()
    
    def connect(self, address):
        """Connects the Client to the pubsubsql server.
        
        The address string has the form host:port.
        """
        #disconnect()
        # set host and port 
        host, separator, port = address.partition(":")
        # validate address
        if not separator:
            raise ValueError("Invalid network address", address)
        elif not host:
            raise ValueError("Host is not provided")
        elif not port:
            raise ValueError("Port is not provided")
        else:
            try:
                port = int(port)
            except:
                raise ValueError("Invalid port", port)
        # connect
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.__CONNECTION_TIMEOUT_SEC())
        sock.connect((host, port))
        sock.settimeout(None)
        self.__net.open(sock)
