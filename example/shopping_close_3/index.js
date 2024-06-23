document.addEventListener('DOMContentLoaded', function() {
    const featuredProducts = [
        {imgSrc: "product1.jpg", description: "Description for product 1, such as a black phone"},
        {imgSrc: "product2.jpg", description: "Description for product 2, such as a smartwatch"},
        {imgSrc: "product3.jpg", description: "Description for product 3, such as a wireless speaker"}
    ];

    const productList = document.getElementById('product-list');
    featuredProducts.forEach(product => {
        const imgElement = document.createElement('img');
        imgElement.src = product.imgSrc;
        imgElement.alt = product.description;
        imgElement.setAttribute('description', product.description);
        productList.appendChild(imgElement);
    });

    // Additional JS to handle live chat support, promotional pop-ups, etc.
});