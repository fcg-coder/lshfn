
  function getRandomPosition(min, max) {
    return Math.random() * (max - min) + min;
  }


  



  function moveImage() {
    const images = document.querySelectorAll('.randGif');
    images.forEach(function(image) {
      const x = getRandomPosition(0, window.innerWidth - image.width);
      const y = getRandomPosition(0, window.innerHeight - image.height);

      image.style.left = `${x}px`;
      image.style.top = `${y}px`;
    });

    setTimeout(moveImage, 1000); // Повторить через 1 секунду
  }

  function opacityToTime() {
    const images = document.querySelectorAll('.randGif');
    images.forEach(function(image) {
      image.style.opacity = 0;
      setTimeout(function() {
        image.style.opacity = 1;
      }, Math.random()* 500000);
    });

    setTimeout(opacityToTime, 3000); // Повторить через 3 секунды
  }

  moveImage();
  opacityToTime();