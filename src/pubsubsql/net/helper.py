#! /usr/bin/env python
"""
Copyright (C) 2014 CompleteDB LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the Apache License Version 2.0 http://www.apache.org/licenses.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""

class Helper:
    
    def __init__(self):
        self.__socket = None
    
    def is_open(self):
        return self.__socket

    def is_closed(self):
        return not self.is_open()
    
    def open(self, sock):
        self.__socket = sock
    
    def close(self):
        if self.is_closed():
            return
        #
        try:
            self.__socket.close()
        except:
            pass
        finally:
            self.__socket = None
