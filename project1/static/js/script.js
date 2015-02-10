/**
 * Created by travisselland on 2/9/15.
 */

$(function() {

    var year = (new Date).getFullYear();

    $('.current-year').text(year);


  $("ul.tab-bar > li").click(function() {
    $(this).siblings('.tab-active').removeClass('tab-active');
    $(this).addClass('tab-active');
  });

    $('.notification > .fa').on('click', function(){
        $(this).parent().fadeOut();
    });

    $('li > .dropdown-toggle').on('click', function(){
       $(this).siblings('.dropdown-menu').fadeToggle();
    });

    var top = $('.menu-float').offset().top - parseFloat($('.menu-float').css('marginTop').replace(/auto/, 100));


    //tab bar stays with them regardless of how far down they scroll
    $(window).scroll(function (event) {
        if ($(this).scrollTop() >= top) {
          $('.menu-float').addClass('fixed');
        } else {
          $('.menu-float').removeClass('fixed');
        }
    });
});