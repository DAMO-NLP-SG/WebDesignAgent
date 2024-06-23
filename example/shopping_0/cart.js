document.addEventListener('DOMContentLoaded', (event) => {
    const cartItems = [
        { imgSrc: "product1.jpg", description: "Description for product 1", quantity: 1, price: 29.99 },
        { imgSrc: "product2.jpg", description: "Description for product 2", quantity: 2, price: 19.99 },
        // Add more products as needed
    ];

    const cartItemsContainer = document.getElementById('cart-items-container');
    const costSummary = document.getElementById('cost-summary');

    function renderCartItems() {
        cartItemsContainer.innerHTML = '';
        cartItems.forEach((item, index) => {
            const cartItem = document.createElement('div');
            cartItem.classList.add('cart-item');
            cartItem.innerHTML = `
                <img src="${item.imgSrc}" alt="${item.description}" description="${item.description}">
                <p>${item.description}</p>
                <input type="number" value="${item.quantity}" min="1" onchange="updateQuantity(${index}, this.value)">
                <p>$${item.price.toFixed(2)}</p>
                <button onclick="removeItem(${index})">Remove</button>
            `;
            cartItemsContainer.appendChild(cartItem);
        });
        updateTotalCost();
    }

    function updateTotalCost() {
        const totalCost = cartItems.reduce((total, item) => total + item.quantity * item.price, 0).toFixed(2);
        costSummary.innerHTML = `<p>Total Cost: $${totalCost}</p>`;
    }

    window.updateQuantity = (index, quantity) => {
        cartItems[index].quantity = parseInt(quantity, 10);
        renderCartItems();
    };

    window.removeItem = (index) => {
        cartItems.splice(index, 1);
        renderCartItems();
    };

    window.applyDiscountCode = () => {
        const discountCode = document.getElementById('discount-code').value;
        // Implement discount code logic here
        alert(`Discount code ${discountCode} applied!`);
    };

    window.proceedToCheckout = () => {
        window.location.href = 'checkout.html';
    };

    window.continueShopping = () => {
        window.location.href = 'products.html';
    };

    window.saveForLater = () => {
        alert('Items saved for later!');
    };

    renderCartItems();
});