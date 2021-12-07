let companiesCardbtn = document.querySelector(".companies__card_btn")
let burger = document.querySelector('.burger')
let burgerContent = document.querySelector('.burger__content')


$('.companies__cards').slick({
    dots: true,
  infinite: false,
  speed: 300,
  slidesToShow: 3,
  slidesToScroll: 1,
  // arrows: false
  prevArrow: "<images src='../images/arrow_right.svg'>",
  nextArrow: "<images src='../images/arrow_left.svg'>"
});


burger.addEventListener('click', function () {
  console.log(burger);
  burger.classList.toggle('burger_active')
  burgerContent.classList.toggle('burger__content_active')

  console.log(burger);
  
})

