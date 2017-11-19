"""
    This is a demo for operate data use the elastic search.
"""

import elasticsearch
import codecs


class ES:

    @classmethod
    def connect_server(cls):
        es = elasticsearch.Elasticsearch()
        return es

    def put_data(self):
        es = ES.connect_server()
        print("begin insert the data")
        f = codecs.open("test_json.json", "r", "utf8")
        index = 'sport'
        doc_type = 'nba'
        for line in f.readlines():
            es.index(index=index, doc_type=doc_type, body=line)

        print("insert success")

    def es_query(self, domain, doc_type=None, body=None):
        es = ES.connect_server()
        if domain is None:
            return
        if doc_type is None:
            res = es.search(index=domain)
        elif doc_type and body is None:
            res = es.search(index=domain, doc_type=doc_type)
        else:
            res = es.search(index=domain, doc_type=doc_type, body=body)

        for hit in res['hits']['hits']:
            print(hit)


if __name__ == '__main__':
    my_es = ES()
    # my_es.put_data()
    inx = 'sport'
    doc = 'nba'
    body = {
        "query": {
            # 简单检索
            # "match_phrase": {
            #     "created_time": "2017年11月16日15:06",
            # }
            # 多字段检索
            "bool": {
                "should": [
                    {"match": {"title": "科比"}},
                    {"match": {"source": "新浪体育"}},
                    {"match": {"keywords": "湖人"}}
                ]
            }
        }
    }
    my_es.es_query(inx, doc, body)
