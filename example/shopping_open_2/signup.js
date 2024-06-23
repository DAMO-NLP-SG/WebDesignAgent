document.addEventListener('DOMContentLoaded', function() {
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirmPassword');
    const captcha = document.getElementById('captcha');

    username.addEventListener('input', function() {
        validateField(username, 'usernameTooltip');
    });

    email.addEventListener('input', function() {
        validateField(email, 'emailTooltip');
    });

    password.addEventListener('input', function() {
        validateField(password, 'passwordTooltip');
        updatePasswordStrength(password.value);
    });

    confirmPassword.addEventListener('input', function() {
        validateField(confirmPassword, 'confirmPasswordTooltip');
    });

    captcha.addEventListener('input', function() {
        validateField(captcha, 'captchaTooltip');
    });
});

function validateField(field, tooltipId) {
    const tooltip = document.getElementById(tooltipId);
    if (field.value.trim() === '') {
        tooltip.style.display = 'block';
    } else {
        tooltip.style.display = 'none';
    }
}

function updatePasswordStrength(password) {
    const strengthMeter = document.getElementById('passwordStrength');
    let strength = 'Weak';
    if (password.length > 8 && /[A-Z]/.test(password) && /[0-9]/.test(password) && /[!@#$%^&*]/.test(password)) {
        strength = 'Strong';
        strengthMeter.style.color = 'green';
    } else if (password.length > 6) {
        strength = 'Medium';
        strengthMeter.style.color = 'orange';
    } else {
        strengthMeter.style.color = 'red';
    }
    strengthMeter.textContent = `Password Strength: ${strength}`;
}

function submitForm() {
    // Perform form validation and submission logic here
    if (validateForm()) {
        document.getElementById('confirmationMessage').textContent = 'Registration Successful!';
    } else {
        alert('Please fill out all fields correctly.');
    }
}

function validateForm() {
    const form = document.getElementById('registrationForm');
    const fields = form.querySelectorAll('input');
    let isValid = true;

    fields.forEach(field => {
        if (field.value.trim() === '') {
            isValid = false;
            validateField(field, `${field.id}Tooltip`);
        }
    });

    return isValid;
}