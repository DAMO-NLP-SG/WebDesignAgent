document.addEventListener('DOMContentLoaded', function () {
    const orderDetails = {
        imgSrc: "product1.jpg",
        description: 'Description for product 1, such as a black phone',
        productName: 'Sample Product 1',
        quantity: 1,
        price: 10.00,
        totalCost: 10.00,
        paymentMethod: 'Credit Card',
        estimatedDeliveryDate: '2023-10-15',
        trackingInfo: '123456789'
    };

    const orderDetailsContainer = document.getElementById('order-details');

    const orderItemHTML = `
        <div class="order-item">
            <img src="${orderDetails.imgSrc}" alt="Product 1" class="product-img" description="${orderDetails.description}">
            <p>Product Name: ${orderDetails.productName}</p>
            <p>Quantity: ${orderDetails.quantity}</p>
            <p>Price: $${orderDetails.price.toFixed(2)}</p>
        </div>
    `;

    const orderSummaryHTML = `
        <div class="order-summary-details">
            <p>Total Cost: $${orderDetails.totalCost.toFixed(2)}</p>
            <p>Payment Method: ${orderDetails.paymentMethod}</p>
            <p>Estimated Delivery Date: ${orderDetails.estimatedDeliveryDate}</p>
            <p>Tracking Information: ${orderDetails.trackingInfo}</p>
        </div>
    `;

    orderDetailsContainer.innerHTML = orderItemHTML + orderSummaryHTML;

    // Loading animation
    document.body.classList.add('loading');
    setTimeout(() => {
        document.body.classList.remove('loading');
    }, 1000);
});

function redirectToProducts() {
    window.location.href = 'products.html';
}

function trackOrder() {
    alert("Tracking feature coming soon!");
}

function contactSupport() {
    window.location.href = 'support.html';
}