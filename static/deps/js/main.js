
    //Выпадающая подсказка
document.addEventListener( "DOMContentLoaded" , function() {
  document.querySelector('.tooltip').addEventListener('click', function() {
    var tooltipText = this.querySelector('.tooltiptext');
    tooltipText.style.visibility = tooltipText.style.visibility === 'visible' ? 'hidden' : 'visible';
  });
    });
  

     // Выпадающее меню
  $("[data-trigger='dropdown']").on("mouseenter",function(){
    var submenu = $(this).parent().find(".submenu");
    submenu.addClass("active");
    submenu.fadeIn(10000);

    $(".main-menu").on("mouseleave",function(){
      submenu.fadeOut(10000);
    })
  });


  var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle("active");

        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}