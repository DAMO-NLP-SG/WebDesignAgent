// Sample data for cart items
const cartItems = [
    {imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone', price: 29.99},
    {imgSrc: "product2.jpg", description: 'Description for product 2, such as a white phone', price: 49.99},
];

// Function to render cart items
function renderCartItems() {
    const cartItemsContainer = document.getElementById('cartItems');
    cartItems.forEach(item => {
        const cartItemDiv = document.createElement('div');
        cartItemDiv.classList.add('cart-item');

        const img = document.createElement('img');
        img.src = item.imgSrc;
        img.alt = item.description;
        img.setAttribute('description', item.description);
        
        const description = document.createElement('p');
        description.textContent = item.description;

        const price = document.createElement('p');
        price.textContent = `$${item.price.toFixed(2)}`;

        cartItemDiv.appendChild(img);
        cartItemDiv.appendChild(description);
        cartItemDiv.appendChild(price);
        
        cartItemsContainer.appendChild(cartItemDiv);
    });
}

// Function to update order summary
function updateOrderSummary() {
    const orderSummaryContainer = document.getElementById('orderSummary');
    orderSummaryContainer.innerHTML = ""; // Clear previous content

    let total = 0;
    cartItems.forEach(item => {
        const summaryItemDiv = document.createElement('div');
        summaryItemDiv.classList.add('summary-item');

        const img = document.createElement('img');
        img.src = item.imgSrc;
        img.alt = item.description;
        img.setAttribute('description', item.description);

        const description = document.createElement('p');
        description.textContent = item.description;

        const price = document.createElement('p');
        price.textContent = `$${item.price.toFixed(2)}`;

        total += item.price;

        summaryItemDiv.appendChild(img);
        summaryItemDiv.appendChild(description);
        summaryItemDiv.appendChild(price);

        orderSummaryContainer.appendChild(summaryItemDiv);
    });

    const totalDiv = document.createElement('div');
    totalDiv.classList.add('total');
    totalDiv.textContent = `Total: $${total.toFixed(2)}`;
    orderSummaryContainer.appendChild(totalDiv);
}

// Function to apply discount code
function applyDiscount() {
    const discountCode = document.getElementById('discountCode').value;
    // Apply discount logic here
    const feedback = document.getElementById('discountFeedback');
    feedback.textContent = 'Discount code applied: ' + discountCode;
    feedback.classList.remove('hidden');
    
    // Example: apply 10% discount
    const discount = 0.1;
    cartItems.forEach(item => {
        item.price = item.price * (1 - discount);
    });
    updateOrderSummary();
}

// Function to place the order
function placeOrder() {
    // Validate forms and place order logic
    alert('Order placed successfully!');
    window.location.href = 'confirmation.html';
}

// Initialize page
document.addEventListener('DOMContentLoaded', () => {
    renderCartItems();
    updateOrderSummary();
});