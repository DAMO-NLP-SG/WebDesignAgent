const products = [
    { imgSrc: "product1.jpg", description: 'Description for product 1, a high-quality camera.', price: 500, category: 'electronics' },
    { imgSrc: "product2.jpg", description: 'Description for product 2, a beauty product set.', price: 150, category: 'beauty' },
    { imgSrc: "product3.jpg", description: 'Description for product 3, a smart home device.', price: 300, category: 'home' },
    { imgSrc: "product4.jpg", description: 'Description for product 4, a luxury watch.', price: 800, category: 'fashion' },
    { imgSrc: "product5.jpg", description: 'Description for product 5, a laptop with accessories.', price: 1000, category: 'electronics' }
];

function loadProducts(filteredProducts = products) {
    const productList = document.getElementById('product-list');
    productList.innerHTML = '';
    filteredProducts.forEach(product => {
        const productCard = document.createElement('div');
        productCard.className = 'product-card';
        productCard.innerHTML = `
            <img src="${product.imgSrc}" alt="${product.description}" description="${product.description}">
            <div class="product-description">
                <p>${product.description}</p>
            </div>
            <button onclick="showQuickView('${product.description}')">Quick View</button>
            <button onclick="addToCart()">Add to Cart</button>
        `;
        productList.appendChild(productCard);
    });
}

function applyFilters() {
    const category = document.getElementById('category-filter').value;
    const priceRange = document.getElementById('price-range').value;
    const filteredProducts = products.filter(product => {
        return (category === "" || product.category === category) && product.price <= priceRange;
    });
    loadProducts(filteredProducts);
    alert(`Filters applied! Category: ${category}, Price Range: Up to $${priceRange}`);
}

function sortProducts() {
    const sortedProducts = products.sort((a, b) => a.price - b.price);
    loadProducts(sortedProducts);
    alert('Products sorted!');
}

function addToCart() {
    // Implement add to cart logic here
    alert('Product added to cart!');
}

function showQuickView(description) {
    const modal = document.getElementById('quick-view-modal');
    const modalDescription = document.getElementById('quick-view-description');
    modalDescription.textContent = description;
    modal.style.display = "block";
}

function closeQuickView() {
    const modal = document.getElementById('quick-view-modal');
    modal.style.display = "none";
}

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function updatePriceRangeValue(value) {
    document.getElementById('price-range-value').textContent = `Up to $${value}`;
}

window.onscroll = function() {
    const backToTop = document.getElementById('back-to-top');
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        backToTop.style.display = "block";
    } else {
        backToTop.style.display = "none";
    }
}

document.addEventListener('DOMContentLoaded', loadProducts);