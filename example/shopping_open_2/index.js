document.addEventListener('DOMContentLoaded', () => {
    loadFeaturedProducts();
    setupLiveChatSupport();
    displayPromotionalPopups();
});

function navigateTo(page) {
    window.location.href = page;
}

function loadFeaturedProducts() {
    const products = [
        { imgSrc: "product1.jpg", title: 'Black Phone', price: '$299', description: 'High-quality smartphone with advanced features.' },
        { imgSrc: "product2.jpg", title: 'Stylish Jacket', price: '$99', description: 'Fashionable jacket for all seasons.' },
        { imgSrc: "product3.jpg", title: 'Modern Laptop', price: '$999', description: 'Powerful laptop for all your needs.' },
        { imgSrc: "product4.jpg", title: 'Smart Watch', price: '$199', description: 'Stylish smartwatch with various features.' }
    ];

    const productGrid = document.getElementById('product-grid');
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.className = 'product';

        const img = document.createElement('img');
        img.src = product.imgSrc;
        img.alt = product.title;
        img.setAttribute('description', product.description);

        const title = document.createElement('h3');
        title.textContent = product.title;

        const price = document.createElement('p');
        price.textContent = product.price;

        const desc = document.createElement('p');
        desc.textContent = product.description;

        const button = document.createElement('button');
        button.textContent = 'Shop Now';
        button.onclick = () => navigateTo('product_detail.html');

        productDiv.appendChild(img);
        productDiv.appendChild(title);
        productDiv.appendChild(price);
        productDiv.appendChild(desc);
        productDiv.appendChild(button);

        productGrid.appendChild(productDiv);
    });
}

function setupLiveChatSupport() {
    // Implementation of live chat support
}

function displayPromotionalPopups() {
    // Implementation of promotional pop-ups
}

function searchProducts() {
    // Implementation of search functionality
}

function filterCategory(category) {
    // Implementation of category filtering
}

document.getElementById('newsletter-form').addEventListener('submit', function (e) {
    e.preventDefault();
    document.getElementById('subscription-message').style.display = 'block';
});