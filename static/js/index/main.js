document.addEventListener("DOMContentLoaded", function () {
    var eventCalllback = function (e) {
        var el = e.target,
        clearVal = el.dataset.phoneClear,
        pattern = el.dataset.phonePattern,
        matrix_def = "+7(___) ___-__-__",
        matrix = pattern ? pattern : matrix_def,
        i = 0,
        def = matrix.replace(/\D/g, ""),
        val = e.target.value.replace(/\D/g, "");
        if (clearVal !== 'false' && e.type === 'blur') {
            if (val.length < matrix.match(/([\_\d])/g).length) {
                e.target.value = '';
                return;
            }
        }
        if (def.length >= val.length) val = def;
        e.target.value = matrix.replace(/./g, function (a) {
            return /[_\d]/.test(a) && i < val.length ? val.charAt(i++) : i >= val.length ? "" : a
        });
    }
    var phone_inputs = document.querySelectorAll('[data-phone-pattern]');
    for (let elem of phone_inputs) {
        for (let ev of ['input', 'blur', 'focus']) {
            elem.addEventListener(ev, eventCalllback);
        }
    }
});


const setReplacer = (target, expression) => {
    target.addEventListener('input', () => {
      const parsedValue = target.value.replace(expression, '');
      
      if (parsedValue !== target.value) {
        target.value = parsedValue;
      }
    });
};


setReplacer(document.querySelector('.footer__input--name'), /[^A-Za-zА-Яа-я\s]/g);


const menuBtn = document.querySelector('.menu__btn');
const headerPopup = document.querySelector('.header__popup');
const headerPopupLink = document.querySelectorAll('.header__popup-link');

menuBtn.addEventListener('click', ()=>{
    headerPopup.classList.toggle('header__popup-open');
});

headerPopupLink.forEach((btn) => {
    btn.addEventListener('click', ()=>{
        headerPopup.classList.remove('header__popup-open');
    });
});

const workSwiper = new Swiper('.work__swiper', {
    direction: 'horizontal',
    loop: false,
    spaceBetween: 35,
  
    pagination: {
      el: '.work__pagination',
      clickable: true,
    },
  
  });

const warehouseSwiper = new Swiper('.warehouse__swiper', {
    direction: 'horizontal',
    loop: true,
    spaceBetween: 35,
    
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
  
  });


const priceApplicationBtn = document.querySelector('.price-application__btn');
const pricePopup = document.querySelector('.price-popup');
const priceExitBtn = document.querySelector('.price-exit__btn');
const pricePopupWrapper = document.querySelector('.price__popup-wrapper');
const header = document.querySelector('.header');
const warehouse = document.querySelector('.warehouse');
const work = document.querySelector('.work');
const footer = document.querySelector('.footer');

priceApplicationBtn.addEventListener('click', ()=>{
    pricePopup.classList.add('price-popup-open');
    pricePopupWrapper.classList.add('price-popup-wrapper-open');
    header.style.position = 'static';
    work.style.display = 'none';
    warehouse.style.display = 'none';
    footer.style.display = 'none';
});

priceExitBtn.addEventListener('click', ()=>{
    pricePopup.classList.remove('price-popup-open');
    pricePopupWrapper.classList.remove('price-popup-wrapper-open');
    header.style.position ='sticky';
    work.style.display = 'block';
    warehouse.style.display = 'block';
    footer.style.display = 'block';
});
