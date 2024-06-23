document.addEventListener('DOMContentLoaded', function() {
    const galleryImages = [
        { imgSrc: "product2.jpg", description: "Additional view of product 1" },
        { imgSrc: "product3.jpg", description: "Another angle of product 1" }
    ];

    const relatedProducts = [
        { imgSrc: "related1.jpg", description: "Related product 1" },
        { imgSrc: "related2.jpg", description: "Related product 2" }
    ];

    const productGallery = document.getElementById('product-gallery');
    galleryImages.forEach(image => {
        let imgElement = document.createElement('img');
        imgElement.src = image.imgSrc;
        imgElement.alt = image.description;
        imgElement.setAttribute('description', image.description);
        productGallery.appendChild(imgElement);
    });

    const relatedProductsSection = document.getElementById('related-products');
    relatedProducts.forEach(product => {
        let imgElement = document.createElement('img');
        imgElement.src = product.imgSrc;
        imgElement.alt = product.description;
        imgElement.setAttribute('description', product.description);
        relatedProductsSection.appendChild(imgElement);
    });

    document.getElementById('addToCart').addEventListener('click', function() {
        // Add to cart functionality
        alert('Product added to cart');
    });

    document.getElementById('addToWishlist').addEventListener('click', function() {
        // Add to wishlist functionality
        alert('Product added to wishlist');
    });

    document.getElementById('shareOnFacebook').addEventListener('click', function() {
        // Share on Facebook functionality
        alert('Product shared on Facebook');
    });

    document.getElementById('compareProduct').addEventListener('click', function() {
        // Compare product functionality
        alert('Product added to compare');
    });
});