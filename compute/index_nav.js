var locked = document.getElementById('locked');
var lockedTop = locked.offsetTop;

window.onscroll = function () { myScrollFunction() };

function myScrollFunction() {
var res = lockedTop - document.documentElement.scrollTop;
    if (res > 0) {
        locked.setAttribute('style', 'top:' + res + 'px');
    } else {
        locked.setAttribute('style', 'top:0px')
    }
}
