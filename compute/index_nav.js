var menu = document.getElementById('menu');
var menuTop = menu.offsetTop;
var nav = document.getElementById('nav');
var navTop = nav.offsetTop;

window.onscroll = function () { myScrollFunction() };

function myScrollFunction() {
var res = menuTop - document.documentElement.scrollTop;
var navme = res + 32;
    if (res > 0) {
        menu.setAttribute('style', 'top:' + res + 'px');
        nav.setAttribute('style', 'top:' + navme + 'px');
    } else {
        menu.setAttribute('style', 'top:0px')
        nav.setAttribute('style', 'top:32px')
    }
}
