const form = document.getElementById('myForm');
const usernameInput = document.getElementById('username');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const messageDiv = document.getElementById('message');
const toggleButton = document.getElementById('toggleButton');
const usernameError = document.getElementById('usernameError');
const emailError = document.getElementById('emailError');
const passwordError = document.getElementById('passwordError');

form.addEventListener('submit', function(event) {
    let isValid = true;

    // Username validation
    if (usernameInput.value.trim() === '') {
        usernameError.textContent = 'Username is required.';
        isValid = false;
    } else {
        usernameError.textContent = '';
    }

    // Email validation
    if (emailInput.value.trim() === '') {
        emailError.textContent = 'Email is required.';
        isValid = false;
    } else if (!/\S+@\S+\.\S+/.test(emailInput.value)) {
        emailError.textContent = 'Invalid email format.';
        isValid = false;
    } else {
        emailError.textContent = '';
    }

    // Password validation
    if (passwordInput.value.length < 6) {
        passwordError.textContent = 'Password must be at least 6 characters.';
        isValid = false;
    } else {
        passwordError.textContent = '';
    }

    if (!isValid) {
        event.preventDefault(); // Prevent form submission if validation fails
    } else {
        messageDiv.textContent = 'Form submitted successfully!';
        messageDiv.style.display = 'block';
        event.preventDefault(); //prevent the form from actually submitting.
    }
});

toggleButton.addEventListener('click', function() {
    if (messageDiv.style.display === 'none') {
        messageDiv.style.display = 'block';
    } else {
        messageDiv.style.display = 'none';
    }
});

form.addEventListener('reset', function(){
    usernameError.textContent = '';
    emailError.textContent = '';
    passwordError.textContent = '';
    messageDiv.style.display = 'none';
})