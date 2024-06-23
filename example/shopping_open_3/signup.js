document.addEventListener("DOMContentLoaded", function() {
    const username = document.getElementById("username");
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirmPassword");
    const captcha = document.getElementById("captcha");
    const passwordStrengthMeter = document.getElementById("passwordStrengthMeter");

    username.addEventListener("input", validateUsername);
    email.addEventListener("input", validateEmail);
    password.addEventListener("input", validatePassword);
    confirmPassword.addEventListener("input", validateConfirmPassword);
    captcha.addEventListener("input", validateCaptcha);

    function validateUsername() {
        const error = document.getElementById("usernameError");
        const regex = /^[a-zA-Z0-9_]{5,}$/;
        if (!regex.test(username.value)) {
            error.textContent = "Username must be at least 5 characters long and contain only letters, numbers, and underscores.";
        } else {
            error.textContent = "";
        }
    }

    function validateEmail() {
        const error = document.getElementById("emailError");
        const regex = /^\S+@\S+\.\S+$/;
        if (!regex.test(email.value)) {
            error.textContent = "Please enter a valid email address.";
        } else {
            error.textContent = "";
        }
    }

    function validatePassword() {
        const error = document.getElementById("passwordError");
        const strength = calculatePasswordStrength(password.value);
        passwordStrengthMeter.value = strength;
        passwordStrengthMeter.style.setProperty('--strength-color', passwordStrengthColors[strength]);
        if (strength < 3) {
            error.textContent = "Password is too weak.";
        } else {
            error.textContent = "";
        }
    }

    function validateConfirmPassword() {
        const error = document.getElementById("confirmPasswordError");
        if (confirmPassword.value !== password.value) {
            error.textContent = "Passwords do not match.";
        } else {
            error.textContent = "";
        }
    }

    function validateCaptcha() {
        const error = document.getElementById("captchaError");
        // Placeholder validation for captcha
        if (captcha.value !== "1234") {
            error.textContent = "Captcha is incorrect.";
        } else {
            error.textContent = "";
        }
    }

    function calculatePasswordStrength(password) {
        let strength = 0;
        if (password.length >= 8) strength++;
        if (/[A-Z]/.test(password)) strength++;
        if (/[a-z]/.test(password)) strength++;
        if (/[0-9]/.test(password)) strength++;
        if (/[^A-Za-z0-9]/.test(password)) strength++;
        return strength;
    }

    const passwordStrengthColors = ["#ff0000", "#ff4000", "#ff8000", "#ffbf00", "#bfff00", "#40ff00"];

    window.submitForm = function() {
        validateUsername();
        validateEmail();
        validatePassword();
        validateConfirmPassword();
        validateCaptcha();

        if (document.querySelectorAll('.error:empty').length === 5) {
            alert("Form submitted successfully!");
            // Actual form submission logic here
        } else {
            alert("Please fix the errors in the form.");
        }
    }

    // Adding images through JavaScript
    const products = [
        {imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone'},
        {imgSrc: "product2.jpg", description: 'Description for product 2, such as a red bag'},
        {imgSrc: "product3.jpg", description: 'Description for product 3, such as a blue shirt'}
    ];

    products.forEach((product, index) => {
        const productDiv = document.getElementById(`product${index + 1}`);
        const img = document.createElement('img');
        img.src = product.imgSrc;
        img.alt = product.description;
        img.style.width = '100px';
        img.style.height = '100px';
        img.style.borderRadius = '10px';
        productDiv.appendChild(img);
    });
});