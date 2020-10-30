 gen=0;
var zai=0;
var no=0;
var kon=0;
var zatu=0;
var jou=0;
var kyou=0;

function gen() {
    location.href = 'index.html';
    gen += 1;
    alert("uuuu");
}

function zai() {
    if(gen == 3) {
        zai += 1;
    }
}

function no() {
    if(kyou == 9) {
        true();
    }
}

function kon() {
    if(zai == 1) {
        kon += 1;
    }
}

function zatu() {
    if(kon == 4) {
        zatu += 1;
    }
}

function jou() {
    if(zatu == 1){
        jou += 1;
    }
}

function kyou() {
    if(jou == 5){
        kyou += 1;
    }
}

function true() {
    alert("おめでとう！");
}
