document.addEventListener('DOMContentLoaded', function() {
    const products = [
        { imgSrc: "product1.jpg", description: "Description for product 1, such as a black phone", name: "Product 1", reviews: 4.5 },
        { imgSrc: "product2.jpg", description: "Description for product 2, such as a blue shirt", name: "Product 2", reviews: 4.0 },
        { imgSrc: "product3.jpg", description: "Description for product 3, such as a white bottle", name: "Product 3", reviews: 3.5 },
        { imgSrc: "product4.jpg", description: "Description for product 4, such as a flower vase", name: "Product 4", reviews: 4.2 }
    ];

    function renderProducts(productList) {
        const productListElement = document.getElementById('product-list');
        productListElement.innerHTML = '';

        productList.forEach(product => {
            const productItem = document.createElement('div');
            productItem.className = 'product-item';

            const productImg = document.createElement('img');
            productImg.src = product.imgSrc;
            productImg.alt = product.name;

            const productDescription = document.createElement('p');
            productDescription.textContent = product.description;

            const productReviews = document.createElement('p');
            productReviews.textContent = `Rating: ${product.reviews} ★`;

            const viewButton = document.createElement('button');
            viewButton.textContent = 'View Product';
            viewButton.onclick = () => window.location.href = 'product_detail.html';

            const cartButton = document.createElement('button');
            cartButton.textContent = 'Add to Cart';
            cartButton.onclick = () => window.location.href = 'cart.html';

            const quickViewButton = document.createElement('button');
            quickViewButton.textContent = 'Quick View';
            quickViewButton.onclick = () => showQuickView(product);

            productItem.appendChild(productImg);
            productItem.appendChild(productDescription);
            productItem.appendChild(productReviews);
            productItem.appendChild(viewButton);
            productItem.appendChild(cartButton);
            productItem.appendChild(quickViewButton);

            productListElement.appendChild(productItem);
        });
    }

    function applyFilters() {
        // Example: Filter logic
        const filteredProducts = products.filter(product => product.reviews > 4);
        renderProducts(filteredProducts);
    }

    function sortProducts() {
        // Example: Sort logic
        const sortedProducts = [...products].sort((a, b) => b.reviews - a.reviews);
        renderProducts(sortedProducts);
    }

    function showQuickView(product) {
        const modal = document.getElementById('quick-view-modal');
        const modalBody = document.getElementById('modal-body');
        modalBody.innerHTML = `
            <h2>${product.name}</h2>
            <img src="${product.imgSrc}" alt="${product.name}">
            <p>${product.description}</p>
            <p>Rating: ${product.reviews} ★</p>
        `;
        modal.style.display = 'block';
    }

    function closeQuickView() {
        const modal = document.getElementById('quick-view-modal');
        modal.style.display = 'none';
    }

    renderProducts(products);
});