document.addEventListener('DOMContentLoaded', () => {
    const products = [
        { imgSrc: "product1.jpg", description: "Description for product 1" },
        { imgSrc: "product2.jpg", description: "Description for product 2" },
        // Add more products as needed
    ];

    const productContainer = document.getElementById('product-list');
    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.classList.add('product');

        const imgElement = document.createElement('img');
        imgElement.src = product.imgSrc;
        imgElement.alt = product.description;
        imgElement.setAttribute('description', product.description);

        const descElement = document.createElement('p');
        descElement.textContent = product.description;

        const viewButton = document.createElement('button');
        viewButton.textContent = 'View Product';
        viewButton.onclick = () => window.location.href = 'product_detail.html';

        const cartButton = document.createElement('button');
        cartButton.textContent = 'Add to Cart';
        cartButton.onclick = () => window.location.href = 'cart.html';

        const quickViewButton = document.createElement('button');
        quickViewButton.textContent = 'Quick View';
        quickViewButton.onclick = () => showQuickView(product);

        productElement.appendChild(imgElement);
        productElement.appendChild(descElement);
        productElement.appendChild(viewButton);
        productElement.appendChild(cartButton);
        productElement.appendChild(quickViewButton);

        productContainer.appendChild(productElement);
    });
});

function applyFilters() {
    // Implement filter functionality
}

function sortProducts() {
    // Implement sort functionality
}

function showQuickView(product) {
    // Implement quick view modal functionality
}