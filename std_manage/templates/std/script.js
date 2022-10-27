const card = document.getElementById('card')
const name = document.getElementById('name')
const phone = document.getElementById('phome')
const email = document.getElementById('email')
const address = document.getElementById('address')
const errorElement = document.getElementById('error')

form.addEventListener('btn btn-primary', (e) => {
    let messages = []
    if(name.value === ' ||' name.value == null) {
        messages.push('Name is required')
    }
    if (phone.length = 10) {
      messages.push('phone must be equal to 10 characters ')
    }
    if (messages.length > 0) {
        e.preventDefault()
        errorElement.innerText = messages.join(',')
    }
})