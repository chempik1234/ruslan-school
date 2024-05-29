function footerf() {
    const
        footer = document.getElementName('footer'),
        susick = document.getElementById('main-nav');
    console.log(footer.clientHeight);
    console.log(susick.clientHeight);
    footer.style.marginTop = footer.clientHeight-susick.clientHeight + 30 + 'px';
}

window.addEventListener('load', footerf);
window.addEventListener('resize', footerf);