document.onkeydown = function(e) {
    if (!e) e = window.event;
    var keynum = e.keyCode ? e.keyCode : e.which; // IE vs others
    switch (keynum) {
        case 37:
            var link = document.getElementById('previous-card');
            link.setAttribute('class', 'active');
            location.href = link.getAttribute('href');
            return false;
        case 39:
            var link = document.getElementById('next-card');
            link.setAttribute('class', 'active');
            location.href = link.getAttribute('href');
            return false;
    }
};
