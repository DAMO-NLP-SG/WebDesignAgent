document.addEventListener('DOMContentLoaded', function () {
    const orderData = {
        orderId: '12345',
        orderDate: '2023-10-01',
        totalAmount: '$150.00',
        status: 'Shipped',
        items: [
            { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone', price: '$50.00', quantity: 2 },
            { imgSrc: "product2.jpg", description: 'Description for product 2, such as a white laptop', price: '$25.00', quantity: 1 }
        ],
        tracking: {
            status: "In Transit",
            estimatedDelivery: "2023-10-05"
        }
    };

    const orderDetailsElem = document.getElementById('order-details');
    orderDetailsElem.innerHTML = `
        <p>Order ID: ${orderData.orderId}</p>
        <p>Order Date: ${orderData.orderDate}</p>
        <p>Total Amount: ${orderData.totalAmount}</p>
        <p>Status: ${orderData.status}</p>
    `;

    const itemsListElem = document.getElementById('items-list');
    orderData.items.forEach(item => {
        const itemElem = document.createElement('div');
        itemElem.innerHTML = `
            <img src="${item.imgSrc}" alt="${item.description}" description="${item.description}">
            <p>${item.description}</p>
            <p>Price: ${item.price}</p>
            <p>Quantity: ${item.quantity}</p>
        `;
        itemsListElem.appendChild(itemElem);
    });

    const trackingDetailsElem = document.getElementById('tracking-details');
    trackingDetailsElem.innerHTML = `
        <p>Tracking Status: ${orderData.tracking.status}</p>
        <p>Estimated Delivery: ${orderData.tracking.estimatedDelivery}</p>
    `;

    document.querySelectorAll('.collapsible-content').forEach(section => {
        const button = document.createElement('button');
        button.textContent = 'Toggle Details';
        button.classList.add('toggle-button');
        section.parentNode.insertBefore(button, section);
        button.addEventListener('click', () => {
            section.classList.toggle('collapsed');
        });
    });
});

function confirmReorder() {
    if (confirm('Are you sure you want to reorder these items?')) {
        window.location.href = 'cart.html';
    }
}

function confirmPrintInvoice() {
    if (confirm('Are you sure you want to print the invoice?')) {
        window.print();
    }
}