const cabinetBtn = document.querySelector('.cabinet__btn');
const cabinetPopup = document.querySelector('.cabinet__popup');
const cabinetPopupWrapper = document.querySelector('.cabinet__popup-wrapper');
const backBtnCabinet = document.querySelector('.back-btn-cabinet');
const overlayContainer = document.querySelector('.overlay__container');
const card = document.querySelector('.card');


cabinetBtn.addEventListener('click', ()=>{
    cabinetPopup.classList.add('cabinet__popup-open');
    cabinetPopupWrapper.classList.add('overlay__container-on');
    card.style.zIndex = '-1';
    overlayContainer.classList.add('overlay__container-on');
});

backBtnCabinet.addEventListener('click', ()=>{
    cabinetPopup.classList.remove('cabinet__popup-open');
    cabinetPopupWrapper.classList.remove('overlay__container-on');
    card.style.zIndex = '1';
    overlayContainer.classList.remove('overlay__container-on');
})