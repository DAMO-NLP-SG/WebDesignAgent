// order_confirmation.js

function printReceipt() {
    window.print();
}

document.addEventListener('DOMContentLoaded', () => {
    const recommendations = [
        { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone' },
        { imgSrc: "product2.jpg", description: 'Description for product 2, such as a stylish watch' },
        { imgSrc: "product3.jpg", description: 'Description for product 3, such as a modern laptop' },
        // Add more products as needed
    ];

    const recommendationsSection = document.getElementById('recommendations');
    recommendations.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.classList.add('recommendation');

        const img = document.createElement('img');
        img.src = product.imgSrc;
        img.alt = product.description;
        img.setAttribute('description', product.description);

        const p = document.createElement('p');
        p.innerText = product.description;

        productDiv.appendChild(img);
        productDiv.appendChild(p);
        recommendationsSection.appendChild(productDiv);
    });
});