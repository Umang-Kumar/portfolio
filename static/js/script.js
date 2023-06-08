$(document).on('click', function(event) {
  const target = $(event.target);
  const navCollapse = $('.navCollapseCol');

  // Check if the target is not within the hamburger menu or its toggle button
  if (!target.closest('.navCollapseCol').length && !target.closest('.navToggle').length) {
    // Close the menu if it is currently open
    if (navCollapse.hasClass('show')) {
      navCollapse.removeClass('show');
      $('body').removeClass('navToggleActive');
    }
  }
});

$('.navToggle').on('click', function (e) {
  e.preventDefault();
  const navCollapse = $('.navCollapseCol');

  // Toggle the menu visibility
  navCollapse.toggleClass('show');
  $('body').toggleClass('navToggleActive');
});

$(window).scroll(function(){
  if ($(this).scrollTop() > 10) {
    $('body').addClass('fixedHeader');
  } else {
    $('body').removeClass('fixedHeader');
  }
});


var swiper = new Swiper(".testimonialSwiper", {
  navigation: {
    nextEl: ".test-swiper-button-next",
    prevEl: ".test-swiper-button-prev",
  },
});


var swiper = new Swiper(".certificatesSlider", {
  slidesPerView: 1,
  spaceBetween: 16,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".cert-swiper-button-next",
    prevEl: ".cert-swiper-button-prev",
  },
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
    1024: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
  },
});

const toggleBtn = document.querySelector("#dark-mode-btn");

toggleBtn.addEventListener("click", function() {
  document.body.classList.toggle("dark-mode");
  if (document.body.classList.contains("dark-mode")) {
    localStorage.setItem("dark-mode", "on");
  } else {
    localStorage.setItem("dark-mode", "off");
  }
});

// Check if dark mode is enabled on page load
if (localStorage.getItem("dark-mode") === "on") {
  document.body.classList.add("dark-mode");
}
