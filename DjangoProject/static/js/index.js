var bar = document.getElementById("scroll-proggress-bar");
window.addEventListener('scroll', function () {
    bar.style.width = (((document.documentElement.scrollTop || document.body.scrollTop) / window.scrollMaxY)*100) + "%"
});
// Next part of code
/*const startAnimation = (entries, observer) => {
  entries.forEach(entry => {
    entry.target.classList.toggle("title-anim", entry.isIntersecting);
  });
};

const observer = new IntersectionObserver(startAnimation);
const options = { root: null, rootMargin: '0px', threshold: 1 };

// const elements = document.querySelectorAll('.card');
const elements = document.getElementsByClassName("main-media-title");
[...elements].forEach(el => {
  observer.observe(el, options);
});*/
/*const elements = document.querySelectorAll('.card');
elements.forEach(el => {
  observer.observe(el, options);
});*/