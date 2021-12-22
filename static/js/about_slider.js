var slideIndex1 = 1;
showSlides(slideIndex1);

// Next/previous controls
function nextSlides(n) {
  showSlides((slideIndex1 += n));
}

// Thumbnail image controls
function activeSlide(n) {
  showSlides((slideIndex1 = n));
}

function showSlides(n) {
  var index;
  var slides = document.getElementsByClassName("carousel");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {
    slideIndex1 = 1;
  }
  if (n < 1) {
    slideIndex1 = slides.length;
  }
  for (index = 0; index < slides.length; index++) {
    slides[index].style.display = "none";
  }
  for (index = 0; index < dots.length; index++) {
    dots[index].className = dots[index].className.replace(" active", "");
  }
  slides[slideIndex1 - 1].style.display = "block";
  dots[slideIndex1 - 1].className += " active";
}
