import rpyc
import time

t0 = time.time()
conn = rpyc.connect('localhost', port=18861, config={"allow_all_attrs": True})
response = conn.root.getValue(10)
t1 = time.time()
print(response)
print(format((t1-t0) * 1000, '.12f'), 'miliseconds')

