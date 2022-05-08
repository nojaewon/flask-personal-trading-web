console.log('hello');

const myPageLink = $('a.my-page');
const myPageInterface = $('.mypage-interface');
const myPageClose = $('.mypage-close');

$(document).ready(function(){
    myPageLink.click(function(e){
        e.preventDefault();
        myPageInterface.animate({left:'60%'});
    });

    myPageClose.click(function(e){
        e.preventDefault();
        myPageInterface.animate({left:'100%'});
    })
})