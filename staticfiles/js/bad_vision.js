const toggleButton = document.getElementById('toggle-vision');
const body = document.body;

toggleButton.addEventListener('click', () => {
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


var currentTextSizeClass = "";
function changeTextSize(sizeClass) {
    if (currentTextSizeClass != ""){
        body.classList.remove(currentTextSizeClass);
    }
    body.classList.add(sizeClass);
    currentTextSizeClass = sizeClass;
}