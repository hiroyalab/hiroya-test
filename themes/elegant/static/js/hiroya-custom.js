const swiper = new Swiper(".swiper", {
    loop: true, // ループ
    speed: 100, // (デフォルトは300)
    slidesPerView: 1, // 一度に表示する枚数
    autoHeight: true, // 高さ自動調整
    // ページネーション
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    // 前後の矢印
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

// intense.min.jsより後にしないとダメ
var elements = document.querySelectorAll( '.fullscreen-image' );
Intense( elements );