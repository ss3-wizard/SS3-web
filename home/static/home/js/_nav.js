const menus = document.getElementById("menus");
menus.onmouseenter = function () {
    document.getElementById("menu-sub").style.height = "250px";
    document.getElementById("header").style.height = "0px";
};
menus.onmouseleave = function () {
    document.getElementById("menu-sub").style.height = "0px";
    document.getElementById("header").style.height = "250px";
};