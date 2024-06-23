// cart.js

document.addEventListener('DOMContentLoaded', function () {
    const cartItems = [
        { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone', price: 10.99, quantity: 1 },
        { imgSrc: "product2.jpg", description: 'Description for product 2, such as a modern lamp', price: 15.99, quantity: 2 }
    ];
    const cartItemsContainer = document.getElementById('cart-items');
    const summaryDetailsContainer = document.getElementById('summary-details');

    function renderCartItems() {
        cartItemsContainer.innerHTML = `
            <h2>Your Items</h2>
        `;
        cartItems.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.className = 'cart-item';
            itemElement.innerHTML = `
                <img src="${item.imgSrc}" alt="${item.description}" title="${item.description}">
                <p class="description">${item.description}</p>
                <p>Price: $${item.price.toFixed(2)}</p>
                <input type="number" value="${item.quantity}" min="1" data-index="${cartItems.indexOf(item)}">
                <button class="remove-btn" onclick="removeItem(${cartItems.indexOf(item)})">Remove</button>
                <button class="wishlist-btn" onclick="moveToWishlist(${cartItems.indexOf(item)})">Move to Wishlist</button>
            `;
            cartItemsContainer.appendChild(itemElement);
        });
    }

    function renderSummary() {
        const total = cartItems.reduce((acc, item) => acc + item.price * item.quantity, 0);
        const estimatedShipping = total > 50 ? 0 : 5; // Free shipping for orders over $50
        summaryDetailsContainer.innerHTML = `
            <p>Total Cost: $${total.toFixed(2)}</p>
            <p>Estimated Shipping: $${estimatedShipping.toFixed(2)}</p>
        `;
    }

    function updateQuantity(index, quantity) {
        cartItems[index].quantity = quantity;
        renderSummary();
    }

    function removeItem(index) {
        cartItems.splice(index, 1);
        renderCartItems();
        renderSummary();
    }

    function moveToWishlist(index) {
        alert(`Moved ${cartItems[index].description} to Wishlist!`);
        removeItem(index);
    }

    document.getElementById('cart-items').addEventListener('input', function (event) {
        if (event.target.type === 'number') {
            const index = event.target.dataset.index;
            const quantity = parseInt(event.target.value, 10);
            if (quantity > 0) {
                updateQuantity(index, quantity);
            }
        }
    });

    renderCartItems();
    renderSummary();
});

function saveForLater() {
    alert('Items saved for later!');
}

function applyDiscountCode() {
    let discountCode = document.getElementById('discount-code').value;
    if (discountCode === 'DISCOUNT10') {
        alert('Discount code applied successfully!');
    } else {
        alert('Invalid discount code!');
    }
}

function checkout() {
    window.location.href = 'checkout.html';
}

function addToCart(productId) {
    alert(`Product ${productId} added to cart!`);
    // Implement the logic to add the product to the cart here.
}