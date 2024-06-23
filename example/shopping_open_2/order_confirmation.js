document.addEventListener("DOMContentLoaded", function() {
    const recommendations = [
        { imgSrc: "product1.jpg", description: "Description for product 1, such as a black phone" },
        { imgSrc: "product2.jpg", description: "Description for product 2, such as a white tablet" },
        { imgSrc: "product3.jpg", description: "Description for product 3, such as a smart watch" },
        { imgSrc: "product4.jpg", description: "Description for product 4, such as a pair of headphones" },
        { imgSrc: "product5.jpg", description: "Description for product 5, such as a gaming console" }
    ];

    const recommendationsContainer = document.getElementById('recommendations');
    recommendations.forEach(product => {
        const div = document.createElement('div');
        div.classList.add('recommendation-item');

        const img = document.createElement('img');
        img.src = product.imgSrc;
        img.alt = product.description;

        const desc = document.createElement('p');
        desc.innerText = product.description;

        div.appendChild(img);
        div.appendChild(desc);
        recommendationsContainer.appendChild(div);
    });
});

function printReceipt() {
    alert("Printing receipt...");
    window.print();
}