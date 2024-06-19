document.addEventListener("DOMContentLoaded", function() {
    // Load dynamic reviews
    const reviews = [
        { name: "John Doe", review: "Amazing game! Loved the storyline and gameplay." },
        { name: "Jane Smith", review: "A truly unique experience, highly recommended!" }
    ];

    const reviewsContainer = document.getElementById('reviews');
    reviews.forEach(review => {
        const reviewElement = document.createElement('div');
        reviewElement.classList.add('review');
        reviewElement.innerHTML = `<strong>${review.name}</strong>: ${review.review}`;
        reviewsContainer.appendChild(reviewElement);
    });

    // Form submission for new reviews
    document.getElementById("reviewForm").addEventListener("submit", function(event) {
        event.preventDefault();
        
        const userName = document.getElementById("userName").value;
        const userReview = document.getElementById("userReview").value;
        
        const newReviewElement = document.createElement('div');
        newReviewElement.classList.add('review');
        newReviewElement.innerHTML = `<strong>${userName}</strong>: ${userReview}`;
        
        reviewsContainer.appendChild(newReviewElement);
        
        // Clear the form
        document.getElementById("reviewForm").reset();
    });
});