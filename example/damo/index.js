function navigateTo(page) {
    window.location.href = page;
}

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Add more interactive elements as needed

document.addEventListener('DOMContentLoaded', function() {
    // Add any additional JavaScript functionalities here
    // Example: Adding a smooth scroll effect for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});