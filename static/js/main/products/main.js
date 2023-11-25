const cabinetBtn = document.querySelector('.cabinet__btn');
const cabinetPopup = document.querySelector('.cabinet__popup');

cabinetBtn.addEventListener('click', ()=>{
    cabinetPopup.classList.toggle('cabinet__popup-open');
});