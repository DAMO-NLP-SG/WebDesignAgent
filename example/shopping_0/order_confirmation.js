document.addEventListener("DOMContentLoaded", function() {
    // Function to print receipt
    function printReceipt() {
        window.print();
    }

    // Adding product recommendations dynamically
    const recommendations = [
        { imgSrc: "product1.jpg", description: 'A great product for your needs' },
        { imgSrc: "product2.jpg", description: 'Another amazing product' },
        { imgSrc: "product3.jpg", description: 'You might like this one too' }
    ];

    const recommendationsContainer = document.getElementById("recommendationsContainer");

    recommendations.forEach(product => {
        const imgElement = document.createElement("img");
        imgElement.src = product.imgSrc;
        imgElement.alt = product.description;
        imgElement.setAttribute("description", product.description);
        recommendationsContainer.appendChild(imgElement);
    });

    // Add print receipt function to button
    document.querySelector("button[onclick='printReceipt()']").onclick = printReceipt;
});