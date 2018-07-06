import grpc
import time

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = calculator_pb2.Number(value=123465)

# start computing the call time
t0 = time.time()
# make the call
response = stub.SquareRoot(number)
t1 = time.time()

# return the time of the call
print(response.value)
print(format((t1-t0) * 1000, '.12f'), 'miliseconds')