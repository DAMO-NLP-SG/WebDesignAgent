// reset_password.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('resetForm');
    const passwordStrength = document.getElementById('passwordStrength');
    const formFeedback = document.getElementById('formFeedback');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        formFeedback.textContent = 'Processing...';
        
        const email = document.getElementById('email').value;
        const newPassword = document.getElementById('newPassword').value;
        const confirmPassword = document.getElementById('confirmPassword').value;

        if (newPassword !== confirmPassword) {
            formFeedback.textContent = 'Passwords do not match!';
            return;
        }

        // Add token handling and secure password reset logic here

        formFeedback.textContent = 'Password reset link has been sent to your email!';
    });

    // Real-time password strength validation
    document.getElementById('newPassword').addEventListener('input', function() {
        const strength = getPasswordStrength(this.value);
        passwordStrength.textContent = `Password Strength: ${strength}`;
    });

    function getPasswordStrength(password) {
        let strength = 'Weak';
        if (password.length > 8) strength = 'Medium';
        if (password.length > 12 && /[A-Z]/.test(password) && /[0-9]/.test(password) && /[^A-Za-z0-9]/.test(password)) 
            strength = 'Strong';
        return strength;
    }

    // Add featured products dynamically
    const featuredProducts = [
        {imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone'},
        {imgSrc: "product2.jpg", description: 'Description for product 2, such as a red dress'},
        {imgSrc: "product3.jpg", description: 'Description for product 3, such as a blue watch'}
    ];

    const featuredProductsContainer = document.getElementById('featuredProducts');
    featuredProducts.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.classList.add('product');
        
        const productImg = document.createElement('img');
        productImg.src = product.imgSrc;
        productImg.alt = product.description;
        
        const productDesc = document.createElement('p');
        productDesc.textContent = product.description;
        
        productDiv.appendChild(productImg);
        productDiv.appendChild(productDesc);
        
        featuredProductsContainer.appendChild(productDiv);
    });
});