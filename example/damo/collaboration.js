// collaboration.js

document.addEventListener('DOMContentLoaded', () => {
    const projects = [
        { imgSrc: 'project1.jpg', description: 'Description for Project 1' },
        { imgSrc: 'project2.jpg', description: 'Description for Project 2' }
    ];

    const partners = [
        { imgSrc: 'partner1.jpg', description: 'Description for Partner 1' },
        { imgSrc: 'partner2.jpg', description: 'Description for Partner 2' }
    ];

    function loadImages(sectionId, items) {
        const section = document.getElementById(sectionId);
        items.forEach(item => {
            const div = document.createElement('div');
            div.className = sectionId.slice(0, -1); // Remove last character 's' to get singular form
            const img = document.createElement('img');
            img.src = item.imgSrc;
            img.alt = item.description;
            img.setAttribute('description', item.description);
            const p = document.createElement('p');
            p.textContent = item.description;
            div.appendChild(img);
            div.appendChild(p);
            section.appendChild(div);
        });
    }

    loadImages('projects', projects);
    loadImages('partners', partners);

    const form = document.getElementById('collaboration-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const feedback = document.getElementById('form-feedback');
        feedback.style.display = 'block';
        form.reset();
        setTimeout(() => {
            feedback.style.display = 'none';
        }, 3000);
    });
});