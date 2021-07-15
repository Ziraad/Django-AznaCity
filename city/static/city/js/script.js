var slide = document.getElementsByClassName('slide');
var dot = document.getElementsByClassName('dot');
var prev = document.querySelector('.prev');
var next = document.querySelector('.next');
var n = 0;
var i;
var open = document.getElementById('open-continue')
var close = document.getElementById("continue")
var desc = document.getElementById("category-item-des")

open.addEventListener('click', () =>{
    if (close.classList.contains('hidden')){
        close.classList.remove('hidden');
    }else{
        close.classList.add('hidden');
    }
})

// Start Fixed Navbar----------------------------------------------------
// var fixmeTop = $('.navbar').offset().top;       // get initial position of the element
// //
// $(window).scroll(function () {                  // assign scroll event listener
//
//     var currentScroll = $(window).scrollTop(); // get current position
//
//     if (currentScroll > fixmeTop) {           // apply position: fixed if you
//         $('.navbar').css({                      // scroll to that element or below it
//             position: 'fixed',
//             top: '0',
//             left: '0',
//             right: '0',
//             zIndex: '100',
//             backgroundColor: '#0099ff'
//
//         });
//         // $('.navbar').css({                      // scroll to that element or below it
//         //     marginTop: '10px',
//         // });
//         // $('.signing').css({                      // scroll to that element or below it
//         //     marginTop: '20px',
//         // });
//         // $('.container-search-bar').css({                      // scroll to that element or below it
//         //     bottom: '-10px',
//         // });
//     } else {                                   // apply position: static
//         $('.navbar').css({                      // if you scroll above it
//             position: 'static',
//         });
//         // $('.navbar').css({                      // scroll to that element or below it
//         //     marginTop: '10px',
//         // });
//         // $('.container-search-bar').css({                      // scroll to that element or below it
//         //     marginTop: '0',
//         // });
//         // $('.signing').css({                      // scroll to that element or below it
//         //     marginTop: '40px',
//         // });
//     }
//
// });

// End Fixed Navbar-----------------------------------------------------
var swiper2 = new Swiper('.swiper-tourism', {

    breakpoints: {
        480: {
            slidesPerView: 1
        },
        640: {
            slidesPerView: 2,
            spaceBetween: 30
        },
        992: {
            slidesPerView: 3,
            spaceBetween: 15
        },
        1200: {
            slidesPerView: 3,
            spaceBetween: 10
        },
        1600: {
            slidesPerView: 4,
            spaceBetween: 10
        },
    },
    // slidesPerView: 4,
    // spaceBetween: 5,
    // // slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    keyboard: true,
    navigation: {
        nextEl: '.btn-next-tourism',
        prevEl: '.btn-prev-tourism',
    },
});

var swiper3 = new Swiper('.swiper-hotel', {

    breakpoints: {
        480: {
            slidesPerView: 1
        },
        640: {
            slidesPerView: 2,
            spaceBetween: 30
        },
        992: {
            slidesPerView: 3,
            spaceBetween: 15
        },
        1200: {
            slidesPerView: 3,
            spaceBetween: 10
        },
        1600: {
            slidesPerView: 4,
            spaceBetween: 10
        },
    },
    // slidesPerView: 4,
    // spaceBetween: 5,
    // // slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    keyboard: true,
    navigation: {
        nextEl: '.btn-next-hotel',
        prevEl: '.btn-prev-hotel',
    },
});

var swiper4 = new Swiper('.swiper-soghat', {

    breakpoints: {
        480: {
            slidesPerView: 1
        },
        640: {
            slidesPerView: 2,
            spaceBetween: 30
        },
        992: {
            slidesPerView: 3,
            spaceBetween: 15
        },
        1200: {
            slidesPerView: 3,
            spaceBetween: 10
        },
        1600: {
            slidesPerView: 4,
            spaceBetween: 10
        },
    },
    // slidesPerView: 4,
    // spaceBetween: 5,
    // // slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    keyboard: true,
    navigation: {
        nextEl: '.btn-next-soghat',
        prevEl: '.btn-prev-soghat',
    },
});

var swiper5 = new Swiper('.swiper-factory', {

    breakpoints: {
        480: {
            slidesPerView: 1
        },
        640: {
            slidesPerView: 2,
            spaceBetween: 30
        },
        992: {
            slidesPerView: 3,
            spaceBetween: 15
        },
        1200: {
            slidesPerView: 3,
            spaceBetween: 10
        },
        1600: {
            slidesPerView: 4,
            spaceBetween: 10
        },
    },
    // slidesPerView: 4,
    // spaceBetween: 5,
    // // slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    keyboard: true,
    navigation: {
        nextEl: '.btn-next-factory',
        prevEl: '.btn-prev-factory',
    },
});
// swiper-slider---------------------------------------------------------
var swiper = new Swiper('.swiper-first-slide', {
    slidesPerView: 1,
    spaceBetween: 0,
    loop: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,

    },
    keyboard: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});



// var appendNumber = 4;
// var prependNumber = 1;
// var swiper = new Swiper('.swiper-container', {
//   slidesPerView: 3,
//   centeredSlides: true,
//   spaceBetween: 30,
//   pagination: {
//     el: '.swiper-pagination',
//     clickable: true,
//   },
//   navigation: {
//     nextEl: '.swiper-button-next',
//     prevEl: '.swiper-button-prev',
//   },
// });
// document.querySelector('.prepend-2-slides').addEventListener('click', function (e) {
//   e.preventDefault();
//   swiper.prependSlide([
//     '<div class="swiper-slide">Slide ' + (--prependNumber) + '</div>',
//     '<div class="swiper-slide">Slide ' + (--prependNumber) + '</div>'
//   ]);
// });
// document.querySelector('.prepend-slide').addEventListener('click', function (e) {
//   e.preventDefault();
//   swiper.prependSlide('<div class="swiper-slide">Slide ' + (--prependNumber) + '</div>');
// });
// document.querySelector('.append-slide').addEventListener('click', function (e) {
//   e.preventDefault();
//   swiper.appendSlide('<div class="swiper-slide">Slide ' + (++appendNumber) + '</div>');
// });
// document.querySelector('.append-2-slides').addEventListener('click', function (e) {
//   e.preventDefault();
//   swiper.appendSlide([
//     '<div class="swiper-slide">Slide ' + (++appendNumber) + '</div>',
//     '<div class="swiper-slide">Slide ' + (++appendNumber) + '</div>'
//   ]);
// });
// swiper-slider ------------------------------------------------


function change_name() {
    if (open.innerText === 'ادامه ...') {
        open.innerText = 'بستن';
    } else {
        open.innerText = 'ادامه ...';
    }
}

function disno() {
    for (i = 0; i < slide.length; i++) {
        slide[i].style.display = 'none';
    }
}

function no_active() {
    for (i = 0; i < dot.length; i++) {
        dot[i].classList.remove('active');
    }
}

next.addEventListener('click', function (e) {
    e.preventDefault();
    n++;
    if (n > slide.length - 1) {
        n = 0;
    }
    disno();
    no_active();
    slide[n].style.display = 'block';
    dot[n].classList.add('active');
})

prev.addEventListener('click', function (e) {
    e.preventDefault();
    n--;
    if (n < 0) {
        n = slide.length - 1;
    }
    disno();
    no_active();
    slide[n].style.display = 'block';
    dot[n].classList.add('active');
})

setInterval(function () {
    n++;
    if (n > slide.length - 1) {
        n = 0;
    }
    disno();
    no_active();
    slide[n].style.display = 'block';
    dot[n].classList.add('active');
}, 10000)

