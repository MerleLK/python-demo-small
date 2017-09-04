"""
@description: not use the twisted, just use the xmlrpc module
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-9-3
@details:
    How to use:
    in python3, you can use the module xmlrpc

    In [1]: from xmlrpc.client import ServerProxy

    In [2]: c = ServerProxy('http://localhost:15000', allow_none=True)

    In [3]: c.set("foo", "bar")

    In [4]: c.set("spam", [1,2,3])

    In [9]: c.keys()
    Out[9]: ['foo', 'spam']

    In [10]: c.get('spam')
    Out[10]: [1, 2, 3]

"""

from xmlrpc.server import SimpleXMLRPCServer


class KeyValueServer(object):
    # the methods what the rpc server divide
    _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']

    # init the server
    def __init__(self, address):
        self._data = {}
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods_:
            self._serv.register_function(getattr(self, name))

    # return the value for the key
    def get(self, name):
        return self._data[name]

    # set the new value for the key
    def set(self, name, value):
        self._data[name] = value

    # delete the key and value
    def delete(self, name):
        del self._data[name]

    # check if exists the key.
    def exists(self, name):
        return name in self._data

    # return the all keys
    def keys(self):
        return list(self._data)

    # make a request handled in a time until it shutdown
    def server_forever(self):
        self._serv.serve_forever()


if __name__ == '__main__':
    print("The server is begin listening at port {p}".format(p=15000))
    kvserv = KeyValueServer(("", 15000))
    kvserv.server_forever()
