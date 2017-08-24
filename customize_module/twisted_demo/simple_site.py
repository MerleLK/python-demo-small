"""
@description:
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/22
"""

from twisted.web import server, resource
from twisted.internet import reactor, endpoints


class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        return "<html>Hello, world!</html>"
site = server.Site(Simple())
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8080)
endpoint.listen()
