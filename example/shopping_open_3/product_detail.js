document.addEventListener('DOMContentLoaded', function() {
    const thumbnails = document.querySelectorAll('.thumbnails img');
    const mainImage = document.querySelector('.main-img');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const carousel = document.querySelector('.carousel');

    thumbnails.forEach(thumb => {
        thumb.addEventListener('click', function() {
            mainImage.src = this.src;
            mainImage.alt = this.alt;
            mainImage.setAttribute('description', this.getAttribute('description'));
        });
    });

    prevButton.addEventListener('click', function() {
        carousel.scrollBy({
            left: -200,
            behavior: 'smooth'
        });
    });

    nextButton.addEventListener('click', function() {
        carousel.scrollBy({
            left: 200,
            behavior: 'smooth'
        });
    });

    const reviewForm = document.querySelector('.review-form');
    reviewForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const name = reviewForm.querySelector('input').value;
        const review = reviewForm.querySelector('textarea').value;
        if (name && review) {
            alert('Review submitted');
        } else {
            alert('Please fill out all fields');
        }
    });
});

function addToCart() {
    alert('Product added to cart');
}

function addToWishlist() {
    alert('Product added to wishlist');
}

function shareOnFacebook() {
    alert('Product shared on Facebook');
}

function addToCompare() {
    alert('Product added to compare');
}