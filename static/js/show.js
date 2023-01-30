const password = document.getElementById('password')
const checkbox = document.getElementById('checkbox')

checkbox.addEventListener('click', hideAndShow)

function hideAndShow(){
    password.type == 'password' ? password.type = 'text' : password.type='password'
}

