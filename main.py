import proxy
import proxyBroadcaster
from threading import *

# Create threads for each method
t1 = Thread(target=proxy.start)
t2 = Thread(target=proxyBroadcaster.broadCast)

# Start both threads
t1.start()
t2.start()

# (Optional) Wait for both threads to complete
t1.join()
t2.join()