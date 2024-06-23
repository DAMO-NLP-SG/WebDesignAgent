document.addEventListener('DOMContentLoaded', function () {
    // Define the order details
    const orderDetails = {
        orderId: '123456',
        orderDate: '2023-10-01',
        totalAmount: '$150.00',
        status: 'Shipped',
        items: [
            { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone', price: '$50.00', quantity: 2 },
            { imgSrc: "product2.jpg", description: 'Description for product 2, such as a smart watch', price: '$25.00', quantity: 2 }
        ]
    };

    // Load order summary
    const orderInfo = document.getElementById('order-info');
    orderInfo.innerHTML = `
        <p>Order ID: ${orderDetails.orderId}</p>
        <p>Order Date: ${orderDetails.orderDate}</p>
        <p>Total Amount: ${orderDetails.totalAmount}</p>
        <p>Status: ${orderDetails.status}</p>
    `;

    // Load item details
    const itemsContainer = document.getElementById('items');
    orderDetails.items.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.className = 'item';
        itemElement.innerHTML = `
            <img src="${item.imgSrc}" alt="${item.description}" description="${item.description}">
            <div>
                <p>${item.description}</p>
                <p>Price: ${item.price}</p>
                <p>Quantity: ${item.quantity}</p>
            </div>
        `;
        itemsContainer.appendChild(itemElement);
    });
});

// Print invoice function
function printInvoice() {
    alert("Printing Invoice...");
}