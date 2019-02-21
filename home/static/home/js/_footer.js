window.onscroll = function () {
    const go_to_top = document.getElementById("go_to_top");
    if (document.documentElement.scrollTop <= 50) {
        go_to_top.style.display = "none"
    } else{
        go_to_top.style.display = "block"
    }
};

