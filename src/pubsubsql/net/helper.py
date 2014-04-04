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

    def __readSocket(self, dstBuffer, readSizeB):
        toRead = readSizeB
        view = memoryview(dstBuffer)
        while toRead > 0:
            readCount = self.__socket.recv_into(view)
            if readCount > 0:
                view = view[readCount:]
                toRead -= readCount
            else:
                raise Exception("Failed to read socket")

        
    def __readHeader(self):
        self.__readSocket(self.__netHeader.getHeaderBuffer(),
                          self.__netHeader.getHeaderSizeB())
        self.__netHeader.unpackBuffer()
    
    def __readData(self):
        dataSizeB = self.__netHeader.getMessageSizeB()
        if dataSizeB < 0:
            raise Exception("Invalid message size", dataSizeB)
        if len(self.__dataBuffer) < dataSizeB:
            self.__dataBuffer = bytearray(dataSizeB)
        self.__readSocket(self.__dataBuffer, dataSizeB)
        view = memoryview(self.__dataBuffer)
        return view[:dataSizeB]
                     
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

    def read(self):
        self.__readHeader()
        return self.__readData()
    
    def readTimeout(self, socketTimeoutSec):
        try:
            self.__socket.settimeout(socketTimeoutSec)
            return self.read()
        except socket.timeout:
            return None

    def __init__(self):
        self.__socket = None
        self.__netHeader = NetHeader()
        self.__dataBuffer = bytearray()
