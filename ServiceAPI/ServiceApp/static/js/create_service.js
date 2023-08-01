"use strict"

function select_file() {
    let form = document.querySelectorAll("#id_ServiceFile")
    console.log(form)
    if (form[0].files[0] === undefined) {
        let span = document.querySelectorAll("span")
        console.log(span)
        span[1].innerHTML = 'Картинка не выбрана'
    } else {
        let span = document.querySelectorAll("span")
        span[1].innerHTML = '&nbsp'
    }
}

