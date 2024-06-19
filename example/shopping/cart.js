document.addEventListener('DOMContentLoaded', function() {
    const cartItems = [
        { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone', price: 20.00, quantity: 1 },
        { imgSrc: "product2.jpg", description: 'Description for product 2, such as a small cube', price: 15.00, quantity: 2 }
    ];

    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');

    function renderCartItems() {
        cartItemsContainer.innerHTML = '';
        let total = 0;

        cartItems.forEach((item, index) => {
            const cartItemElement = document.createElement('div');
            cartItemElement.className = 'cart-item';

            cartItemElement.innerHTML = `
                <img src="${item.imgSrc}" alt="${item.description}" description="${item.description}">
                <div class="cart-item-details">
                    <p>${item.description}</p>
                    <p>$${item.price.toFixed(2)}</p>
                    <div class="cart-item-quantity">
                        <button onclick="updateQuantity(${index}, -1)">-</button>
                        <span>${item.quantity}</span>
                        <button onclick="updateQuantity(${index}, 1)">+</button>
                    </div>
                    <p class="description">${item.description}</p>
                </div>
                <button class="remove-button" onclick="removeItem(${index})">Remove</button>
            `;

            cartItemsContainer.appendChild(cartItemElement);
            total += item.price * item.quantity;
        });

        cartTotalElement.textContent = total.toFixed(2);
    }

    window.updateQuantity = function(index, change) {
        cartItems[index].quantity += change;
        if (cartItems[index].quantity < 1) {
            cartItems[index].quantity = 1;
        }
        renderCartItems();
    }

    window.removeItem = function(index) {
        cartItems.splice(index, 1);
        renderCartItems();
    }

    renderCartItems();

    document.getElementById('checkout-button').addEventListener('click', function() {
        window.location.href = 'checkout.html';
    });

    document.getElementById('apply-discount').addEventListener('click', function() {
        const discountCode = document.getElementById('discount-code').value;
        applyDiscount(discountCode);
    });

    function applyDiscount(code) {
        const discount = (code === "DISCOUNT10") ? 0.1 : 0;
        const total = parseFloat(cartTotalElement.textContent);
        const newTotal = total * (1 - discount);
        cartTotalElement.textContent = newTotal.toFixed(2);

        if (discount > 0) {
            alert("Discount applied successfully!");
        } else {
            alert("Invalid discount code.");
        }
    }
});