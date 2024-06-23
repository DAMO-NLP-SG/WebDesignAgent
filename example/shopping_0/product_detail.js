document.addEventListener('DOMContentLoaded', () => {
    // Add related products dynamically
    const relatedProducts = [
        { imgSrc: 'related1.jpg', description: 'Related Product 1' },
        { imgSrc: 'related2.jpg', description: 'Related Product 2' },
        { imgSrc: 'related3.jpg', description: 'Related Product 3' }
    ];

    const carousel = document.querySelector('.carousel');
    relatedProducts.forEach(product => {
        const img = document.createElement('img');
        img.src = product.imgSrc;
        img.alt = product.description;
        img.description = product.description;
        carousel.appendChild(img);
    });

    // Handle adding to cart
    window.addToCart = () => {
        alert('Product added to cart!');
    };

    // Handle adding to wishlist
    window.addToWishlist = () => {
        alert('Product added to wishlist!');
    };

    // Handle sharing on Facebook
    window.shareOnFacebook = () => {
        alert('Product shared on Facebook!');
    };

    // Handle adding to compare
    window.addToCompare = () => {
        alert('Product added to compare!');
    };

    // Change main image on thumbnail click
    window.changeImage = (imgSrc) => {
        document.getElementById('main-product-image').src = imgSrc;
    };
});