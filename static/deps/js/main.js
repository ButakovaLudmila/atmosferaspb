
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
    //submenu.addClass("active");
    submenu.fadeIn(300);

    $(".main-menu").on("mouseleave",function(){
      submenu.fadeOut(300);
    })
  });
