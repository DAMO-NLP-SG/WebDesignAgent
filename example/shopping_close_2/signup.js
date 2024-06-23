// signup.js
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('signupForm');
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm-password');
    const passwordStrength = document.querySelector('.password-strength');

    function updatePasswordStrength() {
        const strength = calculatePasswordStrength(password.value);
        passwordStrength.style.width = strength + '%';
        passwordStrength.style.backgroundColor = getStrengthColor(strength);
    }

    function calculatePasswordStrength(password) {
        let strength = 0;
        if (password.length >= 8) strength += 25;
        if (/[A-Z]/.test(password)) strength += 25;
        if (/[0-9]/.test(password)) strength += 25;
        if (/[^A-Za-z0-9]/.test(password)) strength += 25;
        return strength;
    }

    function getStrengthColor(strength) {
        if (strength <= 25) return 'red';
        if (strength <= 50) return 'orange';
        if (strength <= 75) return 'yellow';
        return 'green';
    }

    password.addEventListener('input', updatePasswordStrength);

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        if (password.value !== confirmPassword.value) {
            alert("Passwords do not match");
            return;
        }
        alert("Form submitted successfully!");
    });

    // Real-time validation feedback
    function validateUsername() {
        if (username.value.length < 3) {
            username.setCustomValidity("Username must be at least 3 characters long.");
        } else {
            username.setCustomValidity("");
        }
    }

    function validateEmail() {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email.value)) {
            email.setCustomValidity("Please enter a valid email address.");
        } else {
            email.setCustomValidity("");
        }
    }

    function validatePassword() {
        if (password.value.length < 8) {
            password.setCustomValidity("Password must be at least 8 characters long.");
        } else {
            password.setCustomValidity("");
        }
    }

    username.addEventListener('input', validateUsername);
    email.addEventListener('input', validateEmail);
    password.addEventListener('input', validatePassword);
});

function submitForm() {
    document.getElementById('signupForm').submit();
}