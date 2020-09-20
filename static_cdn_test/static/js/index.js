$(document).ready(function () {

      $(document).scroll(function () {
            if ($(window).scrollTop() > 100) { document.getElementById("scrollBtn").style.display = "block"; }

            if ($(window).scrollTop() > 700) {
                  $("nav").removeClass("nav-exit")
                  $("nav").addClass("nav-entry")
            }
            else if ($(window).scrollTop() > 100) {
                  if ($("nav").hasClass("nav-entry")) {
                        $("nav").addClass("nav-exit")
                        $("nav").removeClass("nav-entry")
                  }
            }
            else {
                  document.getElementById("scrollBtn").style.display = "none";
                  if ($("nav").hasClass("nav-exit")) {
                        $("nav").removeClass("nav-exit")
                  }
            }
      });

      $("#scrollBtn").click(function () {
            $('html, body').animate({
                  scrollTop: 0
            }, 1000, 'easeInOutExpo');
      });
      $('#dropdown2').hover(function () {
            if((document.getElementById("dropdown-content")).style.display == "none"){
            $('#dropdown-content').animate({ 'top': '30px', 'left': '20px' }, { duration: 400, queue: false }).fadeIn(400)
            }
            else{
                  $('#dropdown-content').hide()
            }
      }, function () {
            $('#dropdown-content').hide()
            $('#dropdown-content').css({ 'top': '50px', 'left': '40px' })
      })

      $('body').click(function (evt) {
            if (evt.target.id == "navbarSupportedContent")
                  return;
            if ($(evt.target).closest('#navbarSupportedContent').length)
                  return;

            $('.navbar-collapse').collapse('hide');
      });

});