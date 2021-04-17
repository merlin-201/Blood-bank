
$(document).ready(function(){

    $(".loading").fadeOut(1000);

    $("body").css("overflow" , "auto" )


    $('#animy1').slideDown( 1000 , function() {


        $('#animy2').slideDown( 1000 , function(){
            
            $('#animy3').slideDown(1000)
    
        }  )
     })

})

$('#animy1').click(function(){

    $('#donation').css( 'display'  , 'flex' );

 })

 $('#animy2').click(function(){

    $('#needDonation').css( 'display'  , 'flex' );

 })

$('#close , #nclose').click(function(){

    $('#donation').css( 'display' , 'none' )
    $('#needDonation').css( 'display' , 'none' )
})


let don = document.getElementById('don');
document.addEventListener("click" , function(e)
{
    if (e.target ==  don )  
    {
        $('#donation').css( 'display' , 'none' )    
    }

})
let ndon = document.getElementById('ndon');
document.addEventListener("click" , function(e)
{
    if (e.target ==  ndon )  
    {
        $('#needDonation').css( 'display' , 'none' )    
    }

})

$('.backwidth').click(function(){


    let idForm =  $(this).attr('id')

    let formSelector = '#' + idForm + '-m' ;

    let spanSelector = '#' + idForm + ' span';

    /////////////////////////////

    $('.backwidth').removeClass( 'currentbackwidth' )

   
    $('.backwidth span').removeClass( 'currentspan')

    $(this).addClass( 'currentbackwidth' )


    $(spanSelector).addClass( 'currentspan' )

    ////////////////////////

    $(formSelector).nextAll().hide(1000);

    $(formSelector).prevAll().hide(1000);

    $(formSelector).show(1000);  

})


$("#donation #nextButton").click(function(){
   
    $("#perInfo-m").hide(1000);
    $('#bloInfo-m').show(1000) ;
     /////////////////////////////

     $('.backwidth').removeClass( 'currentbackwidth' )

   
     $('.backwidth span').removeClass( 'currentspan')
 
     $('.backwidth2').addClass( 'currentbackwidth' )
 
  
     ////////////////////////

})


$("#needDonation #nextButton").click(function(){
    $("#nperInfo-m").hide(1000);
    $('#nbloInfo-m').show(1000) ; 

     /////////////////////////////

     $('.backwidth').removeClass( 'currentbackwidth' )

   
     $('.backwidth span').removeClass( 'currentspan')
 
     $('.backwidth2').addClass( 'currentbackwidth' )
 
  
     ////////////////////////

})

$("#donation #fillMessageButton").click(function(){

    $("#bloInfo-m").hide(1000);
    $('#getIn-m').show(1000) ; 
     /////////////////////////////

     $('.backwidth').removeClass( 'currentbackwidth' )

   
     $('.backwidth span').removeClass( 'currentspan')
 
     $('.backwidth3').addClass( 'currentbackwidth' )
 
  
     ////////////////////////

})


$("#needDonation #fillMessageButton").click(function(){

    $("#nbloInfo-m").hide(1000);
    $('#ngetIn-m').show(1000) ; 

     /////////////////////////////

     $('.backwidth').removeClass( 'currentbackwidth' )

   
     $('.backwidth span').removeClass( 'currentspan')
 
     $('.backwidth3').addClass( 'currentbackwidth' )
 
  
     ////////////////////////

})



$('#finalSubmit').click(function(){
    $("#needDonation").hide(1000);
    $('#resultsNeedDonation').show(1000) ;  
})

$('#submit').click(function(){
    
    $("#donation").hide(1000);
    $('#resultsDonation').show(1000) ;  
})




