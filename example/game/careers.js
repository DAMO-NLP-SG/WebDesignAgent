document.addEventListener('DOMContentLoaded', () => {
    const jobData = [
        {imgSrc: "job1.jpg", description: 'Description for Senior Game Developer', title: 'Senior Game Developer', location: 'New York, NY'},
        {imgSrc: "job2.jpg", description: 'Description for 3D Artist', title: '3D Artist', location: 'San Francisco, CA'},
        {imgSrc: "job3.jpg", description: 'Description for Game Designer', title: 'Game Designer', location: 'Austin, TX'}
    ];

    const jobContainer = document.getElementById('job-container');
    const positionSelect = document.getElementById('position');

    jobData.forEach(job => {
        const jobItem = document.createElement('div');
        jobItem.className = 'job-item';

        const img = document.createElement('img');
        img.src = job.imgSrc;
        img.alt = job.title;
        img.setAttribute('description', job.description);

        const title = document.createElement('h3');
        title.textContent = job.title;

        const location = document.createElement('p');
        location.textContent = `Location: ${job.location}`;

        jobItem.appendChild(img);
        jobItem.appendChild(title);
        jobItem.appendChild(location);

        jobContainer.appendChild(jobItem);

        const option = document.createElement('option');
        option.value = job.title;
        option.textContent = job.title;
        positionSelect.appendChild(option);
    });

    const form = document.getElementById('job-application-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Application submitted successfully!');
        form.reset();
    });
});