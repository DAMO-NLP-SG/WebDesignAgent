// reset_password.js

document.addEventListener('DOMContentLoaded', function() {
    const resetForm = document.getElementById('reset-form');

    resetForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const email = document.getElementById('email').value;
        const newPassword = document.getElementById('new-password').value;
        const confirmPassword = document.getElementById('confirm-password').value;
        const captchaInput = document.getElementById('captcha-input').value;
        const captcha = document.getElementById('captcha-container').textContent;
        const securityAnswer = document.getElementById('security-answer').value;

        if (newPassword !== confirmPassword) {
            alert('Passwords do not match!');
            return;
        }

        if (captchaInput !== captcha) {
            alert('Incorrect CAPTCHA!');
            return;
        }

        document.getElementById('loading-indicator').style.display = 'block';
        setTimeout(() => {
            alert('Password reset link has been sent to your email.');
            document.getElementById('loading-indicator').style.display = 'none';
        }, 2000);
    });

    const newPasswordInput = document.getElementById('new-password');
    newPasswordInput.addEventListener('input', function() {
        const strength = document.getElementById('password-strength');
        const value = newPasswordInput.value;
        if (value.length < 6) {
            strength.textContent = 'Weak';
            strength.style.color = 'red';
        } else if (value.length < 10) {
            strength.textContent = 'Moderate';
            strength.style.color = 'orange';
        } else {
            strength.textContent = 'Strong';
            strength.style.color = 'green';
        }
    });

    const emailInput = document.getElementById('email');
    emailInput.addEventListener('input', function() {
        const emailFeedback = document.getElementById('email-feedback');
        const emailValue = emailInput.value;
        if (validateEmail(emailValue)) {
            emailFeedback.textContent = 'Valid email';
            emailFeedback.style.color = 'green';
        } else {
            emailFeedback.textContent = 'Invalid email';
            emailFeedback.style.color = 'red';
        }
    });

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    window.navigateTo = function(page) {
        window.location.href = page;
    };

    generateCaptcha();
});

function generateCaptcha() {
    const captchaContainer = document.getElementById('captcha-container');
    const captcha = Math.random().toString(36).substring(7);
    captchaContainer.textContent = captcha;
}