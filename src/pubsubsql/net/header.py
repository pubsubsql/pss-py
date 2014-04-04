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
    
    def getHeaderSizeB(self):
        return 8

    def getMessageSizeB(self):
        return self.__messageSizeB 
    
    def getRequestId(self):
        return self.__requestId 

    def getHeaderBuffer(self):
        return self.__buffer

    def getBytes(self):
        return self.getHeaderBuffer()
        
    def unpackBuffer(self):
        self.__messageSizeB, self.__requestId = \
            struct.unpack_from(">II", buffer(self.__buffer), 0)
    
    def packBuffer(self):
        struct.pack_into(">II", self.__buffer, 0,
                         self.__messageSizeB,
                         self.__requestId)
    
    def setData(self, messageSizeB, requestId):
        self.__messageSizeB = messageSizeB
        self.__requestId = requestId
        #
        self.packBuffer()

    def __init__(self, messageSizeB = 0, requestId = 0):
        self.__buffer = bytearray(self.getHeaderSizeB())
        self.setData(messageSizeB, requestId)
