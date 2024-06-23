document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('resetPasswordForm');
    const passwordInput = document.getElementById('newPassword');
    const passwordStrength = document.getElementById('passwordStrength');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const email = form.email.value;
        const newPassword = form.newPassword.value;
        const confirmPassword = form.confirmPassword.value;
        const captcha = form.captcha.value;

        if (newPassword !== confirmPassword) {
            alert('Passwords do not match!');
            return;
        }

        if (captcha !== '7') {
            alert('CAPTCHA is incorrect!');
            return;
        }

        // Simulate sending a password reset request
        console.log('Sending password reset request for:', email);
        // Add AJAX or fetch API for real request handling here

        alert('Password reset link sent to your email!');
        window.location.href = 'signin.html';
    });

    passwordInput.addEventListener('input', function() {
        const strength = getPasswordStrength(passwordInput.value);
        passwordStrength.textContent = `Password Strength: ${strength}`;
    });

    function getPasswordStrength(password) {
        const lengthCriteria = password.length >= 8;
        const numberCriteria = /[0-9]/.test(password);
        const specialCharCriteria = /[!@#$%^&*]/.test(password);

        if (lengthCriteria && numberCriteria && specialCharCriteria) {
            return 'Strong';
        } else if (lengthCriteria && (numberCriteria || specialCharCriteria)) {
            return 'Medium';
        } else {
            return 'Weak';
        }
    }

    // Adding additional promotional images
    const promotions = [
        { imgSrc: 'promo3.jpg', description: 'Flash sale on clothing!' },
        { imgSrc: 'promo4.jpg', description: 'Discounts on home appliances.' }
    ];
    const sidebar = document.querySelector('.sidebar');
    promotions.forEach(promo => {
        const img = document.createElement('img');
        img.src = promo.imgSrc;
        img.alt = promo.description;
        img.setAttribute('description', promo.description);
        sidebar.appendChild(img);
    });
});