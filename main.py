# import itchat

# itchat.auto_login()

# itchat.send_msg('Hello, filehelper', toUserName='nickrogerson')

# author = itchat.search_friends(nickName='Jake')[0]
# author.send(author)

# print(author)

# @itchat.get_msg
# def messages():
#     # equals to print(msg['FromUserName'])
#     print(msg['jake5480'])

# messages()


# At the moment, can only do this with a hot reload so ties down one worker for good
# Not sure how to do the QR authentication on a server / Redis
# Get Redis to create the qr code and email it me 
# - need to pretty much eliminate the QR regeneration code or find a non-qr code way of authenticating
# - and re-write the source code to email rather than pop it up on my laptop


import itchat, json, redis
from itchat.content import *

# r = redis.Redis(decode_responses=True)

@itchat.msg_register(TEXT, isGroupChat=True)
def print_msgs(text):
    r.set('wechat', text.text.encode().decode())
    print(json.dumps(text, indent=4))
    print(text.text.encode().decode())

itchat.auto_login(hotReload = True)
itchat.run()


# text = "\"\u5c3c\u514b: \u90a3\u4f60\u4e3a\u4ec0\u4e48\u624d\u51b3\u5b9a\u5f00\u59cb\u5b66\u4e60\uff1f\"\n- - - - - - - - - - - - - - -\n\u56e0\u4e3a\u6211\u662f\u4e3a\u4e86\u9ad8\u8003\u624d\u5b66\u4e60\u7684\u4f53\u80b2\uff0c\u73b0\u5728\u8003\u4e0a\u5927\u5b66\u4e86\uff0c\u6211\u6362\u4e86\u4e2a\u4e13\u4e1a"

# print(text.encode().decode())


Q_CLUSTER = {
    'redis': {
        'host': 'localhost',
        'port': 6379,
        'db': 0,
        'password': None,
        'socket_timeout': None,
        'charset': 'utf-8',
        'errors': 'strict',
        'unix_socket_path': None
    }
}


              
