var forms = document.querySelectorAll(".org-form");
// console.log(forms[0].tagName);

// if (forms[0] != undefined) {
//     for (var i = 0; i < forms[0].length; i++) {
//         forms[0][i].classList.add("form-control");
//         console.log(forms[0][i]);

//         if (forms[0][i].tagName == 'SELECT') {
//             console.log('select tag')
//             forms[0][i].classList.add('select-tag');
//         }

//         if (forms[0][i].type == 'submit') {
//             forms[0][i].classList.add('form-control', 'btn', 'btn-primary', 'button-spacing');
//         }

//     }
// }

var cards = document.querySelectorAll(".landing-page-option");
//console.log(cards);

for (var i = 0; i < cards.length; i++) {
    if (i == 0) {
        cards[i].addEventListener('click', function (event) {
            window.location.href = '/post';
        });
    }
    if (i == 1) {
        cards[i].addEventListener('click', function (event) {
            window.location.href = '/find?seeking=donors';
        });
    }
    if (i == 2) {
        cards[i].addEventListener('click', function (event) {
            window.location.href = '/find?seeking=volunteer';
        });
    }

    cards[i].addEventListener('mouseover', function (event) {

        if (event.target.parentElement.className == 'landing-page-option flipper') {
            console.log('mouseover parent');
            //event.target.parentElement.childNodes[1].setAttribute("style", "color:red;");
            event.target.parentElement.childNodes[1].style.transform = 'rotateY(' + 180 + 'deg)';
            event.target.parentElement.childNodes[3].style.transform = 'rotateY(' + 360 + 'deg)';
        }

    });
    cards[i].addEventListener('mouseout', function (event) {

        if (event.target.parentElement.className == 'landing-page-option flipper') {
            console.log('mouseleave parent');
            //event.target.parentElement.childNodes[1].setAttribute("style", "color:red;");
            event.target.parentElement.childNodes[1].style.transform = 'rotateY(' + 0 + 'deg)';
            event.target.parentElement.childNodes[3].style.transform = 'rotateY(' + 180 + 'deg)';
        }
    });
}