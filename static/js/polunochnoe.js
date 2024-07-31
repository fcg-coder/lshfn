

// Определите массив изображений
var images = [
    "images/polunochnoe/1.webp",
    "images/polunochnoe/2.webp",
    "images/polunochnoe/3.webp",
    "images/polunochnoe/4.webp",
    "images/polunochnoe/5.webp",
    "images/polunochnoe/6.webp",
    "images/polunochnoe/7.webp",
    "images/polunochnoe/8.webp",
    "images/polunochnoe/9.webp",
    "images/polunochnoe/10.webp",
    "images/polunochnoe/11.webp"
];

// Выберите случайное изображение из массива
var randomImage = images[Math.floor(Math.random() * images.length)];

// Установите выбранное изображение в качестве фона
document.body.style.backgroundImage = "url('" + randomImage + "')";






const picture1 = document.querySelector('.picture1');
const picture2 = document.querySelector('.picture2');
const picture3 = document.querySelector('.picture3');
const picture4 = document.querySelector('.picture4');
const picture5 = document.querySelector('.picture5');
const picture6 = document.querySelector('.picture6');
const picture7 = document.querySelector('.picture7');
const picture8 = document.querySelector('.picture8');
const picture9 = document.querySelector('.picture9');
const picture10 = document.querySelector('.picture10');
const picture11 = document.querySelector('.picture11')

// Функция для генерации случайных чисел от min до max
function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

picture1.addEventListener('mouseover', () => {
    // Генерируем случайные координаты для перемещения картинки
    const x = getRandomNumber(-50, 50) + 'px';
    const y = getRandomNumber(-50, 50) + 'px';

    // Устанавливаем значения переменных --x и --y для перемещения картинки
    picture1.style.setProperty('--x', x);
    picture1.style.setProperty('--y', y);

});


picture2.addEventListener('mouseover', () => {
    // Генерируем случайные координаты для перемещения картинки
    const x = getRandomNumber(-50, 50) + 'px';
    const y = getRandomNumber(-50, 50) + 'px';

    // Устанавливаем значения переменных --x и --y для перемещения картинки
    picture2.style.setProperty('--x', x);
    picture2.style.setProperty('--y', y);


});


picture3.addEventListener('mouseover', () => {
    // Генерируем случайные координаты для перемещения картинки
    const x = getRandomNumber(-50, 50) + 'px';
    const y = getRandomNumber(-50, 50) + 'px';

    // Устанавливаем значения переменных --x и --y для перемещения картинки
    picture3.style.setProperty('--x', x);
    picture3.style.setProperty('--y', y);

});


picture4.addEventListener('mouseover', () => {
    // Генерируем случайные координаты для перемещения картинки
    const x = getRandomNumber(-50, 50) + 'px';
    const y = getRandomNumber(-50, 50) + 'px';

    // Устанавливаем значения переменных --x и --y для перемещения картинки
    picture4.style.setProperty('--x', x);
    picture4.style.setProperty('--y', y);


});



picture5.addEventListener('mouseover', () => {
    // Генерируем случайные координаты для перемещения картинки
    const x = getRandomNumber(-50, 50) + 'px';
    const y = getRandomNumber(-50, 50) + 'px';

    // Устанавливаем значения переменных --x и --y для перемещения картинки
    picture5.style.setProperty('--x', x);
    picture5.style.setProperty('--y', y);

});


picture6.addEventListener('mouseover', () => {
    // Генерируем случайные координаты для перемещения картинки
    const x = getRandomNumber(-50, 50) + 'px';
    const y = getRandomNumber(-50, 50) + 'px';

    // Устанавливаем значения переменных --x и --y для перемещения картинки
    picture6.style.setProperty('--x', x);
    picture6.style.setProperty('--y', y);


});


picture7.addEventListener('mouseover', () => {
    // Генерируем случайные координаты для перемещения картинки
    const x = getRandomNumber(-50, 50) + 'px';
    const y = getRandomNumber(-50, 50) + 'px';

    // Устанавливаем значения переменных --x и --y для перемещения картинки
    picture7.style.setProperty('--x', x);
    picture7.style.setProperty('--y', y);

});


picture8.addEventListener('mouseover', () => {
    // Генерируем случайные координаты для перемещения картинки
    const x = getRandomNumber(-50, 50) + 'px';
    const y = getRandomNumber(-50, 50) + 'px';

    // Устанавливаем значения переменных --x и --y для перемещения картинки
    picture8.style.setProperty('--x', x);
    picture8.style.setProperty('--y', y);


});

picture9.addEventListener('mouseover', () => {
    // Генерируем случайные координаты для перемещения картинки
    const x = getRandomNumber(-50, 50) + 'px';
    const y = getRandomNumber(-50, 50) + 'px';

    // Устанавливаем значения переменных --x и --y для перемещения картинки
    picture9.style.setProperty('--x', x);
    picture9.style.setProperty('--y', y);


});

