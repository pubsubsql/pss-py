#! /usr/bin/env python
"""
Copyright (C) 2014 CompleteDB LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the Apache License Version 2.0 http://www.apache.org/licenses.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""

import unittest
from header import Header as NetHeader

class TestHeader(unittest.TestCase):
         
    def setUp(self):
        pass

    def tearDown(self):
        pass
         
    def testGetBytes(self):
        header1 = NetHeader(32567, 9875235)
        header2 = NetHeader(0, 0)
        #
        buffer_bytes = header1.getBytes()
        header2.getBytes()[:] = buffer_bytes
        header2.unpackBuffer()
        #
        self.assertEqual(header1.getMessageSizeB(),
                         header2.getMessageSizeB(),
                         "MessageSize do not match")
        #
        self.assertEqual(header1.getRequestId(),
                         header2.getRequestId(),
                         "RequestId do not match")

    def testSetData(self):
        header1 = NetHeader()
        header2 = NetHeader()
        #
        header1.setData(32567, 9875235)
        buffer_bytes = bytearray(100)
        buffer_bytes[:] = header1.getBytes()
        #
        header2.getBytes()[:] = buffer_bytes
        header2.unpackBuffer()
        #
        self.assertEqual(header1.getMessageSizeB(),
                         header2.getMessageSizeB(),
                         "MessageSize do not match")
        #
        self.assertEqual(header1.getRequestId(),
                         header2.getRequestId(),
                         "RequestId do not match")

if __name__ == "__main__":
    unittest.main()
