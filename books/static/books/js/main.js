/**
 * Created by KANHU on 15-03-2017.
 */

$('ul.nav li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay().fadeIn();
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay().fadeOut();
});
