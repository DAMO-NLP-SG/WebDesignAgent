document.addEventListener("DOMContentLoaded", function () {
    const projects = [
        { imgSrc: "product1.jpg", description: 'Description for product 1 such as a black phone', title: "Project 1" },
        { imgSrc: "product2.jpg", description: 'Description for product 2 such as a silver tablet', title: "Project 2" },
        { imgSrc: "product3.jpg", description: 'Description for product 3 such as a futuristic device', title: "Project 3" },
        // Add more projects as needed
    ];

    const projectsContainer = document.getElementById("projects-container");

    function displayProjects(filteredProjects) {
        projectsContainer.innerHTML = "";
        filteredProjects.forEach(project => {
            const projectCard = document.createElement("div");
            projectCard.className = "project-card";

            const img = document.createElement("img");
            img.src = project.imgSrc;
            img.alt = project.title;
            img.setAttribute("description", project.description);
            projectCard.appendChild(img);

            const title = document.createElement("h3");
            title.textContent = project.title;
            projectCard.appendChild(title);

            const desc = document.createElement("p");
            desc.textContent = project.description;
            projectCard.appendChild(desc);

            const tooltip = document.createElement("div");
            tooltip.className = "tooltip";
            tooltip.textContent = project.description;
            projectCard.appendChild(tooltip);

            projectsContainer.appendChild(projectCard);
        });
    }

    displayProjects(projects);

    document.getElementById("search").addEventListener("input", function (e) {
        const searchTerm = e.target.value.toLowerCase();
        const filteredProjects = projects.filter(project => 
            project.title.toLowerCase().includes(searchTerm) || 
            project.description.toLowerCase().includes(searchTerm)
        );
        displayProjects(filteredProjects);
    });
});