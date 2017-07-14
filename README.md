# auto_tweet_bot
自動でツイートしてくれます。

注意点
raspbianでのみ動作確認
ubuntuやdebianでも動作すると思います。

$ sudo apt-get install oauth2

をコマンドラインで実行しoarth2のライブラリをインストールしておいて下さい。

dev.twitter.com
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

