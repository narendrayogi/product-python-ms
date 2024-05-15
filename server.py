import grpc
from concurrent import futures
import time
# from proto import product_pb2_grpc as pb2_grpc
# from proto import product_pb2 as pb2
import product_pb2_grpc as pb2_grpc
import product_pb2 as pb2

class ProductService(pb2_grpc.ProductService):

    def __init__(self, *args, **kwargs):
        pass

    def ListProduct(self, request, context):

        # get the string from the incoming request
        isActive = request.isActive
        items = [{"productId": "1", "name": f'Hello I am up and running received "{isActive}" message from you', "isActive": isActive }]
        result = {'items': items}

        return pb2.ListProductResp(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()