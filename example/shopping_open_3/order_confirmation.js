// order_confirmation.js

document.addEventListener('DOMContentLoaded', function() {
    displayOrderDetails();
    displayRecommendations();
});

function displayOrderDetails() {
    const orderDetails = document.getElementById('orderDetails');
    const orderInfo = [
        { imgSrc: "phone.jpg", description: 'This is a black phone with a sleek design.' },
        { imgSrc: "headphones.jpg", description: 'This is a pair of noise-cancelling headphones.' }
    ];

    orderInfo.forEach(item => {
        const container = document.createElement('div');
        container.classList.add('order-item');

        const img = document.createElement('img');
        img.src = item.imgSrc;
        img.alt = item.description;
        container.appendChild(img);

        const desc = document.createElement('p');
        desc.textContent = item.description;
        container.appendChild(desc);

        orderDetails.appendChild(container);
    });
}

function displayRecommendations() {
    const recommendations = document.getElementById('recommendations');
    const recommendationItems = [
        { imgSrc: "smartwatch.jpg", description: 'A trendy smartwatch with multiple features.' },
        { imgSrc: "speaker.jpg", description: 'A stylish and compact wireless speaker.' }
    ];

    recommendationItems.forEach(item => {
        const container = document.createElement('div');
        container.classList.add('recommendation-item');

        const img = document.createElement('img');
        img.src = item.imgSrc;
        img.alt = item.description;
        container.appendChild(img);

        const desc = document.createElement('p');
        desc.textContent = item.description;
        container.appendChild(desc);

        recommendations.appendChild(container);
    });
}

function printReceipt() {
    window.print();
}

function viewInvoice() {
    // Logic to view or download the invoice
    alert('Invoice functionality will be implemented here.');
}