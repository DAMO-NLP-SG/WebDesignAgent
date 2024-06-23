document.addEventListener('DOMContentLoaded', function() {
    const cartItems = [
        {imgSrc: 'product1.jpg', description: 'Description for product 1, such as a black phone', price: 19.99, quantity: 2},
        {imgSrc: 'product2.jpg', description: 'Description for product 2, such as a smart speaker', price: 29.99, quantity: 1},
        // Add more items as needed
    ];

    const recommendedItems = [
        {imgSrc: 'recommended1.jpg', description: 'Recommended product 1', price: 15.99},
        {imgSrc: 'recommended2.jpg', description: 'Recommended product 2', price: 25.99},
        // Add more recommended items as needed
    ];

    const cartItemsContainer = document.getElementById('cart-items');
    const costDetailsContainer = document.getElementById('cost-details');
    const recommendationItemsContainer = document.getElementById('recommendation-items');

    function renderCartItems() {
        cartItemsContainer.innerHTML = '';
        cartItems.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.className = 'cart-item';
            itemElement.innerHTML = `
                <img src="${item.imgSrc}" alt="${item.description}" description="${item.description}">
                <div>
                    <p>${item.description}</p>
                    <p>Price: $${item.price}</p>
                    <p>Quantity: <input type="number" value="${item.quantity}" min="1"></p>
                </div>
            `;
            cartItemsContainer.appendChild(itemElement);
        });
        updateTotalCost();
    }

    function renderRecommendedItems() {
        recommendationItemsContainer.innerHTML = '';
        recommendedItems.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.className = 'recommendation-item';
            itemElement.innerHTML = `
                <img src="${item.imgSrc}" alt="${item.description}" description="${item.description}">
                <div>
                    <p>${item.description}</p>
                    <p>Price: $${item.price}</p>
                </div>
            `;
            recommendationItemsContainer.appendChild(itemElement);
        });
    }

    function updateTotalCost() {
        let totalCost = 0;
        cartItems.forEach(item => {
            totalCost += item.price * item.quantity;
        });
        costDetailsContainer.innerHTML = `
            <p>Total Cost: $${totalCost.toFixed(2)}</p>
        `;
    }

    document.getElementById('apply-discount').addEventListener('click', function() {
        // Add discount application logic here
        alert('Discount code applied!');
    });

    document.getElementById('checkout').addEventListener('click', function() {
        window.location.href = 'checkout.html';
    });

    document.getElementById('continue-shopping').addEventListener('click', function() {
        window.location.href = 'products.html';
    });

    document.getElementById('save-for-later').addEventListener('click', function() {
        // Add save for later logic here
        alert('Items saved for later!');
    });

    document.getElementById('view-shipping').addEventListener('click', function() {
        // Add logic to view estimated shipping costs
        alert('Estimated shipping cost is $10.00');
    });

    renderCartItems();
    renderRecommendedItems();
});