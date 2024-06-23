// cart.js

document.addEventListener('DOMContentLoaded', function() {
    const cartItems = [
        { imgSrc: "product1.jpg", description: 'A sleek black phone with high-resolution display', quantity: 2, price: 20 },
        { imgSrc: "product2.jpg", description: 'Stylish wireless earbuds with noise cancellation', quantity: 1, price: 50 }
    ];

    const productRecommendations = [
        { imgSrc: "product3.jpg", description: 'Smartwatch with multiple fitness features', price: 100 },
        { imgSrc: "product4.jpg", description: 'Portable Bluetooth speaker with high bass', price: 75 }
    ];

    const cartItemsContainer = document.querySelector('.cart-items');
    const costBreakdownContainer = document.querySelector('.cost-breakdown');
    const productRecommendationsContainer = document.querySelector('.product-recommendations');

    function updateCart() {
        cartItemsContainer.innerHTML = '<h2>Your Cart Items</h2>' + cartItems.map(item => `
            <div class="cart-item">
                <img src="${item.imgSrc}" alt="${item.description}" description="${item.description}">
                <div class="item-details">
                    <p>${item.description}</p>
                    <input type="number" value="${item.quantity}" min="1" data-index="${cartItems.indexOf(item)}">
                    <p>$${item.price}</p>
                </div>
                <button data-index="${cartItems.indexOf(item)}" onclick="removeItem(${cartItems.indexOf(item)})">Remove</button>
            </div>
        `).join('');

        const totalCost = cartItems.reduce((acc, item) => acc + item.quantity * item.price, 0);
        costBreakdownContainer.innerHTML = `
            <p>Subtotal: $${totalCost}</p>
            <p>Estimated Shipping: $10</p>
            <p>Total: $${totalCost + 10}</p>
        `;
    }

    function updateRecommendations() {
        productRecommendationsContainer.innerHTML += productRecommendations.map(item => `
            <div class="recommended-product">
                <img src="${item.imgSrc}" alt="${item.description}" description="${item.description}">
                <div class="item-details">
                    <p>${item.description}</p>
                    <p>$${item.price}</p>
                </div>
                <button onclick="addToCart('${item.imgSrc}', '${item.description}', ${item.price})">Add to Cart</button>
            </div>
        `).join('');
    }

    function removeItem(index) {
        cartItems.splice(index, 1);
        updateCart();
    }

    function addToCart(imgSrc, description, price) {
        cartItems.push({ imgSrc, description, quantity: 1, price });
        updateCart();
    }

    document.querySelector('.cart-items').addEventListener('input', function(event) {
        if (event.target.type === 'number') {
            const index = event.target.getAttribute('data-index');
            cartItems[index].quantity = parseInt(event.target.value);
            updateCart();
        }
    });

    updateCart();
    updateRecommendations();
});

function saveForLater() {
    alert('Item saved for later!');
}

function applyDiscountCode() {
    alert('Discount code applied!');
}