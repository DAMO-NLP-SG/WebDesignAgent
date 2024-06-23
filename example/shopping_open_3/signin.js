function authenticateUser() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const feedback = document.getElementById('feedback');

    // Simple validation for demonstration
    if (username === "" || password === "") {
        feedback.textContent = "Please fill in both fields.";
        return;
    }

    // Simulate authentication (replace with real authentication logic)
    if (username === "user" && password === "password") {
        feedback.textContent = "Login successful!";
        feedback.style.color = "green";
        // Redirect to main page or user dashboard
        setTimeout(() => {
            window.location.href = "index.html";
        }, 1000);
    } else {
        feedback.textContent = "Invalid username or password.";
    }
}

function socialLogin(platform) {
    alert(`Logging in with ${platform}.`);
    // Implement social media login logic here
}