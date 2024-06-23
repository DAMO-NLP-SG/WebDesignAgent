document.addEventListener("DOMContentLoaded", function() {
    const products = [
        { imgSrc: "product1.jpg", description: "Description for product 1, such as a black phone", category: "category1", rating: 4.5, reviews: 10 },
        { imgSrc: "product2.jpg", description: "Description for product 2, such as a red dress", category: "category2", rating: 4.0, reviews: 5 },
        { imgSrc: "product3.jpg", description: "Description for product 3, such as a coffee machine", category: "category1", rating: 3.5, reviews: 8 },
        // Add more products as needed
    ];

    let currentPage = 1;
    const productsPerPage = 3;

    const productContainer = document.getElementById("product-list");
    const paginationContainer = document.getElementById("pagination");

    function displayProducts(products, page = 1) {
        productContainer.innerHTML = "";
        const start = (page - 1) * productsPerPage;
        const end = start + productsPerPage;
        const paginatedProducts = products.slice(start, end);

        paginatedProducts.forEach(product => {
            const productElement = document.createElement("div");
            productElement.className = "product";
            productElement.innerHTML = `
                <img src="${product.imgSrc}" alt="${product.description}" description="${product.description}">
                <p class="product-description">${product.description}</p>
                <p>Rating: ${product.rating}</p>
                <p>Reviews: ${product.reviews}</p>
            `;
            productContainer.appendChild(productElement);
        });

        renderPagination(products.length, page);
    }

    function renderPagination(totalProducts, currentPage) {
        paginationContainer.innerHTML = "";
        const totalPages = Math.ceil(totalProducts / productsPerPage);

        for (let i = 1; i <= totalPages; i++) {
            const pageButton = document.createElement("button");
            pageButton.textContent = i;
            pageButton.onclick = () => {
                displayProducts(products, i);
                currentPage = i;
            };
            if (i === currentPage) {
                pageButton.classList.add("active");
            }
            paginationContainer.appendChild(pageButton);
        }
    }

    function filterProducts(category) {
        document.querySelectorAll("#filters button").forEach(button => button.classList.remove("active"));
        document.getElementById(`filter-${category}`).classList.add("active");

        if (category === 'all') {
            displayProducts(products);
        } else {
            const filteredProducts = products.filter(product => product.category === category);
            displayProducts(filteredProducts);
        }
    }

    function sortProducts(criteria) {
        document.querySelectorAll("#sorting button").forEach(button => button.classList.remove("active"));
        document.getElementById(`sort-${criteria}`).classList.add("active");

        const sortedProducts = [...products].sort((a, b) => b[criteria] - a[criteria]);
        displayProducts(sortedProducts);
    }

    function searchProducts() {
        const query = document.getElementById("search-bar").value.toLowerCase();
        const filteredProducts = products.filter(product => product.description.toLowerCase().includes(query));
        displayProducts(filteredProducts);
    }

    // Initial display of products
    displayProducts(products);
});