document.addEventListener('DOMContentLoaded', () => {
    const orderItems = [
        { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone' },
        { imgSrc: "product2.jpg", description: 'Description for product 2, such as a pair of headphones' },
        { imgSrc: "product3.jpg", description: 'Description for product 3, such as a smartwatch' }
    ];

    const orderItemsContainer = document.getElementById('order-items');

    orderItems.forEach(item => {
        const itemElement = document.createElement('div');
        const imgElement = document.createElement('img');
        imgElement.src = item.imgSrc;
        imgElement.alt = item.description;
        itemElement.appendChild(imgElement);
        const descriptionElement = document.createElement('p');
        descriptionElement.textContent = item.description;
        itemElement.appendChild(descriptionElement);
        orderItemsContainer.appendChild(itemElement);
    });

    // Set current step in progress bar
    const currentStep = 3; // Example step
    document.getElementById(`step${currentStep}`).classList.add('active');
});

function editShippingAddress() {
    // Implement edit shipping address functionality
    alert('Edit Shipping Address clicked');
}

function editPaymentMethod() {
    // Implement edit payment method functionality
    alert('Edit Payment Method clicked');
}

function applyPromoCode() {
    // Implement apply promo code functionality
    alert('Apply Promo Code clicked');
}

function placeOrder() {
    // Implement place order functionality
    alert('Place Order clicked');
}