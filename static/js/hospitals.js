/*Hospital Ssection */
$(".tag h2").click(function(){
  var mkm= $(this).attr('target');
   $(`#div${mkm}`).show();
   $(`#div${mkm}`).nextAll().hide();
   $(`#div${mkm}`).prevAll().hide();  
});

console.log($("#hospitals").outerHeight());
/*Chat box*/
$(".sendIcon").click(sendData);
function sendData(){
  let message= document.getElementById("textarea").value;
 // console.log(message.length);
  //console.log($(".chatMessage input").outerHeight());
  
  let messageList= document.createElement("li");
  messageList.innerHTML =message;
  document.getElementById("messages").appendChild(messageList);
  $("#textarea").val("");
  
}






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
         $("#logo").attr("src" , "static/img/1logo.png") ;
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





/*Expansion Feature:
if(message.length>21){
    $(".chatMessage input").css({height:"4rem"});
    alert("hello");
     }


using JQuery:
 // let message= $("textarea").val();
// let m= $("#messages").appendChild(messageList);
m.css("display", "block");
 */
/* console.log(z);
  $("#targetedDiv").show(z);
  console.log($("#targetedDiv").html(z));
var z= $(`#div${mkm}`).html();
$("#targetedDiv").empty();
  $(".gm").show();
function changeContent(){
  var mkm= $(this).attr('target');
  var z= $(`#div${mkm}`);
  console.log(z);
  $("#targetedDiv").html(z);
  $("#targetedDiv").html($(`#div${mkm}`));

  console.log($("#targetedDiv").children());
  console.log($("#targetedDiv").find($(`#div${mkm}`)));*/
/*} 
//Sol: jquery children lis eq(),change in html
  //var booleanValue= $(`#div${mkm}`).hasClass("d-none");
  /*if(booleanValue==true){
    //$(`#div${mkm}`).removeClass("d-none");
   // $(`#div1`).addClass("d-none");
    $("#targetedDiv").html($(`#div${mkm}`));
  }
  else{ 
    $(`#div1`).removeClass("d-none");  
  }*/
  //let inText= $(`#div${mkm}`).text();
 // let inText= $(`#div${mkm}`);
  //console.log(inText);
 // document.getElementById("targetedDiv").innerHTML=$(`#div${mkm}`).text();
 // $("#targetedDiv").empty();
 //inText.show();
 


/*
ideas to implement this code: 
2)check siblings 
4)Hide/show/toggle
if(mkm!=1){
    $(`#div${mkm}`).animate({display:'block'},1000);

  } 
    jQuery(function() {
  jQuery('#showall').click(function() {
    jQuery('.targetDiv').show();
  });
  jQuery('.showSingle').click(function() {
    jQuery('.targetDiv').hide();
    jQuery('#div' + $(this).attr('target')).show();
  });
});
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<div class="buttons">
  <a id="showall">All</a>
  <a class="showSingle" target="1">Div 1</a>
  <a class="showSingle" target="2">Div 2</a>
  <a class="showSingle" target="3">Div 3</a>
  <a class="showSingle" target="4">Div 4</a>
</div>

<div id="div1" class="targetDiv">Lorum Ipsum1</div>
<div id="div2" class="targetDiv">Lorum Ipsum2</div>
<div id="div3" class="targetDiv">Lorum Ipsum3</div>
<div id="div4" class="targetDiv">Lorum Ipsum4</div>
   */
  /*
  Extras: 1)design, more detail for each hospital
  2)responsive design
  3)attach file button, local storage, more features in chat box.
  */