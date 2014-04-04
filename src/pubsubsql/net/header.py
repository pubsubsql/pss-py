#! /usr/bin/env python
"""
Copyright (C) 2014 CompleteDB LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the Apache License Version 2.0 http://www.apache.org/licenses.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""

import struct

class Header:
    """
    --------------------+--------------------
    |   message_size    |    request_id     |
    --------------------+--------------------
    |      uint32       |      uint32       |
    --------------------+--------------------
    (BIG ENDIAN)
    """
    
    def __HEADER_SIZE_B(self):
        return 8
    
    def __init__(self):
        self.__buffer = bytearray(self.__HEADER_SIZE_B())
        #
        self.__message_size = 0
        self.__request_id = 0

    def set_data(self, message_size, request_id):
        self.__message_size = message_size
        self.__request_id = request_id
        #
        struct.pack_into(">II", self.__buffer, 0,
                         self.__message_size,
                         self.__request_id)

    def get_bytes(self):
        return self.__buffer
    
