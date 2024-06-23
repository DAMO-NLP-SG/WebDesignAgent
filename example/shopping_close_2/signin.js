function authenticateUser() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    if (!username || !password) {
        alert('Please enter both username and password.');
        return;
    }

    // Simulate authentication process
    if (username === 'user' && password === 'pass') {
        alert('Login successful.');
        // Redirect to main page or user dashboard
        window.location.href = 'index.html';
    } else {
        alert('Invalid username or password.');
    }
}

// Real-time feedback, input validation, and session management can be added here
document.getElementById('signinForm').addEventListener('submit', function(event) {
    event.preventDefault();
    authenticateUser();
});

// Function to add images dynamically
function addProductImage(product) {
    const productContainer = document.createElement('div');
    productContainer.classList.add('product');

    const img = document.createElement('img');
    img.src = product.imgSrc;
    img.alt = product.description;
    img.description = product.description;

    const desc = document.createElement('p');
    desc.textContent = product.description;

    productContainer.appendChild(img);
    productContainer.appendChild(desc);

    document.querySelector('.products').appendChild(productContainer);
}

// Example of adding a product image dynamically
addProductImage({ imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone' });

// Add more product images as needed
addProductImage({ imgSrc: "product2.jpg", description: 'Description for product 2, such as a silver watch' });