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

class Helper:
    
    def __CONNECTION_TIMEOUT_SEC(self):
        return 500.0 / 1000 
    
    def __init__(self):
        self.__socket = None
    
    def is_open(self):
        return self.__socket

    def is_closed(self):
        return not self.is_open()
    
    def open(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.__CONNECTION_TIMEOUT_SEC())
        sock.connect((host, port))
        sock.settimeout(None)
        #
        self.__socket = sock
    
    def close(self):
        if self.is_open():
            try:
                self.__socket.close()
            except:
                pass
            finally:
                self.__socket = None
