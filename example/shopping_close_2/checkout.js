// checkout.js
document.addEventListener('DOMContentLoaded', function() {
  // Handle address input, payment processing, order review, form validation, and progress tracking.
  
  function editShippingAddress() {
    // Logic to edit shipping address
  }
  
  function editPaymentMethod() {
    // Logic to edit payment method
  }
  
  function applyPromoCode() {
    // Logic to apply promo code
  }
  
  function placeOrder() {
    // Logic to place the order
  }
  
  // Form validation
  const shippingForm = document.getElementById('shipping-form');
  const paymentForm = document.getElementById('payment-form');

  // Add event listeners for form validation
  shippingForm.addEventListener('submit', validateShippingForm);
  paymentForm.addEventListener('submit', validatePaymentForm);
  
  function validateShippingForm(event) {
    event.preventDefault();
    // Validation logic for shipping form
  }
  
  function validatePaymentForm(event) {
    event.preventDefault();
    // Validation logic for payment form
  }
  
  // Progress bar tracking
  const steps = document.querySelectorAll('.progress-bar .step');

  function updateProgressBar(currentStep) {
    steps.forEach((step, index) => {
      if (index <= currentStep) {
        step.classList.add('active');
      } else {
        step.classList.remove('active');
      }
    });
  }

  // Initialize progress bar
  updateProgressBar(0);

  // Add images and descriptions dynamically
  const orderItems = document.getElementById('order-items');
  const products = [
    {imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone'},
    {imgSrc: "product2.jpg", description: 'Description for product 2, such as a red laptop'}
  ];

  products.forEach(product => {
    const imgElement = document.createElement('img');
    imgElement.src = product.imgSrc;
    imgElement.alt = product.description;
    imgElement.classList.add('order-image');

    const descElement = document.createElement('p');
    descElement.textContent = product.description;
    descElement.classList.add('description');

    const productContainer = document.createElement('div');
    productContainer.classList.add('product-container');
    productContainer.appendChild(imgElement);
    productContainer.appendChild(descElement);

    orderItems.appendChild(productContainer);
  });
});