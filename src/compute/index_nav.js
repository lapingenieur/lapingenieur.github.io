// index_nav.js - v0.3.1 global

var locked = document.getElementById('locked');
var lockedTop = locked.offsetTop;

window.onscroll = function () { myScrollFunctionB() };

function myScrollFunctionB() {
    var res = lockedTop - document.documentElement.scrollTop;
    if (res > 0) {
        locked.setAttribute('style', 'top:' + res + 'px');
    } else {
        locked.setAttribute('style', 'top:0px')
    }
}
