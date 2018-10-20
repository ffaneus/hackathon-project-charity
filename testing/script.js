var cards = document.querySelectorAll(".landing-page-option")

document.querySelector(".landing-page-option").addEventListener('mouseover', function (event) {

    // if (event.target.className == 'landing-page-option flipper'){
    //     console.log(event.target.childNodes)
    //     console.log('mouseover self');
    //     //event.target.childNodes[1].setAttribute("style", "color:red;");
    //     event.target.childNodes[1].style.transform = 'rotateY(' + 180 + 'deg)';
    //     event.target.childNodes[3].style.transform = 'rotateY(' + 360 + 'deg)';
    // }
    
    if(event.target.parentElement.className == 'landing-page-option flipper') {
        console.log('mouseover parent');
        //event.target.parentElement.childNodes[1].setAttribute("style", "color:red;");
        event.target.parentElement.childNodes[1].style.transform = 'rotateY(' + 180 + 'deg)';
        event.target.parentElement.childNodes[3].style.transform = 'rotateY(' + 360 + 'deg)';
    }

});

document.querySelector(".landing-page-option").addEventListener('mouseout', function (event) {
    //event.target.childNodes[1].submit();
    //console.log(event.target.className);
    //console.log(event.target.parentElement.className);

    // if (event.target.className == 'landing-page-option flipper') {
    //     console.log('mouseleave self');
    //     //event.target.childNodes[1].setAttribute("style", "color:red;");
    //     event.target.childNodes[1].style.transform = 'rotateY(' + 0 + 'deg)';
    //     event.target.childNodes[3].style.transform = 'rotateY(' + 180 + 'deg)';
    // }

    if (event.target.parentElement.className == 'landing-page-option flipper') {
        console.log('mouseleave parent');
        //event.target.parentElement.childNodes[1].setAttribute("style", "color:red;");
        event.target.parentElement.childNodes[1].style.transform = 'rotateY(' + 0 + 'deg)';
        event.target.parentElement.childNodes[3].style.transform = 'rotateY(' + 180 + 'deg)';
    }
});