document.addEventListener('DOMContentLoaded', () => {
    const teamContainer = document.getElementById('team-container');

    const teamMembers = [
        { imgSrc: 'team1.jpg', description: 'John Doe - Lead Developer' },
        { imgSrc: 'team2.jpg', description: 'Jane Smith - Art Director' },
        { imgSrc: 'team3.jpg', description: 'Samuel Green - Game Designer' },
        { imgSrc: 'team4.jpg', description: 'Emily Blue - Sound Engineer' }
    ];

    teamMembers.forEach(member => {
        const memberDiv = document.createElement('div');
        memberDiv.classList.add('team-member');

        const img = document.createElement('img');
        img.src = member.imgSrc;
        img.alt = member.description;
        img.setAttribute('description', member.description);

        const descriptionDiv = document.createElement('div');
        descriptionDiv.classList.add('description');
        descriptionDiv.textContent = member.description;

        memberDiv.appendChild(img);
        memberDiv.appendChild(descriptionDiv);
        teamContainer.appendChild(memberDiv);
    });
});