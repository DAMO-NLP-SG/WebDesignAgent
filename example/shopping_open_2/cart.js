// Sample cart items
const cartItems = [
    { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone', price: 29.99, quantity: 1 },
    { imgSrc: "product2.jpg", description: 'Description for product 2, such as a blue laptop', price: 49.99, quantity: 2 },
];

document.addEventListener("DOMContentLoaded", () => {
    loadCartItems();
    loadRecommendedProducts();
    updateCartSummary();
});

function loadCartItems() {
    const cartItemsContainer = document.getElementById('cart-items');
    cartItemsContainer.innerHTML = '';

    cartItems.forEach((item, index) => {
        const itemElement = document.createElement('div');
        itemElement.classList.add('cart-item');
        itemElement.innerHTML = `
            <img src="${item.imgSrc}" alt="${item.description}" description="${item.description}">
            <p>${item.description}</p>
            <p>$${item.price.toFixed(2)}</p>
            <input type="number" value="${item.quantity}" min="1" onchange="updateQuantity(${index}, this.value)">
            <button onclick="removeItem(${index})">Remove</button>
            <button onclick="moveToWishlist(${index})">Move to Wishlist</button>
        `;
        cartItemsContainer.appendChild(itemElement);
    });
}

function updateQuantity(index, quantity) {
    if (quantity < 1) {
        alert('Quantity cannot be less than 1');
        return;
    }
    cartItems[index].quantity = parseInt(quantity);
    updateCartSummary();
    alert(`Quantity for ${cartItems[index].description} updated to ${quantity}`);
}

function removeItem(index) {
    const itemDescription = cartItems[index].description;
    cartItems.splice(index, 1);
    loadCartItems();
    updateCartSummary();
    alert(`${itemDescription} removed from the cart`);
}

function moveToWishlist(index) {
    const itemDescription = cartItems[index].description;
    // Implement the logic to move the item to the wishlist
    // For now, just remove the item from the cart
    cartItems.splice(index, 1);
    loadCartItems();
    updateCartSummary();
    alert(`${itemDescription} moved to the wishlist`);
}

function updateCartSummary() {
    let subtotal = 0;
    cartItems.forEach(item => {
        subtotal += item.price * item.quantity;
    });

    const shipping = subtotal > 50 ? 0 : 5; // Example shipping cost calculation
    const total = subtotal + shipping;

    document.getElementById('subtotal').textContent = `$${subtotal.toFixed(2)}`;
    document.getElementById('shipping').textContent = `$${shipping.toFixed(2)}`;
    document.getElementById('total').textContent = `$${total.toFixed(2)}`;
}

function applyDiscountCode() {
    const discountCode = document.getElementById('discount-code').value;
    // Example discount code logic
    if (discountCode === 'SAVE10') {
        alert('Discount applied: 10% off');
        const subtotal = parseFloat(document.getElementById('subtotal').textContent.slice(1));
        const discount = subtotal * 0.10;
        const newTotal = subtotal - discount + parseFloat(document.getElementById('shipping').textContent.slice(1));
        document.getElementById('total').textContent = `$${newTotal.toFixed(2)}`;
    } else {
        alert('Invalid discount code');
    }
}

function proceedToCheckout() {
    window.location.href = 'checkout.html';
}

function saveForLater() {
    alert('Items saved for later');
    // Implement save for later functionality
}

function loadRecommendedProducts() {
    const recommendedProducts = [
        { imgSrc: "product3.jpg", description: 'Recommended product 1, such as a red tablet', price: 39.99 },
        { imgSrc: "product4.jpg", description: 'Recommended product 2, such as a green smartwatch', price: 59.99 },
    ];

    const recommendationsContainer = document.getElementById('product-recommendations');
    recommendationsContainer.innerHTML = '';

    recommendedProducts.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.classList.add('recommended-item');
        itemElement.innerHTML = `
            <img src="${item.imgSrc}" alt="${item.description}" description="${item.description}">
            <p>${item.description}</p>
            <p>$${item.price.toFixed(2)}</p>
        `;
        recommendationsContainer.appendChild(itemElement);
    });
}