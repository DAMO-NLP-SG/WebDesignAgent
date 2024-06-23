// signup.js

document.addEventListener('DOMContentLoaded', function() {
    const usernameField = document.getElementById('username');
    const emailField = document.getElementById('email');
    const passwordField = document.getElementById('password');
    const confirmPasswordField = document.getElementById('confirmPassword');

    usernameField.addEventListener('input', function() {
        // Real-time validation and feedback for username
    });

    emailField.addEventListener('input', function() {
        // Real-time validation and feedback for email
    });

    passwordField.addEventListener('input', function() {
        // Real-time password strength meter
    });

    confirmPasswordField.addEventListener('input', function() {
        // Real-time validation for password confirmation
    });
});

function submitForm() {
    const form = document.getElementById('signupForm');
    
    // Perform form validation
    if (validateForm()) {
        // Handle form submission
        alert('Form submitted successfully!');
    } else {
        alert('Please correct the errors in the form.');
    }
}

function validateForm() {
    // Add validation logic here (e.g., check if passwords match, validate email format, etc.)
    return true;
}