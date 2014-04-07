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

class QuickStart:
    """MAKE SURE TO RUN PUBSUBSQL SERVER WHEN RUNNING THE EXAMPLE"""
    
    def quickStart(self):
        print("Quick Start")
        client = Client()
        subscriber = Client()
        
        """
        //----------------------------------------------------------------------------------------------------
        // CONNECT
        //----------------------------------------------------------------------------------------------------
        """
        
        address = "localhost:7777"
        client.connect(address)
        subscriber.connect(address);
        
        """
        //----------------------------------------------------------------------------------------------------
        // SQL MUST-KNOW RULES
        //
        // All commands must be in lower case.
        //
        // Identifiers can only begin with alphabetic characters and may contain any alphanumeric characters.
        //
        // The only available (but optional) data definition commands are
        //    key (unique index)      - key table_name column_name
        //    tag (non-unique index)  - tag table_name column_name
        //
        // Tables and columns are auto-created when accessed.
        //
        // The underlying data type for all columns is String.
        // Strings do not have to be enclosed in single quotes as long as they have no special characters.
        // The special characters are
        //    , - comma
        //      - white space characters (space, tab, new line)
        //    ) - right parenthesis
        //    ' - single quote
        //----------------------------------------------------------------------------------------------------
        """
        
        """
        //----------------------------------------------------------------------------------------------------
        // INDEX
        //----------------------------------------------------------------------------------------------------
        """

        try:
            client.execute("key Stocks Ticker")
            client.execute("tag Stocks MarketCap")
        except:
            # key or tag may have already been defined, so its ok
            pass

        """
        //----------------------------------------------------------------------------------------------------
        // SUBSCRIBE
        //----------------------------------------------------------------------------------------------------
        """

        subscriber.execute("subscribe * from Stocks where MarketCap = 'MEGA CAP'")
        pubsubId = subscriber.getPubSubId()
        print "subscribed to Stocks pubsubid:", pubsubId
        
        """
        //----------------------------------------------------------------------------------------------------
        // PUBLISH INSERT
        //----------------------------------------------------------------------------------------------------
        """
        
        client.execute("insert into Stocks (Ticker, Price, MarketCap) values (GOOG, '1,200.22', 'MEGA CAP')")
        client.execute("insert into Stocks (Ticker, Price, MarketCap) values (MSFT, 38,'MEGA CAP')")
        
        """
        //----------------------------------------------------------------------------------------------------
        // SELECT
        //----------------------------------------------------------------------------------------------------
        """
        
        client.execute("select id, Ticker from Stocks")
        while client.nextRow():
            print "*********************************"
            print "id:{} Ticker:{} \n".format(client.getValue("id"), client.getValue("Ticker"))
        
        """
        //----------------------------------------------------------------------------------------------------
        // PROCESS PUBLISHED INSERT
        //----------------------------------------------------------------------------------------------------
        """
        
        timeout = 100
        while subscriber.waitForPubSub(timeout):
            print "*********************************"
            print "Action:", subscriber.getAction()
            while subscriber.nextRow():
                print "New MEGA CAP stock:", subscriber.getValue("Ticker")
                print "Price:", subscriber.getValue("Price")
        
        """
        //----------------------------------------------------------------------------------------------------
        // PUBLISH UPDATE
        //----------------------------------------------------------------------------------------------------
        """
        
        client.execute("update Stocks set Price = '1,500.00' where Ticker = GOOG")
        
        """
        //----------------------------------------------------------------------------------------------------
        // SERVER WILL NOT PUBLISH INSERT BECAUSE WE ONLY SUBSCRIBED TO 'MEGA CAP'
        //----------------------------------------------------------------------------------------------------
        """
        
        client.execute("insert into Stocks (Ticker, Price, MarketCap) values (IBM, 168, 'LARGE CAP')")

        """
        //----------------------------------------------------------------------------------------------------
        // PUBLISH ADD
        //----------------------------------------------------------------------------------------------------
        """
        
        client.execute("update Stocks set Price = 230.45, MarketCap = 'MEGA CAP' where Ticker = IBM")
        
        """
        //----------------------------------------------------------------------------------------------------
        // PUBLISH REMOVE
        //----------------------------------------------------------------------------------------------------
        """
        
        client.execute("update Stocks set Price = 170, MarketCap = 'LARGE CAP' where Ticker = IBM")
        
        """
        //----------------------------------------------------------------------------------------------------
        // PUBLISH DELETE
        //----------------------------------------------------------------------------------------------------
        """
        
        client.execute("delete from Stocks")
        
        """
        //----------------------------------------------------------------------------------------------------
        // PROCESS ALL PUBLISHED
        //----------------------------------------------------------------------------------------------------
        """
        
        while subscriber.waitForPubSub(timeout):
            print "*********************************"
            print "Action:", subscriber.getAction()
            while subscriber.nextRow():
                for ordinal, column in enumerate(subscriber.getColumns()):
                    print "{}:{}".format(column, subscriber.getValue(ordinal))
                    
        
        """
        //----------------------------------------------------------------------------------------------------
        // UNSUBSCRIBE
        //----------------------------------------------------------------------------------------------------
        """
           
        subscriber.execute("unsubscribe from Stocks")
                
        """
        //----------------------------------------------------------------------------------------------------
        // DISCONNECT
        //----------------------------------------------------------------------------------------------------
        """
        
        subscriber.disconnect();
        client.disconnect();
        print("Done.")

if __name__ == "__main__":
    QuickStart().quickStart()
