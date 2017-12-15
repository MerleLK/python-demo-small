# coding=utf-8

import os
import sys
import json
import time
import base64
import requests
from bs4 import BeautifulSoup
from Crypto.Cipher import AES
from spider_setting import USERNAME, PW, SECONDS, BEGIN, END
from db_demo import db

reload(sys)
sys.setdefaultencoding('utf-8')


# follow by https://www.zhihu.com/question/31677442
DEFAULT_HEADER = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cookie': 'appver=2.0.2;',
        'Host': "music.163.com",
        'Origin': "http://music.163.com",
        'Referer': "http://music.163.com/",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

BASE_URL = 'http://music.163.com'

session = requests.session()
session.headers.update(DEFAULT_HEADER)


def get_page(page_index):
    page_url = 'http://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset=' + page_index
    soup = BeautifulSoup(session.get(page_url).content, "html.parser")
    song_list = soup.findAll('a', attrs={'class': 'tit f-thide s-fc0'})
    for i in song_list:
        print(i['href'])
        get_play_list(i['href'])


def get_play_list(play_list_id):
    play_list_url = BASE_URL + play_list_id
    soup = BeautifulSoup(session.get(play_list_url).content, "html.parser")
    song_list = soup.find('ul', attrs={'class': 'f-hide'})
    for i in song_list.findAll('li'):
        start_index = i.find('a')['href']
        song_id = start_index.split('=')[1]
        read_ever(song_id)  # 得到一万评论以上的音乐


def aes_encrypt(text, sec_key):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(sec_key, 2, '0102030405060708')
    cipher_text = encryptor.encrypt(text)
    cipher_text = base64.b64encode(cipher_text)
    return cipher_text


def rsa_encrypt(text, public_key, modulus):
    text = text[::-1]
    rs = int(text.encode('hex'), 16) ** int(public_key, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


def create_secret_key(size):
    return (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(size))))[0:16]


def read_ever(song_id):
    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(song_id) + '/?csrf_token='
    text = {'username': USERNAME, 'password': PW, 'rememberLogin': 'true'}
    modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17' \
              'a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af' \
              '6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b' \
              '8e289dc6935b3ece0462db0a22b8e7'

    nonce = '0CoJUm6Qyw8W8jud'
    public_key = '010001'
    text = json.dumps(text)
    sec_key = create_secret_key(16)
    enc_text = aes_encrypt(aes_encrypt(text, nonce), sec_key)
    enc_sec_key = rsa_encrypt(sec_key, public_key, modulus)
    data = {
        'params': enc_text,
        'encSecKey': enc_sec_key
    }
    req = requests.post(url, headers=DEFAULT_HEADER, data=data)
    try:
        total = req.json()['total']
    except KeyError:
        print("may be chatting...")
        print(req.json())
        sys.exit()
    if int(total) > 10000:
        get_song_info(song_id, total)
    else:
        pass
    time.sleep(SECONDS)


def get_song_info(song_id, total):
    url = BASE_URL + '/song?id=' + str(song_id)
    url.decode('utf-8')
    soup = BeautifulSoup(session.get(url).content, "html.parser")
    content_list = soup.title.string.split(' - ')
    song_name = content_list[0]
    song_singer = content_list[1]
    if db.insert_data(song_name.encode('utf-8'), song_id, song_singer.encode('utf-8'), total):
        print("saved one song. {name}".format(name=song_name.encode('utf-8')))
    else:
        print("has error.................")


if __name__ == '__main__':
    # 区间 1-1297
    for index in xrange(BEGIN, END):
        get_page(str(index))