picture10.addEventListener('mouseover', () => {
    // Генерируем случайные координаты для перемещения картинки
    const x = getRandomNumber(-50, 50) + 'px';
    const y = getRandomNumber(-50, 50) + 'px';

    // Устанавливаем значения переменных --x и --y для перемещения картинки
    picture10.style.setProperty('--x', x);
    picture10.style.setProperty('--y', y);


});

picture11.addEventListener('mouseover', () => {
    // Генерируем случайные координаты для перемещения картинки
    const x = getRandomNumber(-50, 50) + 'px';
    const y = getRandomNumber(-50, 50) + 'px';

    // Устанавливаем значения переменных --x и --y для перемещения картинки
    picture11.style.setProperty('--x', x);
    picture11.style.setProperty('--y', y);


});




  // Генерируем случайные значения top и left относительно окна браузера
  var randomTop = Math.floor(Math.random() * window.innerHeight);
  var randomLeft = Math.floor(Math.random() * window.innerWidth);
  
   // Присваиваем новые значения свойствам top и left элемента
   picture1.style.top = randomTop + "px";
   picture1.style.left = randomLeft + "px"



  // Генерируем случайные значения top и left относительно окна браузера
  var randomTop = Math.floor(Math.random() * window.innerHeight);
  var randomLeft = Math.floor(Math.random() * window.innerWidth);
  
   // Присваиваем новые значения свойствам top и left элемента
   picture2.style.top = randomTop + "px";
   picture2.style.left = randomLeft + "px"


  // Генерируем случайные значения top и left относительно окна браузера
  var randomTop = Math.floor(Math.random() * window.innerHeight);
  var randomLeft = Math.floor(Math.random() * window.innerWidth);
  
   // Присваиваем новые значения свойствам top и left элемента
   picture3.style.top = randomTop + "px";
   picture3.style.left = randomLeft + "px"

  // Генерируем случайные значения top и left относительно окна браузера
  var randomTop = Math.floor(Math.random() * window.innerHeight);
  var randomLeft = Math.floor(Math.random() * window.innerWidth);
  
   // Присваиваем новые значения свойствам top и left элемента
   picture4.style.top = randomTop + "px";
   picture4.style.left = randomLeft + "px"

  // Генерируем случайные значения top и left относительно окна браузера
  var randomTop = Math.floor(Math.random() * window.innerHeight);
  var randomLeft = Math.floor(Math.random() * window.innerWidth);
  
   // Присваиваем новые значения свойствам top и left элемента
   picture5.style.top = randomTop + "px";
   picture5.style.left = randomLeft + "px"


     // Генерируем случайные значения top и left относительно окна браузера
  var randomTop = Math.floor(Math.random() * window.innerHeight);
  var randomLeft = Math.floor(Math.random() * window.innerWidth);
  
   // Присваиваем новые значения свойствам top и left элемента
   picture6.style.top = randomTop + "px";
   picture6.style.left = randomLeft + "px"


  // Генерируем случайные значения top и left относительно окна браузера
  var randomTop = Math.floor(Math.random() * window.innerHeight);
  var randomLeft = Math.floor(Math.random() * window.innerWidth);
  
   // Присваиваем новые значения свойствам top и left элемента
   picture7.style.top = randomTop + "px";
   picture7.style.left = randomLeft + "px"


  // Генерируем случайные значения top и left относительно окна браузера
  var randomTop = Math.floor(Math.random() * window.innerHeight);
  var randomLeft = Math.floor(Math.random() * window.innerWidth);
  
   // Присваиваем новые значения свойствам top и left элемента
   picture8.style.top = randomTop + "px";
   picture8.style.left = randomLeft + "px"

  // Генерируем случайные значения top и left относительно окна браузера
  var randomTop = Math.floor(Math.random() * window.innerHeight);
  var randomLeft = Math.floor(Math.random() * window.innerWidth);
  
   // Присваиваем новые значения свойствам top и left элемента
   picture9.style.top = randomTop + "px";
   picture9.style.left = randomLeft + "px"


  // Генерируем случайные значения top и left относительно окна браузера
  var randomTop = Math.floor(Math.random() * window.innerHeight);
  var randomLeft = Math.floor(Math.random() * window.innerWidth);
  
   // Присваиваем новые значения свойствам top и left элемента
   picture10.style.top = randomTop + "px";
   picture10.style.left = randomLeft + "px"


     // Генерируем случайные значения top и left относительно окна браузера
  var randomTop = Math.floor(Math.random() * window.innerHeight);
  var randomLeft = Math.floor(Math.random() * window.innerWidth);
  
   // Присваиваем новые значения свойствам top и left элемента
   picture11.style.top = randomTop + "px";
   picture11.style.left = randomLeft + "px"






   