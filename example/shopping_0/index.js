// index.js

document.addEventListener('DOMContentLoaded', function () {
    const featuredProducts = [
        { imgSrc: "product1.jpg", description: 'Description for product 1' },
        { imgSrc: "product2.jpg", description: 'Description for product 2' },
        { imgSrc: "product3.jpg", description: 'Description for product 3' }
    ];

    const featuredProductsContainer = document.getElementById('featured-products-container');
    featuredProducts.forEach(product => {
        let img = document.createElement('img');
        img.src = product.imgSrc;
        img.alt = product.description;
        img.style.width = '200px'; // ensuring the size
        img.style.height = '200px'; // ensuring the size
        img.style.objectFit = 'cover';
        featuredProductsContainer.appendChild(img);
    });
});

function navigate(page) {
    window.location.href = page;
}