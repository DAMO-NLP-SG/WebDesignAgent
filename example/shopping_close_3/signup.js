function submitForm() {
    // Form validation logic
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Simple validation checks
    if (username === '' || email === '' || password === '' || confirmPassword === '') {
        alert('All fields are required.');
        return;
    }

    if (password !== confirmPassword) {
        alert('Passwords do not match.');
        return;
    }

    // Assuming validation passes, submit the form
    alert('Form submitted successfully!');
    // Add code to handle actual form submission, e.g., via AJAX
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('signupForm');

    form.addEventListener('input', (event) => {
        const target = event.target;
        const tooltip = target.nextElementSibling;

        if (tooltip && tooltip.classList.contains('tooltip')) {
            tooltip.style.display = target.value ? 'none' : 'block';
        }
    });

    const images = [
        { imgSrc: "product1.jpg", description: "Description for product 1, such as a black phone" },
        { imgSrc: "product2.jpg", description: "Description for product 2, such as a red dress" }
    ];

    const productSection = document.querySelector('.product-section');
    productSection.innerHTML = ''; // Clear existing content

    images.forEach(image => {
        const imgElement = document.createElement('img');
        imgElement.src = image.imgSrc;
        imgElement.alt = image.description;
        imgElement.classList.add('product-image');
        imgElement.setAttribute('description', image.description);

        const galleryDiv = document.createElement('div');
        galleryDiv.classList.add('product-gallery');
        galleryDiv.appendChild(imgElement);

        const descriptionP = document.createElement('p');
        descriptionP.textContent = image.description;
        galleryDiv.appendChild(descriptionP);

        productSection.appendChild(galleryDiv);
    });
});