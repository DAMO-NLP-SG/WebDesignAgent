document.addEventListener('DOMContentLoaded', () => {
    loadFeaturedProducts();
    startCarousel();
    document.getElementById('search-bar').addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            searchProducts(event.target.value);
        }
    });
});

function navigateTo(page) {
    window.location.href = page;
}

function loadFeaturedProducts() {
    const products = [
        { imgSrc: 'product1.jpg', description: 'Description for product 1, such as a black camera' },
        { imgSrc: 'product2.jpg', description: 'Description for product 2, such as a white lotion' },
        { imgSrc: 'product3.jpg', description: 'Description for product 3, such as a grey perfume bottle' },
        { imgSrc: 'product4.jpg', description: 'Description for product 4, such as a silver clock' }
    ];

    const featuredProductsSection = document.getElementById('featured-products');
    products.forEach(product => {
        const productContainer = document.createElement('div');
        productContainer.classList.add('product-container');

        const imgElement = document.createElement('img');
        imgElement.src = product.imgSrc;
        imgElement.alt = product.description;
        imgElement.setAttribute('description', product.description);

        const descriptionElement = document.createElement('p');
        descriptionElement.textContent = product.description;

        productContainer.appendChild(imgElement);
        productContainer.appendChild(descriptionElement);

        featuredProductsSection.appendChild(productContainer);
    });
}

function startCarousel() {
    const carousel = document.querySelector('.carousel');
    const images = carousel.querySelectorAll('img');
    const indicators = document.querySelectorAll('.indicator');
    let index = 0;

    setInterval(() => {
        images.forEach(img => img.style.transform = 'translateX(100%)');
        indicators.forEach(indicator => indicator.classList.remove('active'));
        images[index].style.transform = 'translateX(0)';
        indicators[index].classList.add('active');
        index = (index + 1) % images.length;
    }, 3000);
}

function carouselControl(direction) {
    const carousel = document.querySelector('.carousel');
    const images = carousel.querySelectorAll('img');
    const indicators = document.querySelectorAll('.indicator');
    let currentIndex = Array.from(images).findIndex(img => img.style.transform === 'translateX(0)');

    images[currentIndex].style.transform = 'translateX(100%)';
    indicators[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + direction + images.length) % images.length;
    images[currentIndex].style.transform = 'translateX(0)';
    indicators[currentIndex].classList.add('active');
}

function currentSlide(n) {
    const images = document.querySelectorAll('.carousel img');
    const indicators = document.querySelectorAll('.indicator');
    images.forEach(img => img.style.transform = 'translateX(100%)');
    indicators.forEach(indicator => indicator.classList.remove('active'));
    images[n].style.transform = 'translateX(0)';
    indicators[n].classList.add('active');
}

function searchProducts(query) {
    if (query.trim()) {
        window.location.href = `products.html?search=${encodeURIComponent(query)}`;
    }
}