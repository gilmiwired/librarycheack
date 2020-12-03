<?php
//こちら受信側→サーバ側に置いておく
    $bin = file_get_contents("php://input");//受信したモノを取り出し
    file_put_contents('./img.jpg',$bin);//同じディレクトリに『img.jpg』というファイル名で保存する
?>
