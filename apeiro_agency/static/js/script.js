$(function($) {
    //banner part 
    $('#banner_full').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 4000,
        arrows: true,
        dots: false,
        fade: true,
        nextArrow: '<i class="fas fa-chevron-right next_arrow"></i>',
        prevArrow: '<i class="fas fa-chevron-left prev_arrow"></i>',
    });

    // navfix
    // WARN: This crashes scrolling window
    // let navfix = $('.main_menu').offset().top;

    // $(window).scroll(function () {
    //     let scrolling = $(this).scrollTop();

    //     if (scrolling > navfix) {
    //         $('.main_menu').addClass('menufix');
    //     } else {
    //         $('.main_menu').removeClass('menufix');
    //     }
    // })
    $(function() {
        $('#easy-filter-wrap').easyFilter();
    });

    // your identity part
    $(".expand_button").click(function() {
        $(".expand_area").slideToggle();
    });


    // gallary part
    $('.galvan').venobox();
})
