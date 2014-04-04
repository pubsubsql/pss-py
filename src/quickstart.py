#! /usr/bin/env python
"""
Copyright (C) 2014 CompleteDB LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the Apache License Version 2.0 http://www.apache.org/licenses.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""

from pubsubsql import Client

def main():
    print("Quick Start")
    client = Client()
    client.connect("localhost:7777")
    client.execute("status")
    print client.getJSON()
    client.disconnect()
    print("Done.")

main()
