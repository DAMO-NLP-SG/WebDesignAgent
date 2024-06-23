document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('signin-form');
    const spinner = document.getElementById('loading-spinner');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        // Perform form validation and user authentication
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const usernameError = document.getElementById('username-error');
        const passwordError = document.getElementById('password-error');

        let isValid = true;

        if (!username) {
            usernameError.textContent = 'Username is required.';
            usernameError.style.display = 'block';
            isValid = false;
        } else {
            usernameError.style.display = 'none';
        }

        if (!password) {
            passwordError.textContent = 'Password is required.';
            passwordError.style.display = 'block';
            isValid = false;
        } else {
            passwordError.style.display = 'none';
        }

        if (!isValid) return;

        spinner.style.display = 'block';

        // Simulate authentication process (replace with real authentication logic)
        setTimeout(() => {
            spinner.style.display = 'none';
            if (username === 'user' && password === 'password') {
                alert('Authentication successful!');
                // Redirect to user's dashboard or another page
            } else {
                alert('Invalid credentials. Please try again.');
            }
        }, 2000);
    });

    document.getElementById('google-signin').addEventListener('click', function() {
        // Handle Google sign-in logic
        alert('Google sign-in clicked!');
    });

    document.getElementById('facebook-signin').addEventListener('click', function() {
        // Handle Facebook sign-in logic
        alert('Facebook sign-in clicked!');
    });
});