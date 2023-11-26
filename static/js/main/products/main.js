const cabinetBtn = document.querySelector('.cabinet__btn');
const cabinetPopup = document.querySelector('.cabinet__popup');
const cabinetPopupWrapper = document.querySelector('.cabinet__popup-wrapper');
const bodyEl = document.body;
const productAddWrapper = document.querySelector('.product-add__wrapper');
const productBtn = document.querySelector('.product__btn');
const productAddContainer = document.querySelector('.product-add__container');
const backBtn = document.querySelector('.back-btn');


cabinetBtn.addEventListener('click', (e)=>{
    // e.stopPropagation();
    cabinetPopup.classList.add('cabinet__popup-open');
    bodyEl.classList.add('cabinet__overlay');
    cabinetPopupWrapper.classList.add('cabinet__overlay');
});

document.addEventListener('click', (e)=>{
    const target = e.target;
    const itsCabinetPopupWrapper = target == cabinetPopupWrapper || cabinetPopupWrapper.contains(target);
    const itsCabinetBtn = target == cabinetBtn;
    const overlayIsActive = cabinetPopupWrapper.classList.contains("cabinet__overlay");

    if (!itsCabinetPopupWrapper && !itsCabinetBtn && overlayIsActive) {
        cabinetPopup.classList.remove('cabinet__popup-open');
        bodyEl.classList.remove('cabinet__overlay');
        cabinetPopupWrapper.classList.remove('cabinet__overlay');
    }
})

productBtn.addEventListener('click', ()=>{
    productAddWrapper.classList.add('product-add__overlay');
    productAddContainer.classList.add('product-add__show');
});

backBtn.addEventListener('click', ()=>{
    productAddWrapper.classList.remove('product-add__overlay');
    productAddContainer.classList.remove('product-add__show');
});

