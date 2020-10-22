var wSck= new WebSocket("echo.websocket.org");// WebSocketオブジェクト生成

wSck.onopen = function() {//ソケット接続時のアクション
	document.getElementById('show').innerHTML += "接続しました。" + "<br/>";
};

wSck.onmessage = function(e) {//メッセージを受け取ったときのアクション
	document.getElementById('show').innerHTML += e.data + "<br/>";
};

var sendMsg = function(val) {//メッセージを送信するときのアクション
	var line = document.getElementById('msg');//入力内容を取得
	wSck.send(line.value);//ソケットに送信
	line.value = "";//内容をクリア
};
