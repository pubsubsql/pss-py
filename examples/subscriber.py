import time
import random

import pubsubsql as pss


subscriber = pss.Client()

subscriber.connect("public.pubsubsql.com:7777")

subscriber.execute("subscribe * from Stocks where MarketCap = 'MEGA CAP'")

timeout = 60000

while subscriber.waitForPubSub(timeout):
    print "*********************************"
    print "Action:{}".format(subscriber.getAction())
    while subscriber.nextRow():
        for ordinal, column in enumerate(subscriber.getColumns()):
            print "{}:{}".format(column, subscriber.getValue(ordinal)),
        print ""
