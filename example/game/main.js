document.addEventListener('DOMContentLoaded', () => {
    const games = [
        { imgSrc: "game1.jpg", description: "Gameplay screenshot of Game 1", text: "The latest action-packed adventure." },
        { imgSrc: "game2.jpg", description: "Gameplay screenshot of Game 2", text: "An epic journey awaits." },
        { imgSrc: "game3.jpg", description: "Gameplay screenshot of Game 3", text: "Experience the thrill of the battle." }
    ];

    const highlightsSection = document.querySelector('.highlights');
    games.forEach(game => {
        const gameDiv = document.createElement('div');
        gameDiv.className = 'game';
        
        const img = document.createElement('img');
        img.src = game.imgSrc;
        img.alt = game.description;
        img.description = game.description;

        const p = document.createElement('p');
        p.textContent = game.text;

        gameDiv.appendChild(img);
        gameDiv.appendChild(p);
        highlightsSection.appendChild(gameDiv);
    });

    const newsItems = [
        { imgSrc: "news1.jpg", description: "News about the latest game release", text: "New game release: Black Myth Wukong" },
        { imgSrc: "news2.jpg", description: "News about company achievements", text: "Company wins multiple awards" }
    ];

    const newsSection = document.querySelector('.news');
    newsItems.forEach(news => {
        const newsDiv = document.createElement('div');
        newsDiv.className = 'news-item';
        
        const img = document.createElement('img');
        img.src = news.imgSrc;
        img.alt = news.description;
        img.description = news.description;

        const p = document.createElement('p');
        p.textContent = news.text;

        newsDiv.appendChild(img);
        newsDiv.appendChild(p);
        newsSection.appendChild(newsDiv);
    });

    // Add more interactive elements as needed
});