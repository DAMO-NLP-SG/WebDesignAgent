// social_responsibility.js
document.addEventListener('DOMContentLoaded', () => {
    const initiatives = [
        { imgSrc: 'initiative1.jpg', description: 'Description for initiative 1' },
        { imgSrc: 'initiative2.jpg', description: 'Description for initiative 2' }
    ];

    const initiativeContainer = document.querySelector('.initiatives');
    initiatives.forEach((initiative, index) => {
        const initiativeDiv = document.createElement('div');
        initiativeDiv.className = 'initiative';
        initiativeDiv.id = `initiative${index + 1}`;

        const img = document.createElement('img');
        img.src = initiative.imgSrc;
        img.alt = `Initiative ${index + 1}`;
        img.setAttribute('description', initiative.description);

        const p = document.createElement('p');
        p.textContent = initiative.description;

        initiativeDiv.appendChild(img);
        initiativeDiv.appendChild(p);
        initiativeContainer.appendChild(initiativeDiv);
    });
});