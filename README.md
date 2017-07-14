# auto_tweet_bot
自動でツイートしてくれます。

注意点
raspbianでのみ動作確認
ubuntuやdebianでも動作すると思います。
twitter自体の機能で何時間か置かないと同じ投稿ができませんので気を付けてください

$ sudo apt-get install oauth2

をコマンドラインで実行しoarth2のライブラリをインストールしておいて下さい。

http://dev.twitter.com
からkey4種を取得しておいてください

使い方
１、
consumer_key=''
consumer_secret=''
access_token_key=''
access_token_secret''
にdev.twitter.comより取得したコードを記入してください

２、
message=''の部分に投稿したい文を入力してください

３、
time.sleep(3600.0)と書いてあるカッコに1秒単位で投稿したい時間を入力します
1時間→3600.0
10分→600.0
5時間→18000.0

４、
コマンドラインで
$ python3 auto_tweet_bot.py
と入力することで実行されます。

*message4を使いたいときは
#message4=''　→　message4='投稿したい文'
にして
一番最後の#time.sleep()から#)までの#ををすべて外す
この時にインデントは元々のままで変えないよう気をつけてください。

不明点はhttp://twitter.com/yurisi0212　へ



