// about_us.js

document.addEventListener('DOMContentLoaded', function() {
    const timelineContainer = document.getElementById('timeline-container');
    const teamContainer = document.getElementById('team-container');

    // Timeline Data
    const timelineEvents = [
        { date: '2000', description: 'Company founded', imgSrc: 'event1.jpg', imgDescription: 'Company logo' },
        { date: '2005', description: 'First major product launch', imgSrc: 'event2.jpg', imgDescription: 'Product launch event' },
        { date: '2010', description: 'Global expansion begins', imgSrc: 'event3.jpg', imgDescription: 'Global map with expansion marks' },
        { date: '2020', description: 'Reached 1 million customers', imgSrc: 'event4.jpg', imgDescription: 'Celebration event for reaching 1 million customers' },
    ];

    // Team Members Data
    const teamMembers = [
        { imgSrc: 'team1.jpg', name: 'John Doe', role: 'CEO', description: 'John has over 20 years of experience...' },
        { imgSrc: 'team2.jpg', name: 'Jane Smith', role: 'CTO', description: 'Jane is a technology enthusiast with...' },
        { imgSrc: 'team3.jpg', name: 'Mike Johnson', role: 'CFO', description: 'Mike has a strong background in finance...' },
    ];

    // Populate Timeline
    timelineEvents.forEach(event => {
        const eventDiv = document.createElement('div');
        eventDiv.classList.add('timeline-event');
        eventDiv.innerHTML = `
            <img src="${event.imgSrc}" alt="${event.date}" description="${event.imgDescription}" class="timeline-image">
            <div class="timeline-event-content">
                <h3>${event.date}</h3>
                <p>${event.description}</p>
            </div>
        `;
        timelineContainer.appendChild(eventDiv);
    });

    // Populate Team Members
    teamMembers.forEach(member => {
        const memberDiv = document.createElement('div');
        memberDiv.classList.add('team-member');
        memberDiv.innerHTML = `
            <img src="${member.imgSrc}" alt="${member.name}" description="${member.description}" class="team-image">
            <div>
                <h3>${member.name}</h3>
                <p>${member.role}</p>
                <div class="team-member-details">${member.description}</div>
            </div>
        `;
        memberDiv.addEventListener('click', () => {
            const details = memberDiv.querySelector('.team-member-details');
            details.style.display = details.style.display === 'block' ? 'none' : 'block';
        });
        teamContainer.appendChild(memberDiv);
    });
});