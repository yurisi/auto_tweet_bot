# -*- coding: utf-8 -*-


#使用上の注意点
'''
sudo apt-get install oauth2を予めコマンドラインで打っておいてください
動作確認環境 raspbian =　Debian
'''
import time
import oauth2 as oauth
from urllib import urlencode

#いずれもdev.twitter.comで取得したkeyを入力
# |
#\/
consumer_key="consumerkey"
consumer_secret="comsecret"
access_token_key="accesstokenkey"
access_token_secret="accesstokensecret"


client  = oauth.Client(
oauth.Consumer(key=consumer_key, secret=consumer_secret),
oauth.Token(access_token_key, access_token_secret)
)

while True:
    message=""#発言したいメッセージの追加
    message2=""#追加可能。
    message3=""
    #message4=""

#メッセージ1の投稿処理
    client.request(
    'https://t.co/xdz9ClfP96',
    'POST',
    urlencode({
    'status': message
    }),
     )

    time.sleep(3600.0)#秒単位で次のツイートを投稿する時間の設定
#メッセージ2の投稿処理
    client.request(
    'https://t.co/xdz9ClfP96',
    'POST',
    urlencode({
    'status': message2
    }),
    )

   time.sleep(3600.0)
    
#メッセージ3の投稿処理    
    client.request(
    'https://t.co/xdz9ClfP96',
    'POST',
    urlencode({
    'status': message3
    }),
    )
#もしmessage4のシャープを外し中にメッセージを代入したらここのシャープを消して実行できる状態にする
    #time.sleep(3600.0)

    #client.request(
    #'https://t.co/xdz9ClfP96',
    #'POST',
    #urlencode({
    #'status' : mesaage4
    #}),
    #)
