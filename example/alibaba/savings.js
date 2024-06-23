document.addEventListener('DOMContentLoaded', () => {
    const products = [
        { imgSrc: "black_phone.jpg", description: 'A sleek black smartphone with a modern design.', price: 19.99, discount: 20, rating: 4.5 },
        { imgSrc: "red_dress.jpg", description: 'A stylish red dress perfect for special occasions.', price: 29.99, discount: 15, rating: 4.0 },
        { imgSrc: "coffee_machine.jpg", description: 'A high-quality coffee machine for your kitchen.', price: 9.99, discount: 30, rating: 3.5 },
        // Add more products as needed
    ];

    const productList = document.getElementById('product-list');

    function displayProducts(products) {
        productList.innerHTML = '';
        products.forEach(product => {
            const productDiv = document.createElement('div');
            productDiv.className = 'product';
            productDiv.innerHTML = `
                <img src="${product.imgSrc}" alt="${product.description}" description="${product.description}">
                <div class="product-description">
                    <p>${product.description}</p>
                    <p>Price: $${product.price}</p>
                    <p>Discount: ${product.discount}%</p>
                    <p>Rating: ${product.rating} stars</p>
                </div>
            `;
            productList.appendChild(productDiv);
        });
    }

    displayProducts(products);

    window.filterByCategory = function() {
        // Implement category filtering logic
        alert('Filter by category clicked!');
    };

    window.sortResults = function(criterion) {
        let sortedProducts;
        if (criterion === 'discount') {
            sortedProducts = [...products].sort((a, b) => b.discount - a.discount);
        } else if (criterion === 'price') {
            sortedProducts = [...products].sort((a, b) => a.price - b.price);
        } else if (criterion === 'rating') {
            sortedProducts = [...products].sort((a, b) => b.rating - a.rating);
        }
        displayProducts(sortedProducts);
    };

    window.searchProducts = function() {
        const searchInput = document.getElementById('search-input').value.toLowerCase();
        const filteredProducts = products.filter(product => product.description.toLowerCase().includes(searchInput));
        displayProducts(filteredProducts);
    };

    window.loadMoreProducts = function() {
        // Implement logic to load more products
        alert('Load more products clicked!');
    };
});