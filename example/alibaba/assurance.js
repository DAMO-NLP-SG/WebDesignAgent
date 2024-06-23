document.addEventListener('DOMContentLoaded', function () {
    const testimonials = [
        { imgSrc: "demo1.jpg", description: 'This is a testimonial from a satisfied customer.' },
        { imgSrc: "demo2.jpg", description: 'Another testimonial from a happy customer.' }
    ];

    const caseStudies = [
        { imgSrc: "case-study1.jpg", description: 'A case study exploring trade assurance benefits in a remote island project.' },
        { imgSrc: "case-study2.jpg", description: 'A case study highlighting a successful trade assurance case in a forest conservation project.' }
    ];

    function createImageElement(data) {
        const img = document.createElement('img');
        img.src = data.imgSrc;
        img.alt = data.description;
        img.setAttribute('description', data.description);
        const desc = document.createElement('p');
        desc.textContent = data.description;
        const container = document.createElement('div');
        container.appendChild(img);
        container.appendChild(desc);
        container.classList.add('interactive-item');
        return container;
    }

    function populateSection(sectionId, data) {
        const section = document.getElementById(sectionId);
        data.forEach(item => {
            const imgElement = createImageElement(item);
            section.appendChild(imgElement);
        });
    }

    populateSection('testimonials', testimonials);
    populateSection('case-studies', caseStudies);

    // Handle form submission
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');

    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();
        formMessage.classList.remove('hidden');
        contactForm.reset();
    });
});