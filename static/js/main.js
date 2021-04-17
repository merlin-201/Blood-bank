




$(window).scroll(function(){


    let scrollTopValue =  $(this).scrollTop();
    

    if( scrollTopValue > 100){
        $(".mainMenu").css({ backgroundColor : "#fff"  , top : "0"});
        $(".nav-link").css({color : "#000"} );
        $(".contectSection").css({ display : "none" });
        $("#logo").attr("src" , "/static/img/dark-version-logo.png") ;
        
    }
    else {
        $(".mainMenu").css({ backgroundColor : "rgba(0,0,0,0)" , top : "40"});
        $(".nav-link").css({color : "#fff"} );
        $(".contectSection").css({ display : "inline-block"});
         $("#logo").attr("src" , "/static/img/1logo.png") ;
    }


    $("section").each(function(){




    })
    let menuHight = $(".mainMenu").height();

     $("section").each(function(){
        let  thisSection = $(this);
        
        
        if( thisSection.offset().top <  (scrollTopValue + menuHight)  &&  (thisSection.offset().top + thisSection.outerHeight() ) > (scrollTopValue + menuHight) ){
            let classCatch = '.'+thisSection.attr("class")+'-N';
            $(".nav-link").removeClass("customColor");
            $(classCatch).addClass("customColor") 
        }
        
        
     })
    

})




$(".nav-link").click( ScrollFunction )

function ScrollFunction(){

    
    let menuLink = $(this).attr("href");
    let rowTopPosition = $(menuLink).offset().top;
    $("body").animate({ scrollTop :  rowTopPosition } , 1000);


    $(".nav-link").removeClass("customColor")
    $(this).addClass("customColor");


}

/* sroll button */

$(".clickButton").click(function(){
     let serviceSectionPosition =  $("#header").offset().top;
   $("body").animate({ scrollTop : serviceSectionPosition } , 1000) ; 
})




/* Slider */

$(".sectionslider1").css({display : "none"});
$(".sectionslider2").css({display : "none"});
$(".sectionslider3").css({display : "none"});
$("#content1").css({display : "none"});
$("#content2").css({display : "none"});
$("#content3").css({display : "none"});

/*
setInterval(function(){
    if( $(".sectionslider1").show() ){
        $(".sectionslider1").slideUp(2000);
        $(".sectionslider2").show(2000);
    }
    else if($(".sectionslider2").show() ){
        $(".sectionslider2").slideUp(2000);
        $(".sectionslider3").show(2000);

    }
    else if($(".sectionslider3").show()){
        $(".sectionslider3").slideUp(2000);
        $(".sectionslider1").show(1000);
    }
    
} , 8000)
*/


$(document).ready(function(){


    $(".sectionslider1").show(2000 , function(){
        $("#content1").fadeIn(2000);
        $("#slide1").addClass("whiteBG");
    });

    $("#slide1").click(function(){
        $(".sectionslider2").slideUp(2000);
        $(".sectionslider3").slideUp(2000);
        $(".sectionslider1").show(1000);
        $(".switcher div").removeClass("whiteBG");
        $(this).addClass("whiteBG");
       
      })
    
    $("#slide2").click(function(){
        $(".sectionslider3").slideUp(1000);
        $(".sectionslider1").slideUp(2000);
        $(".sectionslider2").show(1000 , function(){
            $("#content2").fadeIn(2000);
        });
        $(".switcher div").removeClass("whiteBG");
        $(this).addClass("whiteBG");
     
    })
    $("#slide3").click(function(){
        $(".sectionslider1").slideUp(2000);
        $(".sectionslider2").slideUp(2000);
        $(".sectionslider3").show(1000 ,  function(){
            $("#content3").fadeIn(2000);
        });
        $(".switcher div").removeClass("whiteBG");
        $(this).addClass("whiteBG");
      })

})


/** End Slider **/




/* Form */


$("#sentInfo").click(function(){
    $(".firstForm").slideUp(1000 , function(){
        $(".secondForm").slideDown(1000);
    });
    
})

$("#searchResult").click(function(){
    $(".secondForm").slideUp(1000 , function(){
        $(".resultSection").slideDown(1000);
    });
})