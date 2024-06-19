document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const rememberMe = document.getElementById('rememberMe').checked;

    // Simple validation
    if (username === 'testuser' && password === 'password123') {
        alert('Login successful!');
        window.location.href = 'profile.html';
    } else {
        alert('Incorrect username or password.');
    }

    // Handle remember me functionality (for demonstration purposes)
    if (rememberMe) {
        localStorage.setItem('username', username);
    } else {
        localStorage.removeItem('username');
    }
});

document.getElementById('forgotPassword').addEventListener('click', function(event) {
    event.preventDefault();
    alert('Password reset functionality coming soon!');
});

// Sample product data
const products = [
    { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone' },
    { imgSrc: "product2.jpg", description: 'Description for product 2, such as a red laptop' },
    { imgSrc: "product3.jpg", description: 'Description for product 3, such as a white tablet' }
];

// Add product images to the product section
const productSection = document.getElementById('product-section');

products.forEach(product => {
    const productDiv = document.createElement('div');
    productDiv.className = 'product';

    const img = document.createElement('img');
    img.src = product.imgSrc;
    img.alt = product.description;
    productDiv.appendChild(img);

    const description = document.createElement('div');
    description.className = 'product-description';
    description.innerText = product.description;
    productDiv.appendChild(description);

    const buyButton = document.createElement('button');
    buyButton.className = 'buy-now';
    buyButton.innerText = 'Buy Now';
    productDiv.appendChild(buyButton);

    productSection.appendChild(productDiv);
});