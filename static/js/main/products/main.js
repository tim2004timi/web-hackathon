const cabinetBtn = document.querySelector('.cabinet__btn');
const cabinetPopup = document.querySelector('.cabinet__popup');
const cabinetPopupWrapper = document.querySelector('.cabinet__popup-wrapper');
const productAddWrapper = document.querySelector('.product-add__wrapper');
const productBtn = document.querySelector('.product__btn');
const productAddContainer = document.querySelector('.product-add__container');
const backBtn = document.querySelector('.back-btn');
const backBtnCabinet = document.querySelector('.back-btn-cabinet');
const tableEl = document.querySelector('.table');
// const header = document.querySelector('.body');


cabinetBtn.addEventListener('click', ()=>{
    cabinetPopup.classList.add('cabinet__popup-open');
    tableEl.style.zIndex = '-1';
    productAddWrapper.classList.add('product-add__overlay');
    cabinetPopupWrapper.classList.add('product-add__overlay');
});

backBtnCabinet.addEventListener('click', ()=>{
    cabinetPopup.classList.remove('cabinet__popup-open');
    tableEl.style.zIndex = '1';
    productAddWrapper.classList.remove('product-add__overlay');
    cabinetPopupWrapper.classList.remove('product-add__overlay');
})

productBtn.addEventListener('click', ()=>{
    productAddWrapper.classList.add('product-add__overlay');
    productAddContainer.classList.add('product-add__show');
});

backBtn.addEventListener('click', ()=>{
    productAddWrapper.classList.remove('product-add__overlay');
    productAddContainer.classList.remove('product-add__show');
});

