const products = [
    { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone', name: 'Product 1', price: '$10' },
    { imgSrc: "product2.jpg", description: 'Description for product 2, such as a smart home device', name: 'Product 2', price: '$20' },
    { imgSrc: "product3.jpg", description: 'Description for product 3, such as a modern kitchen appliance', name: 'Product 3', price: '$30' },
];

window.onload = function() {
    loadProducts(products);
};

function loadProducts(products) {
    const productList = document.getElementById('product-list');
    productList.innerHTML = '';
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.className = 'product';
        
        const img = document.createElement('img');
        img.src = product.imgSrc;
        img.alt = product.name;
        img.setAttribute('description', product.description);
        productDiv.appendChild(img);
        
        const name = document.createElement('h3');
        name.innerText = product.name;
        productDiv.appendChild(name);
        
        const price = document.createElement('p');
        price.innerText = product.price;
        productDiv.appendChild(price);
        
        const viewButton = document.createElement('button');
        viewButton.innerText = 'View Product';
        viewButton.onclick = () => { window.location.href = 'product_detail.html'; };
        productDiv.appendChild(viewButton);
        
        const cartButton = document.createElement('button');
        cartButton.innerText = 'Add to Cart';
        cartButton.onclick = () => { addToCart(product); };
        productDiv.appendChild(cartButton);

        const quickViewButton = document.createElement('button');
        quickViewButton.innerText = 'Quick View';
        quickViewButton.onclick = () => { showQuickView(product); };
        productDiv.appendChild(quickViewButton);

        productList.appendChild(productDiv);
    });
}

function applyFilters() {
    // Implement filtering logic here
}

function sortProducts() {
    // Implement sorting logic here
}

function addToCart(product) {
    // Implement add to cart functionality here
    alert(`${product.name} added to cart!`);
}

function showQuickView(product) {
    // Implement quick view modal functionality here
    alert(`Quick view for ${product.name}\nDescription: ${product.description}\nPrice: ${product.price}`);
}