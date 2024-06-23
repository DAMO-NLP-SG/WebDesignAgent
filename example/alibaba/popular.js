// popular.js

document.addEventListener("DOMContentLoaded", () => {
    const products = [
        { imgSrc: "product1.jpg", description: "Description for product 1, such as a black phone", title: "Product 1", rating: 4.5, price: "$19.99" },
        { imgSrc: "product2.jpg", description: "Description for product 2, such as red dresses", title: "Product 2", rating: 4.0, price: "$29.99" },
        { imgSrc: "product3.jpg", description: "Description for product 3, such as a coffee machine", title: "Product 3", rating: 5.0, price: "$39.99" },
        // Add more products as needed
    ];

    const productContainer = document.getElementById("product-list");

    function displayProducts(products) {
        productContainer.innerHTML = '';
        products.forEach(product => {
            const productDiv = document.createElement("div");
            productDiv.classList.add("product-item");
            productDiv.innerHTML = `
                <img src="${product.imgSrc}" alt="${product.title}" description="${product.description}">
                <h3>${product.title}</h3>
                <p>${product.description}</p>
                <p>Rating: ${product.rating} ⭐</p>
                <p>Price: ${product.price}</p>
            `;
            productDiv.addEventListener('click', () => openModal(product));
            productContainer.appendChild(productDiv);
        });
    }

    function openModal(product) {
        const modal = document.getElementById("product-modal");
        const modalContent = document.getElementById("modal-product-details");
        modalContent.innerHTML = `
            <img src="${product.imgSrc}" alt="${product.title}">
            <h3>${product.title}</h3>
            <p>${product.description}</p>
            <p>Rating: ${product.rating} ⭐</p>
            <p>Price: ${product.price}</p>
            <div class="reviews">
                <h4>Customer Reviews</h4>
                <p>Review 1: Great product!</p>
                <p>Review 2: Worth every penny!</p>
            </div>
        `;
        modal.style.display = "block";
        modal.style.opacity = 1;
    }

    function closeModal() {
        const modal = document.getElementById("product-modal");
        modal.style.opacity = 0;
        setTimeout(() => { modal.style.display = "none"; }, 400);
    }

    const modalClose = document.querySelector(".close");
    modalClose.addEventListener("click", closeModal);

    window.addEventListener("click", (event) => {
        const modal = document.getElementById("product-modal");
        if (event.target == modal) {
            closeModal();
        }
    });

    displayProducts(products);

    // Add event listeners for filtering and sorting
    document.getElementById('filter').addEventListener('change', (e) => {
        const category = e.target.value;
        const filteredProducts = category === 'all' ? products : products.filter(p => p.title.toLowerCase().includes(category));
        displayProducts(filteredProducts);
    });

    document.getElementById('sort').addEventListener('change', (e) => {
        const sortBy = e.target.value;
        const sortedProducts = [...products].sort((a, b) => {
            if (sortBy === 'price') {
                return parseFloat(a.price.substring(1)) - parseFloat(b.price.substring(1));
            } else if (sortBy === 'rating') {
                return b.rating - a.rating;
            } else { // popularity
                return b.rating - a.rating; // Assuming popularity is similar to rating for this example
            }
        });
        displayProducts(sortedProducts);
    });
});