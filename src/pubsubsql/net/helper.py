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
    
    def __init__(self):
        self.__socket = None
        self.__header = NetHeader()
    
    def is_open(self):
        return self.__socket

    def is_closed(self):
        return not self.is_open()
    
    def open(self, host, port):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.settimeout(self.__CONNECTION_TIMEOUT_SEC())
        self.__socket.connect((host, port))
        self.__socket.settimeout(None)
    
    def close(self):
        if self.is_open():
            try:
                self.__socket.close()
            except:
                pass
            finally:
                self.__socket = None

    def write_with_header(self, request_id, message_bytes):
        self.__header.set_data(len(message_bytes), request_id)
        self.__socket.sendall(self.__header.get_bytes())
        self.__socket.sendall(message_bytes)
