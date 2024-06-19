document.addEventListener("DOMContentLoaded", function() {
    // Handle updating profile picture
    document.getElementById("update-picture").addEventListener("click", function() {
        alert("Feature to update profile picture coming soon!");
    });

    // Handle editing profile
    document.getElementById("edit-profile").addEventListener("click", function() {
        window.location.href = "edit_profile.html";
    });

    // Sample order data
    const orders = [
        { orderId: "12345", product: "Product 1", status: "Delivered", imgSrc: "product1.jpg", description: "Description for product 1, such as a black phone" },
        { orderId: "67890", product: "Product 2", status: "Shipped", imgSrc: "product2.jpg", description: "Description for product 2, such as a white laptop" },
        { orderId: "11223", product: "Product 3", status: "Processing", imgSrc: "product3.jpg", description: "Description for product 3, such as wireless headphones" }
    ];

    const orderList = document.getElementById("order-list");
    orders.forEach(order => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${order.orderId}</td>
            <td>${order.product}</td>
            <td>${order.status}</td>
            <td><img src="${order.imgSrc}" alt="${order.product}" description="${order.description}" style="width: 100px; height: 100px; object-fit: cover;"></td>
        `;
        orderList.appendChild(row);
    });

    // Sample recommended products data
    const recommendedProducts = [
        { imgSrc: "product4.jpg", description: "Description for product 4, such as a smart watch" },
        { imgSrc: "product5.jpg", description: "Description for product 5, such as a gaming console" },
        { imgSrc: "product6.jpg", description: "Description for product 6, such as a digital camera" }
    ];

    const recommendedProductsContainer = document.getElementById("recommended-products");
    recommendedProducts.forEach(product => {
        const card = document.createElement("div");
        card.className = "product-card";
        card.innerHTML = `
            <img src="${product.imgSrc}" alt="${product.description}" description="${product.description}">
            <p>${product.description}</p>
        `;
        recommendedProductsContainer.appendChild(card);
    });
});