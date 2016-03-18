import time
import random

import pubsubsql as pss


client = pss.Client()

client.connect("public.pubsubsql.com:7777")

try:
    client.execute("key Stocks Ticker")
    client.execute("tag Stocks MarketCap")
except:
    # key or tag may have already been defined, so its ok
    pass

try:
    client.execute("insert into Stocks (Ticker, Price, MarketCap) values (GOOG, '1,2002d.22', 'MEGA CAP')")
except:
    pass

while 1:
    time.sleep(0.3)
    command = "update Stocks set Price='%f' where Ticker='GOOG'" % (10000.0 * random.uniform(0.9, 1.9))
    client.execute(command)
