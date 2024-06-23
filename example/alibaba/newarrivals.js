document.addEventListener('DOMContentLoaded', function() {
    const products = [
        { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone', price: "$20", rating: "4.5", availability: "In Stock", discount: "10%", reviews: 5 },
        { imgSrc: "product2.jpg", description: 'Description for product 2, such as a red dress', price: "$25", rating: "4.0", availability: "In Stock", discount: "15%", reviews: 10 },
        { imgSrc: "product3.jpg", description: 'Description for product 3, such as a kitchen item', price: "$15", rating: "3.5", availability: "Out of Stock", discount: "", reviews: 2 },
        // Add more products as needed
    ];

    const productGrid = document.getElementById('product-grid');

    function displayProducts(products) {
        productGrid.innerHTML = "";
        products.forEach(product => {
            const productItem = document.createElement('div');
            productItem.className = 'product-item';

            productItem.innerHTML = `
                <img src="${product.imgSrc}" alt="${product.description}" description="${product.description}">
                <div class="description">${product.description}</div>
                <div class="price">${product.price}</div>
                <div class="rating">${'★'.repeat(Math.floor(product.rating))}</div>
                <div class="availability">${product.availability}</div>
                ${product.discount ? `<div class="discount-badge">${product.discount} OFF</div>` : ''}
                <button class="quick-view" onclick="quickView('${product.description}', '${product.price}', '${product.availability}')">Quick View</button>
                <button class="wishlist" onclick="addToWishlist('${product.description}')">Add to Wishlist</button>
            `;

            productGrid.appendChild(productItem);
        });
    }

    function sortProducts(criteria) {
        // Implement sorting logic based on criteria
        if (criteria === 'popularity') {
            products.sort((a, b) => b.reviews - a.reviews);
        } else if (criteria === 'priceLowToHigh') {
            products.sort((a, b) => parseFloat(a.price.substring(1)) - parseFloat(b.price.substring(1)));
        } else if (criteria === 'priceHighToLow') {
            products.sort((a, b) => parseFloat(b.price.substring(1)) - parseFloat(a.price.substring(1)));
        } else if (criteria === 'newest') {
            // Assuming products array has a date property for sorting by newest
            products.sort((a, b) => new Date(b.date) - new Date(a.date));
        }
        displayProducts(products);
    }

    function filterProducts(criteria) {
        // Implement filtering logic based on criteria
        let filteredProducts = products;
        if (criteria === 'category') {
            // Assuming products array has a category property for filtering by category
            filteredProducts = products.filter(product => product.category === 'desiredCategory');
        } else if (criteria === 'priceRange') {
            // Example price range filter
            filteredProducts = products.filter(product => parseFloat(product.price.substring(1)) < 20);
        } else if (criteria === 'rating') {
            filteredProducts = products.filter(product => product.rating >= 4);
        }
        displayProducts(filteredProducts);
    }

    function quickView(description, price, availability) {
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close" onclick="closeModal()">&times;</span>
                <p>Description: ${description}</p>
                <p>Price: ${price}</p>
                <p>Availability: ${availability}</p>
            </div>
        `;
        document.body.appendChild(modal);
    }

    function closeModal() {
        const modal = document.querySelector('.modal');
        if (modal) {
            modal.remove();
        }
    }

    function addToWishlist(description) {
        alert(`Added to wishlist: ${description}`);
    }

    // Initial display of products
    displayProducts(products);

    // Load more functionality
    document.getElementById('load-more').addEventListener('click', function() {
        // Assuming additional products are fetched and added to the products array
        displayProducts(products);
    });
});