#! /usr/bin/env python
"""
Copyright (C) 2014 CompleteDB LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the Apache License Version 2.0 http://www.apache.org/licenses.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""

class Response:

    def getStatus(self):
        return self.__parsedJson.get("status", "")

    def getMsg(self):
        return self.__parsedJson.get("msg", "")

    def getAction(self):
        return self.__parsedJson.get("action", "")

    def getPubsubid(self):
        return self.__parsedJson.get("pubsubid", "")

    def getRows(self):
        return self.__parsedJson.get("rows", 0)

    def getFromrow(self):
        return self.__parsedJson.get("fromrow", 0)

    def getTorow(self):
        return self.__parsedJson.get("torow", 0)

    def getColumns(self):
        return self.__parsedJson.get("columns", [])

    def getData(self):
        return self.__parsedJson.get("data", [])

    def reset(self):
        self.__parsedJson = {}

    def setParsedJson(self, data):
        if type(data) is dict:            
            self.__parsedJson = data
        else:
            self.reset()
    
    def __init__(self):
        self.reset()
