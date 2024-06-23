// signup.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('signupForm');
    const passwordInput = document.getElementById('password');
    const passwordStrengthMeter = document.getElementById('passwordStrength');
    const confirmPasswordInput = document.getElementById('confirmPassword');
    const captchaContainer = document.getElementById('captchaContainer');
    const usernameInput = document.getElementById('username');
    const emailInput = document.getElementById('email');

    // Real-time validation feedback
    form.addEventListener('input', function(event) {
        const target = event.target;

        if (target === passwordInput) {
            updatePasswordStrength(passwordInput.value);
        }
        validateField(target);
    });

    // Password strength meter
    function updatePasswordStrength(password) {
        let strength = 0;
        if (password.length > 7) strength++;
        if (/[A-Z]/.test(password)) strength++;
        if (/[0-9]/.test(password)) strength++;
        if (/[^A-Za-z0-9]/.test(password)) strength++;
        
        passwordStrengthMeter.value = strength;
    }

    // CAPTCHA implementation (dummy for example)
    captchaContainer.innerHTML = '<img src="captcha.jpg" alt="CAPTCHA" style="width: 100px; height: 50px;"><input type="text" placeholder="Enter CAPTCHA">';
    
    // Form submission handling
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const isValid = validateForm();
        if (isValid) {
            alert('Form submitted successfully!');
            // Add form submission logic here
        }
    });

    function validateField(field) {
        const errorMsg = field.nextElementSibling;
        if (field.validity.valid) {
            errorMsg.textContent = '';
            errorMsg.style.display = 'none';
        } else {
            showError(field, errorMsg);
        }
    }

    function showError(field, errorMsg) {
        if (field.validity.valueMissing) {
            errorMsg.textContent = 'This field is required';
        } else if (field.validity.typeMismatch) {
            errorMsg.textContent = 'Please enter a valid value';
        } else if (field.validity.tooShort) {
            errorMsg.textContent = `Value should be at least ${field.minLength} characters; you entered ${field.value.length}.`;
        }
        errorMsg.style.display = 'block';
    }

    function validateForm() {
        let valid = true;
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;

        if (password !== confirmPassword) {
            const confirmPasswordError = document.getElementById('confirmPasswordError');
            confirmPasswordError.textContent = 'Passwords do not match!';
            confirmPasswordError.style.display = 'block';
            valid = false;
        }

        return valid;
    }
});