// contact.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('interactive-form');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        let isValid = validateForm();
        
        if(isValid) {
            alert('Form submitted successfully!');
            form.reset();
        }
    });
    
    function validateForm() {
        let name = document.getElementById('name').value;
        let email = document.getElementById('email').value;
        let message = document.getElementById('message').value;
        
        if(name === '' || email === '' || message === '') {
            alert('All fields are required.');
            return false;
        }
        
        let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if(!emailPattern.test(email)) {
            alert('Please enter a valid email address.');
            return false;
        }
        
        return true;
    }

    // Adding Images Dynamically
    const images = [
        { imgSrc: "promo1.jpg", description: "This is a promotional banner for Black Myth Wukong" },
        { imgSrc: "promo2.jpg", description: "This is another promotional banner for our upcoming AAA game" }
    ];

    const promotionalImagesSection = document.getElementById('promotional-images');
    images.forEach(image => {
        const imgElement = document.createElement('img');
        imgElement.src = image.imgSrc;
        imgElement.alt = image.description;
        imgElement.setAttribute('description', image.description);
        promotionalImagesSection.appendChild(imgElement);
    });
});

// Google Maps Integration
function initMap() {
    var officeLocation = { lat: -34.397, lng: 150.644 }; // Replace with actual location
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 8,
        center: officeLocation
    });
    var marker = new google.maps.Marker({
        position: officeLocation,
        map: map
    });
}

// Load Google Maps script
let script = document.createElement('script');
script.src = `https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap`;
script.async = true;
script.defer = true;
document.head.appendChild(script);