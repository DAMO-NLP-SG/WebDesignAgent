// Function to handle the editing of the shipping address
function editShippingAddress() {
    // Add your logic here for editing the shipping address
    alert("Edit Shipping Address Clicked");
}

// Function to handle the editing of the payment method
function editPaymentMethod() {
    // Add your logic here for editing the payment method
    alert("Edit Payment Method Clicked");
}

// Function to apply promo code
function applyPromoCode() {
    // Add your logic here for applying the promo code
    alert("Apply Promo Code Clicked");
}

// Function to place the order
function placeOrder() {
    // Add your logic here for placing the order
    alert("Place Order Clicked");
}

// Function to navigate to a specific step
function navigateToStep(stepNumber) {
    const steps = document.querySelectorAll(".progress-bar .step");
    steps.forEach((step, index) => {
        if (index < stepNumber) {
            step.classList.add("active");
        } else {
            step.classList.remove("active");
        }
    });

    const sections = document.querySelectorAll("section");
    sections.forEach((section, index) => {
        if (index === stepNumber - 1) {
            section.style.display = "block";
        } else {
            section.style.display = "none";
        }
    });
}

// Sample product images and descriptions
const products = [
    { imgSrc: "product1.jpg", description: "Description for product 1, such as a black phone" },
    { imgSrc: "product2.jpg", description: "Description for product 2, such as a white bottle" },
    { imgSrc: "product3.jpg", description: "Description for product 3, such as a black camera" }
];

// Function to dynamically populate order items
function populateOrderItems() {
    const orderItemsContainer = document.querySelector(".order-items");
    products.forEach(product => {
        const itemContainer = document.createElement("div");
        itemContainer.classList.add("item");

        const imgElement = document.createElement("img");
        imgElement.src = product.imgSrc;
        imgElement.alt = product.description;
        itemContainer.appendChild(imgElement);

        const descriptionElement = document.createElement("p");
        descriptionElement.textContent = product.description;
        itemContainer.appendChild(descriptionElement);

        orderItemsContainer.appendChild(itemContainer);
    });

    // Update total price and shipping cost
    document.getElementById("totalPrice").textContent = "$100.00"; // Sample total price
    document.getElementById("shippingCost").textContent = "$10.00"; // Sample shipping cost
}

// Populate order items on page load
window.onload = function() {
    populateOrderItems();
    navigateToStep(1); // Start with the first step
};