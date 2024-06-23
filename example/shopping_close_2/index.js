document.addEventListener('DOMContentLoaded', () => {
    loadFeaturedProducts();
});

function navigateTo(page) {
    window.location.href = page;
}

function loadFeaturedProducts() {
    const products = [
        { imgSrc: "product1.jpg", description: "Description for product 1, such as a black phone" },
        { imgSrc: "product2.jpg", description: "Description for product 2, such as a white camera" },
        { imgSrc: "product3.jpg", description: "Description for product 3, such as a stylish watch" },
        { imgSrc: "product4.jpg", description: "Description for product 4, such as a modern chair" }
    ];

    const productList = document.getElementById('product-list');
    products.forEach(product => {
        const productDiv = document.createElement('div');
        const img = document.createElement('img');
        img.src = product.imgSrc;
        img.alt = product.description;
        img.description = product.description;
        productDiv.appendChild(img);
        productList.appendChild(productDiv);
    });
}