document.addEventListener("DOMContentLoaded", function() {
    const thumbnails = [
        {imgSrc: "product1_thumb.jpg", description: 'Thumbnail for product 1'},
        {imgSrc: "product2_thumb.jpg", description: 'Thumbnail for product 2'},
        {imgSrc: "product3_thumb.jpg", description: 'Thumbnail for product 3'}
    ];

    const carousel = [
        {imgSrc: "related_product1.jpg", description: 'Related product 1'},
        {imgSrc: "related_product2.jpg", description: 'Related product 2'},
        {imgSrc: "related_product3.jpg", description: 'Related product 3'}
    ];

    const thumbnailContainer = document.querySelector('.thumbnails');
    const carouselContainer = document.querySelector('.carousel');

    thumbnails.forEach(thumbnail => {
        let img = document.createElement('img');
        img.src = thumbnail.imgSrc;
        img.alt = thumbnail.description;
        img.setAttribute('description', thumbnail.description);
        img.addEventListener('click', function() {
            document.querySelector('.main-image img').src = thumbnail.imgSrc.replace('_thumb', '');
        });
        thumbnailContainer.appendChild(img);
    });

    carousel.forEach(item => {
        let img = document.createElement('img');
        img.src = item.imgSrc;
        img.alt = item.description;
        img.setAttribute('description', item.description);
        carouselContainer.appendChild(img);
    });

    // Placeholder functions for button actions
    window.addToCart = function() {
        alert('Added to cart!');
    };

    window.addToWishlist = function() {
        alert('Added to wishlist!');
    };

    window.shareOnFacebook = function() {
        alert('Shared on Facebook!');
    };

    window.addToCompare = function() {
        alert('Added to compare!');
    };

    // Load More Reviews functionality
    document.querySelector('.load-more').addEventListener('click', function() {
        alert('Loading more reviews...');
        // Implement AJAX call to load more reviews and append them to the reviews section
    });
});