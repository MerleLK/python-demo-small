# coding=utf-8

# this is a simple demo to put something by http put

import httplib2
from datetime import datetime
import simplejson

# a simple json data
data = {'header0':[{'key1':'value1', 'key2':'value2'}]}
json_data = simplejson.dumps(data)

now_date = datetime.now()  # 当前时间

# build a dest url
URL = 'http://127.0.0.1:10000'

# get a Http object
h = httplib2.Http()

resp, content = h.request(URL,
        'PUT',
        json_data,
        headers={'ContentType':'application/json', 
                'Host':'192.168.1.105'
            }
        )

