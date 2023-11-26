const cabinetBtn = document.querySelector('.cabinet__btn');
const cabinetPopup = document.querySelector('.cabinet__popup');
const cabinetPopupWrapper = document.querySelector('.cabinet__popup-wrapper');
const productAddWrapper = document.querySelector('.product-add__wrapper');
const productBtn = document.querySelector('.product__btn');
const productAddContainer = document.querySelector('.product-add__container');
const backBtn = document.querySelector('.back-btn');
const backBtnCabinet = document.querySelector('.back-btn-cabinet');


cabinetBtn.addEventListener('click', ()=>{
    cabinetPopup.classList.add('cabinet__popup-open');
    // cabinetPopupWrapper.classList.add('cabinet__overlay');
});

backBtnCabinet.addEventListener('click', ()=>{
    cabinetPopup.classList.remove('cabinet__popup-open');
    cabinetPopupWrapper.classList.remove('cabinet__overlay');
})

productBtn.addEventListener('click', ()=>{
    productAddWrapper.classList.add('product-add__overlay');
    productAddContainer.classList.add('product-add__show');
});

backBtn.addEventListener('click', ()=>{
    productAddWrapper.classList.remove('product-add__overlay');
    productAddContainer.classList.remove('product-add__show');
});

