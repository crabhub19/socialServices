$(document).ready(function () {
    $(window).on('scroll',function(){
        var scroll = $(window).scrollTop();
        if(scroll>=50){
            $(".s-nav").addClass("add-scroll");
        }else{
            $(".s-nav").removeClass("add-scroll");
        }
    })
    var typed1 = new Typed('.text-for-me', {
        strings: ["My name is bishal.^1000\n I am a web developer. ","","And I have developed this web for your luxury"],
        smartBackspace:true,
        typeSpeed: 100,
        backSpeed: 0,
        loop: true,
        loopCount:Infinity,
        startDelay: 1000,
        cursorChar: '_',
      });
    var typed2 = new Typed('.text-for-webservices', {
        strings: ["get Taxi","get Rickshaw","get Labour","get Servanted","get Electrician"],
        smartBackspace:true,
        typeSpeed: 100,
        backSpeed: 100,
        loop: true,
        loopCount:Infinity,
        startDelay: 3000,
      });
});


$(document).ready(function () {
    var filterizd = $('#worker-container').filterizr({
        animationDuration : .5,
        filter: 'all',
        
       });
 
       
 });