"""
@description: This is a simple rpc server demo
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-9-3
@detail:
    How to build a client.
    in Python2 you can use the module xmlrpclib
    just as the follows:

    In [9]: import xmlrpclib
    In [10]: c = xmlrpclib.Server('http://localhost:7080/')
    In [11]: c.echo("Hello")
    Out[11]: 'Hello'
    In [12]: c.add(1,2)
    Out[12]: 3
"""

import sys

import datetime
from twisted.internet import reactor, endpoints
from twisted.web import xmlrpc, server
from twisted.python import log


class RpcServer(xmlrpc.XMLRPC):
    def xmlrpc_echo(self, x):
        """ Just return the x """
        return x

    def xmlrpc_add(self, x, y):
        """ Just return the x+y """
        return x + y

    def xmlrpc_fault(self):
        """ raise a error for the procedure should not be used """
        raise xmlrpc.Fault(123, "This is a fault!")


class GetDate(xmlrpc.XMLRPC):
    """return the time now"""

    def xmlrpc_time(self):
        return datetime.datetime.now()


log.startLogging(sys.stdout)

if __name__ == '__main__':
    r = RpcServer()
    date = GetDate()
    # r is the main procedure thread and the other is others thread
    r.putSubHandler('date', date)  # add a instance to the sub handler
    reactor.listenTCP(7080, server.Site(r))

    # endpoint = endpoints.TCP4ServerEndpoint(reactor, 7080)
    # endpoint.listen(server.Site(r))
    print("The Server is listening on port at {p}".format(p=7080))
    reactor.run()
