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
from header import Header as NetHeader

class Helper:
    
    def __CONNECTION_TIMEOUT_SEC(self):
        return 500.0 / 1000 
        
    def isOpen(self):
        return self.__socket

    def isClosed(self):
        return not self.isOpen()
    
    def open(self, host, port):
        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.settimeout(self.__CONNECTION_TIMEOUT_SEC())
            self.__socket.connect((host, port))
            self.__socket.settimeout(None)
        except:
            self.__socket = None
            raise
    
    def close(self):
        if self.isOpen():
            try:
                self.__socket.close()
            except:
                pass
            finally:
                self.__socket = None

    def writeWithHeader(self, requestId, messageBytes):
        self.__netHeader.setData(len(messageBytes), requestId)
        self.__socket.sendall(self.__netHeader.getBytes())
        self.__socket.sendall(messageBytes)

    def __init__(self):
        self.__socket = None
        self.__netHeader = NetHeader()
