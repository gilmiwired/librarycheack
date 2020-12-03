import requests
#こちら送信側→ローカルに置く
with open("a.jpg", "rb") as f:#画像をopen(読み込みみたいな？)する
    #url='https://profile-counter.glitch.me/librarycheck/pic_save.php'#送り先
	url='https://ibkosen-librarycondition.netlify.app/img/pic_save.php'
	r = requests.post(url, f.read())#送信
