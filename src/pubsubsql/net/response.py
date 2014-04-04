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

    def reset(self):
        self.status = ""
        self.msg = ""
        self.action = ""
        self.pubsubid = ""
        #
        self.rows = 0
        self.fromrow = 0
        self.torow = 0
        #
        self.columns = []
        self.data = []
    
    def __init__(self):
        self.reset()
