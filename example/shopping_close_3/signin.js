function authenticateUser() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const rememberMe = document.getElementById('rememberMe').checked;
    
    // Perform input validation
    if (username === '' || password === '') {
        alert("Please fill in both fields.");
        return;
    }
    
    // Simulate authentication process
    if (username === 'user' && password === 'password') {
        alert("Login successful!");
        // Handle session management and redirection
        if (rememberMe) {
            // Store session data
            sessionStorage.setItem('username', username);
        }
        window.location.href = 'index.html';
    } else {
        alert("Invalid username or password.");
    }
}

// Function to add product images dynamically
function addProductImages() {
    const productGallery = document.querySelector('.product-gallery');
    const products = [
        { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone' },
        { imgSrc: "product2.jpg", description: 'Description for product 2, such as a red dress' },
        { imgSrc: "product3.jpg", description: 'Description for product 3, such as a blue laptop' },
        { imgSrc: "product4.jpg", description: 'Description for product 4, such as a green bag' }
    ];

    products.forEach(product => {
        const imgElement = document.createElement('img');
        imgElement.src = product.imgSrc;
        imgElement.alt = product.description;
        imgElement.description = product.description;
        productGallery.appendChild(imgElement);
    });
}

// Call the function to add product images on page load
window.onload = addProductImages;