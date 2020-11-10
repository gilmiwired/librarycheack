//WebSocket接続
var connection = new WebSocket("ws://localhost:8000/ws/");

//接続通知
connection.onopen = function(event) {
	document.getElementById( "eventType" ).value = "通信接続イベント受信";
	document.getElementById( "dispMsg" ).value = event.data;
};

//エラー発生
connection.onerror = function(error) {
	document.getElementById( "eventType" ).value = "エラー発生イベント受信";
	document.getElementById( "dispMsg" ).value = error.data;
};

//メッセージ受信
connection.onmessage = function(event) {
	document.getElementById( "eventType" ).value = "メッセージ受信";
	document.getElementById( "dispMsg" ).value = event.data;
};

//切断
connection.onclose = function() {
	document.getElementById( "eventType" ).value = "通信切断イベント受信";
	document.getElementById( "dispMsg" ).value = "";
};
