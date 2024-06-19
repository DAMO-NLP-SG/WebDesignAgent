document.addEventListener('DOMContentLoaded', () => {
    const startChatButton = document.getElementById('startChat');
    const supportForm = document.getElementById('supportTicketForm');

    startChatButton.addEventListener('click', () => {
        alert('Starting live chat support...');
        // Implement actual live chat functionality
    });

    supportForm.addEventListener('submit', (event) => {
        event.preventDefault();
        alert('Support ticket submitted successfully!');
        // Implement actual support ticket submission logic
    });

    // Adding images dynamically
    const images = [
        { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone' },
        { imgSrc: "product2.jpg", description: 'Description for product 2, such as a red phone' }
    ];

    const imageContainer = document.querySelector('.image-container');
    images.forEach(image => {
        const imgElement = document.createElement('img');
        imgElement.src = image.imgSrc;
        imgElement.alt = image.description;
        imgElement.title = image.description; // Tooltip for description
        imageContainer.appendChild(imgElement);
    });
});