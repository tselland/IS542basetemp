/**
 * Created by travisselland on 2/9/15.
 */

$(function() {

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

    //left menu float stays with them regardless of how far down they scroll
    $(window).scroll(function (event) {
        if ($(this).scrollTop() > 55) {
          $('.menu-float').addClass('fixed');
        } else {
          $('.menu-float').removeClass('fixed');
        }
    });
});