document.addEventListener("DOMContentLoaded", function() {
    const orderDetails = `
        <p>Order ID: 123456</p>
        <p>Items: 3</p>
        <p>Total: $150</p>
    `;
    const deliveryDetails = `
        <p>Address: 123 Main St, Anytown, USA</p>
        <p>Estimated Delivery: 3-5 business days</p>
    `;
    const paymentDetails = `
        <p>Payment Method: Credit Card</p>
        <p>Transaction ID: 789012</p>
    `;

    document.getElementById("order-details").innerHTML = orderDetails;
    document.getElementById("delivery-details").innerHTML = deliveryDetails;
    document.getElementById("payment-details").innerHTML = paymentDetails;

    const recommendations = [
        {imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone'},
        {imgSrc: "product2.jpg", description: 'Description for product 2, such as a red blender'},
        {imgSrc: "product3.jpg", description: 'Description for product 3, such as a white coffee maker'}
    ];

    const recommendationImages = document.getElementById("recommendation-images");
    recommendations.forEach(product => {
        const imgElement = document.createElement("img");
        imgElement.src = product.imgSrc;
        imgElement.alt = product.description;
        imgElement.title = product.description;
        recommendationImages.appendChild(imgElement);
    });
});

function printReceipt() {
    window.print();
}