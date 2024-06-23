document.addEventListener('DOMContentLoaded', function() {
    // Event listeners for real-time feedback
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    usernameInput.addEventListener('input', validateInput);
    passwordInput.addEventListener('input', validateInput);

    function validateInput() {
        if (usernameInput.value.trim() === '' || passwordInput.value.trim() === '') {
            usernameInput.style.borderColor = 'red';
            passwordInput.style.borderColor = 'red';
        } else {
            usernameInput.style.borderColor = '#ced4da';
            passwordInput.style.borderColor = '#ced4da';
        }
    }
});

function authenticateUser() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const rememberMe = document.getElementById('remember-me').checked;

    if (username.trim() === '' || password.trim() === '') {
        alert('Please fill in both fields.');
        return;
    }

    // Dummy authentication logic
    if (username === 'user' && password === 'password') {
        alert('Login successful!');
        // Handle session management and redirection here
    } else {
        alert('Invalid username or password.');
    }
}