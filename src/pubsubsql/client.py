#! /usr/bin/env python
"""
Copyright (C) 2014 CompleteDB LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the Apache License Version 2.0 http://www.apache.org/licenses.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""

from pubsubsql.net.helper import Helper

class Client:
    """Client."""
    
    def __reset(self):
        pass
        #response = new ResponseData();
        #rawjson = null;
        #record = -1;
    
    def __hard_disconnect(self):
        #backlog.clear();
        self.__net.close()
        self.__reset()
    
    def __write(self, message):
        try:
            pass
            #if (!rw.isValid()) throw new IOException("Not connected");
            #requestId++;
            #rw.writeWithHeader(requestId, message.getBytes(UTF8_CHARSET));
        except:
            self.__hard_disconnect()
            raise
    
    def __init__(self):
        self.__request_id = 1
        self.__net = Helper() 
        
    def is_connected(self):
        """Returns true if the Client is currently connected to the pubsubsql server."""
        return self.__net.is_open()
    
    def disconnect(self):
        """Disconnects the Client from the pubsubsql server."""
        #backlog.clear();
        try:
            if self.is_connected():
                self.__write("close")
        except:
            self.__reset()
            self.__net.close()
    
    def connect(self, address):
        """Connects the Client to the pubsubsql server.
        
        The address string has the form host:port.
        """
        self.disconnect()
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
        self.__net.open(host, port)
