#! /usr/bin/env python
"""
Copyright (C) 2014 CompleteDB LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the Apache License Version 2.0 http://www.apache.org/licenses.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""

import json
from pubsubsql.net.helper import Helper as NetHelper
from pubsubsql.net.response import Response as ResponseData

class Client:
    """Client."""
    
    def __nvl(self, string):
        if string:
            return string
        else:
            return ""
    
    def __reset(self):
        self.__rawJson = ""
        self.__response.reset()
        self.__record = -1
    
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
                
    def __readTimeout(self, timeoutSec):
        try:
            if self.__net.isClosed():
                raise IOError("Not connected")
            else:
                return self.__net.readTimeout(timeoutSec)
        except:
            self.__hardDisconnect()
            raise

    def __invalidRequestIdError(self):
        raise Exception("Protocol error invalid request id")

    def __setColumns(self):
        self.__columns.clear()
        columns = self.__response.getColumns()
        if columns:
            for index, column in enumerate(columns):
                self.__columns[column] = index

    def __unmarshallJson(self, messageBytes):
        self.__rawJson = messageBytes.decode("utf-8")
        self.__response.setParsedJson(json.loads(self.__rawJson))
        if self.__response.getStatus() == "ok":
            self.__setColumns()
        else:
            raise ValueError(self.__response.getMsg())

    def __getColumn(self, column):
        pass

    def __getValueByColumnName(self, column):
        print self.__response.getData()
        print self.__response.getColumns()
        return ""

    def __getValueByColumnOrdinal(self, ordinal):
        print self.__response.getData()
        print self.__response.getColumns()
        return ""

    def getValue(self, column):
        """Returns the value within the current row for the given column name or column ordinal.
        
        If the column name does not exist, Value returns an empty string.
        The column ordinal represents the zero based position of the column in the Columns collection of the result set.
        If the column ordinal is out of range, getValue returns an empty string.
        """
        print "len: " + str(len(self.__response.getData()))
        if isinstance(column, basestring):
            return self.__getValueByColumnName(column)
        else:
            return self.__getValueByColumnOrdinal(column)

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

    def stream(self, command):
        """Sends a command to the pubsubsql server.
        
        Sends a command to the pubsubsql server.
        The pubsubsql server does not return a response to the Client.
        """
        self.__reset()
        self.__write("stream " + command)

    def getJSON(self):
        """Returns a response string in JSON format.
        
        Returns a response string in JSON format from the 
        last command executed against the pubsubsql server.
        """
        return self.__nvl(self.__rawJson)

    def getAction(self):
        """Returns an action string from the response.
        
        Returns an action string from the response
        returned by the last command executed against the pubsubsql server.
        """
        return self.__nvl(self.__response.getAction())

    def getPubSubId(self):
        """Returns a unique identifier generated by the pubsubsql server.
        
        Returns a unique identifier generated by the pubsubsql server when
        a Client subscribes to a table. If the client has subscribed to more than one table, 
        getPubSubId should be used by the Client to uniquely identify messages 
        published by the pubsubsql server.
        """
        return self.__nvl(self.__response.getPubsubid())

    def getRowCount(self):
        """Returns the number of rows in the result set returned by the pubsubsql server."""
        return self.__nvl(self.__response.getRows())

    def nextRow(self):
        """Move to the next row in the result set returned by the pubsubsql server.
        
        Move to the next row in the result set returned by the pubsubsql server.
        When called for the first time, NextRow moves to the first row in the result set.
        Returns false when all rows are read.
        """
        while True:
            # no result set
            if not self.__response.getRows():
                return False
            if not self.__response.getFromrow():
                return False
            if not self.__response.getTorow():
                return False
            # the current record is valid
            self.__record += 1
            delta = self.__response.getTorow() - self.__response.getFromrow()
            if self.__record <= delta:
                return True
            # we reached the end of the result set?
            if self.__response.getRows() == self.__response.getTorow():
                self.__record -= 1
                return False
            # there is another batch of data
            self.__reset()
            messageBytes = self.__readTimeout(0)
            if not messageBytes:
                raise IOError("Read timed out")
            netRequestId = self.__net.getHeader().getRequestId()
            if netRequestId != self.__requestId:
                self.__invalidRequestIdError()
            self.__unmarshallJson(messageBytes)

    def __init__(self):
        self.__requestId = 1
        self.__record = -1
        self.__rawJson = ""
        self.__net = NetHelper()
        self.__response = ResponseData()
        self.__columns = {}
