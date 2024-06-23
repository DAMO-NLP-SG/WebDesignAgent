// products.js

document.addEventListener('DOMContentLoaded', () => {
    const products = [
        {imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone'},
        {imgSrc: "product2.jpg", description: 'Description for product 2, such as a smart watch'},
        {imgSrc: "product3.jpg", description: 'Description for product 3, such as a skincare set'},
        // Add more products as needed
    ];

    const productContainer = document.getElementById('product-list');
    
    products.forEach((product, index) => {
        const productItem = document.createElement('div');
        productItem.className = 'product-item';
        
        const productImage = document.createElement('img');
        productImage.src = product.imgSrc;
        productImage.alt = `Product ${index + 1}`;
        productImage.setAttribute('description', product.description);
        
        const productDescription = document.createElement('p');
        productDescription.className = 'product-description';
        productDescription.innerText = product.description;

        const viewButton = document.createElement('button');
        viewButton.innerText = 'View Product';
        viewButton.onclick = () => window.location.href = 'product_detail.html';
        
        const cartButton = document.createElement('button');
        cartButton.innerText = 'Add to Cart';
        cartButton.onclick = () => window.location.href = 'cart.html';
        
        const quickViewButton = document.createElement('button');
        quickViewButton.innerText = 'Quick View';
        quickViewButton.onclick = () => showQuickView(product);

        productItem.appendChild(productImage);
        productItem.appendChild(productDescription);
        productItem.appendChild(viewButton);
        productItem.appendChild(cartButton);
        productItem.appendChild(quickViewButton);
        
        productContainer.appendChild(productItem);
    });
});

function applyFilters() {
    // Filter functionality
    alert('Filter functionality to be implemented');
}

function sortProducts() {
    // Sort functionality
    alert('Sort functionality to be implemented');
}

function showQuickView(product) {
    // Quick view functionality
    alert(`Quick view for: ${product.description}`);
}