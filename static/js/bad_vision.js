const body = document.body;

var currentTextSizeClass = "";
function changeTextSize(sizeClass) {
    if (currentTextSizeClass != ""){
        body.classList.remove(currentTextSizeClass);
    }
    body.classList.add(sizeClass);
    currentTextSizeClass = sizeClass;
}
var currentColorSchemeClass = "";
function changeColorScheme(colorSchemeClass) {
    if (currentColorSchemeClass != ""){
        body.classList.remove(currentColorSchemeClass);
    }
    body.classList.add(colorSchemeClass);
    currentColorSchemeClass = colorSchemeClass;
}

const toggleButton = document.getElementById('toggle-vision');
toggleButton.addEventListener('click', () => {
  if (currentTextSizeClass == "") {
      changeTextSize('text-size-100');
  }
  if (currentColorSchemeClass == "") {
    changeColorScheme('color-scheme-white');
  }
  if (body.classList.contains('bad-vision')) {
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
    body.classList.remove('bad-vision');
  } else {
    document.documentElement.setAttribute('data-theme', 'bad-vision');
    localStorage.setItem('theme', 'bad-vision');
    body.classList.add('bad-vision');
  }
});