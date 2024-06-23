document.addEventListener("DOMContentLoaded", function() {
    const thumbnails = document.querySelectorAll('.thumbnails img');
    const mainImage = document.querySelector('.main-image img');

    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            mainImage.src = thumbnail.src;
            mainImage.alt = thumbnail.alt;
        });
    });
});

function addToCart() {
    alert("Product added to cart!");
}

function addToWishlist() {
    alert("Product added to wishlist!");
}

function shareOnFacebook() {
    alert("Product shared on Facebook!");
}

function addToCompare() {
    alert("Product added to comparison list!");
}

// Example of dynamically adding related products
const relatedProducts = [
    {imgSrc: "related1.jpg", description: "Description for related product 1, such as a black phone"},
    {imgSrc: "related2.jpg", description: "Description for related product 2, such as a laptop"},
    {imgSrc: "related3.jpg", description: "Description for related product 3, such as a smartwatch"}
];

const carousel = document.querySelector('.carousel');

relatedProducts.forEach(product => {
    const img = document.createElement('img');
    img.src = product.imgSrc;
    img.alt = product.description;
    img.setAttribute('description', product.description);
    carousel.appendChild(img);
});