import time
import rpyc
from rpyc.utils.server import ThreadedServer

import calculator

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        pass

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        pass

    def getValue(self, value): # this is an exposed method
        return calculator.square_root(value)

    exposed_the_real_answer_though = 43     # an exposed attribute

t = ThreadedServer(MyService, port=18861, protocol_config = {"allow_public_attrs" : True})
print('Starting server. Listening on port 18861.')
t.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    t.close()