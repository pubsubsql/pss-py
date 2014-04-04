#! /usr/bin/env python
"""
Copyright (C) 2014 CompleteDB LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the Apache License Version 2.0 http://www.apache.org/licenses.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""

from pubsubsql.net.helper import Helper as NetHelper

class Client:
    """Client."""
    
    def __nvl(self, string):
        if string:
            return string
        else:
            return ""
    
    def __reset(self):
        pass
        #response = new ResponseData();
        #rawjson = null;
        #record = -1;
    
    def __hardDisconnect(self):
        self.__net.close()
        self.__reset()
    
    def __write(self, message):
        try:
            if self.__net.isClosed():
                raise IOError("Not connected")
            else:
                self.__requestId += 1
                self.__net.writeWithHeader(self.__requestId, message.encode("utf-8"))
        except:
            self.__hardDisconnect()
            raise
    
    def __invalidRequestIdError(self):
        raise Exception("Protocol error invalid request id")
            
    def __readTimeout(self, timeoutSec):
        try:
            if self.__net.isClosed():
                raise IOError("Not connected")
            else:
                return self.__net.readTimeout(timeoutSec)
        except:
            self.__hardDisconnect()
            raise
    
    def __unmarshallJson(self, messageBytes):
        print messageBytes.decode("utf-8")
            
    def isConnected(self):
        """Returns true if the Client is currently connected to the pubsubsql server."""
        return self.__net.isOpen()
    
    def disconnect(self):
        """Disconnects the Client from the pubsubsql server."""
        try:
            if self.isConnected():
                self.__write("close")
        except:
            pass
        finally:
            self.__reset()
            self.__net.close()
    
    def connect(self, address):
        """Connects the Client to the pubsubsql server.
        
        Connects the Client to the pubsubsql server.
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
            else:
                self.__net.open(host, port)

    def execute(self, command):
        """Executes a command against the pubsubsql server.
        
        Executes a command against the pubsubsql server.
        The pubsubsql server returns to the Client a response in JSON format.
        """
        self.__reset()
        self.__write(command)
        while True:
            self.__reset()
            messageBytes = self.__readTimeout(0)
            if not messageBytes:
                raise IOError("Read timed out")
            netRequestId = self.__net.getHeader().getRequestId()
            if netRequestId == self.__requestId:
                # response we are waiting for
                self.__unmarshallJson(messageBytes)
                return
            elif netRequestId == 0:
                pass
            elif netRequestId < self.__requestId:
                # we did not read full result set from previous command ignore it
                self.__reset()
            else:
                self.__invalidRequestIdError()

    def getAction(self):
        """Returns an action string from the response.
        
        Returns an action string from the response
        returned by the last command executed against the pubsubsql server.
        """
        return ""

    def __init__(self):
        self.__requestId = 1
        self.__net = NetHelper()
