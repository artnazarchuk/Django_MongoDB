"use strict"

// уборка лишнего текста из формы
let form = document.querySelectorAll(".form")
form[0].childNodes[8].nodeValue = ''
form[0].childNodes[11].nodeValue = ''
form[0].childNodes[9].innerHTML = ''

let name_service = document.querySelectorAll("#id_ServiceName")
let name_service2 = document.querySelectorAll("#service_name")
name_service2[0].innerHTML = name_service[0].value

function select_file() {
    let form = document.querySelectorAll("#id_ServiceFile")
    if (form[0].files[0] === undefined) {
        let span = document.querySelectorAll("span")
        span[1].innerHTML = 'Картинка не выбрана'
    } else {
        let span = document.querySelectorAll("span")
        span[1].innerHTML = '&nbsp'
        let file_name = form[0].files[0].name;
        let img = document.getElementsByTagName('img')
        img[0].attributes.src.nodeValue = '/ServiceApp/static/image/' + file_name;

        let name_service = document.querySelectorAll("#id_ServiceName")
        let name_service2 = document.querySelectorAll("#service_name")
        name_service2[0].innerHTML = name_service[0].value

        let div_rotate = document.querySelector('div[id="div_rotate"]')
        if (div_rotate.className === 'image animate__animated animate__flipInX') {
            div_rotate.className = 'image animate__animated animate__flipInY'
        } else {
            div_rotate.className = 'image animate__animated animate__flipInX'
        }
    }
}

let img_src = document.querySelectorAll('img[id="id_image"]')
let a = document.querySelectorAll('a')
img_src[0].attributes[0].nodeValue = a[6].attributes.href.nodeValue

let div_rotate = document.querySelector('div[id="div_rotate"]')
div_rotate.addEventListener("click", function () {
    if (div_rotate.className === 'image animate__animated animate__flipInX') {
        div_rotate.className = 'image animate__animated animate__flipInY'
    } else {
        div_rotate.className = 'image animate__animated animate__flipInX'
    }
})