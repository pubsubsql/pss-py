#! /usr/bin/env python
"""
Copyright (C) 2014 CompleteDB LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the Apache License Version 2.0 http://www.apache.org/licenses.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""

from pubsubsql import connect, disconnect
import time

def main():
    print("Quick Start")
    print("connect...")
    sock = connect("localhost:7777")
    #sock.send('Hello, world')
    #data = sock.recv(1024)
    #print 'Received', repr(data)
    time.sleep(5) # seconds
    print("disconnect...")
    disconnect(sock)
    print("Done.")

main()
