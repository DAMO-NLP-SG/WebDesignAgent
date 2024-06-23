document.addEventListener('DOMContentLoaded', function() {
    const orderItems = [
        { imgSrc: "product1.jpg", description: 'Description for product 1', name: 'Product 1', price: '$10.00', status: 'Shipped' },
        // Add more products as needed
    ];

    const orderDetailsSection = document.querySelector('.order-details');

    orderItems.forEach(item => {
        const orderItemDiv = document.createElement('div');
        orderItemDiv.classList.add('order-item');

        const img = document.createElement('img');
        img.src = item.imgSrc;
        img.alt = item.name;
        img.description = item.description;
        orderItemDiv.appendChild(img);

        const itemInfoDiv = document.createElement('div');
        itemInfoDiv.classList.add('item-info');

        const itemName = document.createElement('h2');
        itemName.textContent = item.name;
        itemInfoDiv.appendChild(itemName);

        const itemPrice = document.createElement('p');
        itemPrice.textContent = `Price: ${item.price}`;
        itemInfoDiv.appendChild(itemPrice);

        const itemStatus = document.createElement('p');
        itemStatus.textContent = `Status: ${item.status}`;
        itemInfoDiv.appendChild(itemStatus);

        const viewProductButton = document.createElement('button');
        viewProductButton.textContent = 'View Product';
        viewProductButton.onclick = function() {
            location.href = 'product_detail.html';
        };
        itemInfoDiv.appendChild(viewProductButton);

        orderItemDiv.appendChild(itemInfoDiv);
        orderDetailsSection.appendChild(orderItemDiv);
    });
});

function printInvoice() {
    window.print();
}