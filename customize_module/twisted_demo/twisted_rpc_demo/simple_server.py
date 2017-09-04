"""
@description:??
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-9-4
"""

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

#
# class RequestHandler(SimpleXMLRPCRequestHandler):
#     rpc_paths = ('/RPC2',)
#
#
# with SimpleXMLRPCServer(("localhost", 8000),
#                         requestHandler=RequestHandler) as server:
#     server.register_introspection_functions()
#
#     server.register_function(pow)
#
#
#     def add_function(x, y):
#         return x + y
#
#
#     server.register_function(add_function, 'add')
#
#
#     class MyFuncs(object):
#         def mul(self, x, y):
#             return x * y
#
#
#     server.register_instance(MyFuncs())
#
#     server.serve_forever()

import datetime

import sys


class ExampleService(object):
    def get_data(self):
        return '42'

    class CurrentTime:
        @staticmethod
        def get_current_time():
            return datetime.datetime.now()


with SimpleXMLRPCServer(('localhost', 8000)) as server:
    server.register_function(pow)
    server.register_function(lambda x, y: x + y, 'add')
    server.register_instance(ExampleService(), allow_dotted_names=True)
    server.register_multicall_functions()
    print("Servering XML-RPC on localhost port 8000...")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        compile("\nKeyboard interrupt received, exiting.")
        sys.exit(0)
