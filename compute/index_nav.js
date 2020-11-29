var nav = document.getElementById('nav');
var navTop = nav.offsetTop;

window.onscroll = function () { myScrollFunction() };

function myScrollFunction() {
var res = navTop - document.documentElement.scrollTop;
    if (res > 0) {
        nav.setAttribute('style', 'top:' + res + 'px');
    } else {
        nav.setAttribute('style', 'top:0px')
    }
}
