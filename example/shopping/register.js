document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("registrationForm");
    const usernameInput = document.getElementById("username");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirmPassword");
    const passwordStrength = document.getElementById("passwordStrength");
    const usernameFeedback = document.getElementById("usernameFeedback");
    const emailFeedback = document.getElementById("emailFeedback");
    const registerButton = document.getElementById("registerButton");

    const productImages = [
        { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone' },
        { imgSrc: "product2.jpg", description: 'Description for product 2, such as a red handbag' },
        { imgSrc: "product3.jpg", description: 'Description for product 3, such as a white sneakers' },
    ];

    const productImagesContainer = document.getElementById("productImages");
    productImages.forEach(product => {
        const imgElement = document.createElement("img");
        imgElement.src = product.imgSrc;
        imgElement.alt = product.description;
        imgElement.description = product.description; // Adding description attribute
        productImagesContainer.appendChild(imgElement);
    });

    passwordInput.addEventListener("input", function() {
        const strength = calculatePasswordStrength(passwordInput.value);
        passwordStrength.textContent = `Password strength: ${strength}`;
    });

    usernameInput.addEventListener("input", function() {
        usernameFeedback.textContent = usernameInput.value.length < 3 ? "Username must be at least 3 characters long" : "";
    });

    emailInput.addEventListener("input", function() {
        const isValidEmail = validateEmail(emailInput.value);
        emailFeedback.textContent = isValidEmail ? "" : "Please enter a valid email address";
    });

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        if (validateForm()) {
            window.location.href = "profile.html";
        }
    });

    function calculatePasswordStrength(password) {
        let strength = "Weak";
        if (password.length > 8 && /[A-Z]/.test(password) && /[0-9]/.test(password)) {
            strength = "Strong";
        } else if (password.length > 6) {
            strength = "Medium";
        }
        return strength;
    }

    function validateEmail(email) {
        const re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        return re.test(email);
    }

    function validateForm() {
        const username = document.getElementById("username").value;
        const email = document.getElementById("email").value;
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;
        const terms = document.querySelector("input[name='terms']").checked;

        if (!username || !email || !password || !confirmPassword || !terms) {
            alert("All fields are required.");
            return false;
        }

        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            return false;
        }

        return true;
    }
});