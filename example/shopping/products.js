document.addEventListener('DOMContentLoaded', () => {
    const products = [
        { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone', price: 29.99 },
        { imgSrc: "product2.jpg", description: 'Description for product 2, such as a white keyboard', price: 19.99 },
        { imgSrc: "product3.jpg", description: 'Description for product 3, such as a colorful abstract poster', price: 39.99 },
        // Add more products as needed
    ];

    const productContainer = document.getElementById('products');
    const paginationContainer = document.getElementById('pagination');
    const confirmationModal = document.getElementById('confirmationModal');
    const confirmationMessage = document.getElementById('confirmationMessage');
    const confirmAddToCartButton = document.getElementById('confirmAddToCart');
    const cancelAddToCartButton = document.getElementById('cancelAddToCart');
    let currentPage = 1;
    const itemsPerPage = 3;
    let selectedProduct = null;

    function renderProducts(products, page = 1) {
        productContainer.innerHTML = '';
        const startIndex = (page - 1) * itemsPerPage;
        const endIndex = startIndex + itemsPerPage;
        const paginatedProducts = products.slice(startIndex, endIndex);

        paginatedProducts.forEach(product => {
            const productCard = document.createElement('div');
            productCard.className = 'product-card';

            const productImg = document.createElement('img');
            productImg.src = product.imgSrc;
            productImg.alt = product.description;
            productImg.setAttribute('description', product.description);

            const productDesc = document.createElement('p');
            productDesc.textContent = product.description;

            const productPrice = document.createElement('p');
            productPrice.textContent = `$${product.price.toFixed(2)}`;

            const addToCartButton = document.createElement('button');
            addToCartButton.textContent = 'Add to Cart';
            addToCartButton.addEventListener('click', () => {
                selectedProduct = product;
                confirmationMessage.textContent = `Do you want to add "${product.description}" to the cart?`;
                confirmationModal.style.display = "block";
            });

            productCard.appendChild(productImg);
            productCard.appendChild(productDesc);
            productCard.appendChild(productPrice);
            productCard.appendChild(addToCartButton);

            productContainer.appendChild(productCard);
        });

        renderPagination(products.length, itemsPerPage, page);
    }

    function renderPagination(totalItems, itemsPerPage, currentPage) {
        paginationContainer.innerHTML = '';
        const totalPages = Math.ceil(totalItems / itemsPerPage);

        for (let i = 1; i <= totalPages; i++) {
            const paginationButton = document.createElement('button');
            paginationButton.className = 'pagination-button';
            paginationButton.textContent = i;
            paginationButton.disabled = i === currentPage;
            paginationButton.addEventListener('click', () => {
                renderProducts(products, i);
            });
            paginationContainer.appendChild(paginationButton);
        }
    }

    // Initial render
    renderProducts(products, currentPage);

    // Filtering and sorting functionality
    const searchInput = document.getElementById('search');
    const sortSelect = document.getElementById('sort');

    searchInput.addEventListener('input', () => {
        const searchTerm = searchInput.value.toLowerCase();
        const filteredProducts = products.filter(product => product.description.toLowerCase().includes(searchTerm));
        renderProducts(filteredProducts, 1);
    });

    sortSelect.addEventListener('change', () => {
        const sortValue = sortSelect.value;
        let sortedProducts = [...products];
        if (sortValue === 'price-asc') {
            sortedProducts.sort((a, b) => a.price - b.price);
        } else if (sortValue === 'price-desc') {
            sortedProducts.sort((a, b) => b.price - a.price);
        } else if (sortValue === 'popularity') {
            // Sorting by popularity, assuming we have a popularity attribute
            sortedProducts.sort((a, b) => b.popularity - a.popularity);
        }
        renderProducts(sortedProducts, 1);
    });

    // Modal functionality
    confirmAddToCartButton.addEventListener('click', () => {
        alert(`${selectedProduct.description} added to cart`);
        confirmationModal.style.display = "none";
        window.location.href = 'cart.html';
    });

    cancelAddToCartButton.addEventListener('click', () => {
        confirmationModal.style.display = "none";
    });

    window.onclick = function(event) {
        if (event.target === confirmationModal) {
            confirmationModal.style.display = "none";
        }
    }

    const closeModalButton = document.querySelector('.close');
    closeModalButton.addEventListener('click', () => {
        confirmationModal.style.display = "none";
    });
});