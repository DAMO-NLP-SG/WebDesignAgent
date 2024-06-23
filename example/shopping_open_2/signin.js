// signin.js
function authenticateUser() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // Input validation
    if (username === "" || password === "") {
        alert("Please fill in both fields.");
        return;
    }
    
    // Simulate authentication process
    if (username === "testuser" && password === "password") {
        alert("Login successful!");
        // Redirect to main page
        window.location.href = "index.html";
    } else {
        alert("Invalid username or password.");
    }
}

function socialLogin(platform) {
    alert(`Sign in with ${platform} clicked!`);
}

// Example: Adding an image dynamically
const images = [
    { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone' },
    { imgSrc: "product2.jpg", description: 'Description for product 2, such as a white laptop' }
];

images.forEach(img => {
    const imgElement = document.createElement('img');
    imgElement.src = img.imgSrc;
    imgElement.alt = img.description;
    imgElement.className = 'dynamic-img';
    document.querySelector('.dynamic-image-container').appendChild(imgElement);
});

// Set image size using CSS
const style = document.createElement('style');
style.innerHTML = `
    .dynamic-img {
        width: 150px;
        height: auto;
        margin: 10px;
        transition: transform 0.3s;
    }
    .dynamic-img:hover {
        transform: scale(1.05);
    }
`;
document.head.appendChild(style);