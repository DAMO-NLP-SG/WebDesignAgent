document.addEventListener("DOMContentLoaded", function() {
    const newsFeed = document.getElementById('news-feed');

    const newsArticles = [
        { imgSrc: "demo-banner-1.jpg", description: 'Exclusive gameplay trailer released for Black Myth Wukong' },
        { imgSrc: "demo-banner-2.jpg", description: 'Developer interview: Insights on the making of Black Myth Wukong' },
        { imgSrc: "demo-banner-3.jpg", description: 'Pre-order bonuses and special editions announced' }
    ];

    newsArticles.forEach(article => {
        const newsItem = document.createElement('div');
        newsItem.classList.add('news-item');

        const img = document.createElement('img');
        img.src = article.imgSrc;
        img.alt = article.description;
        img.setAttribute('description', article.description);

        const title = document.createElement('h2');
        title.textContent = article.description;

        const description = document.createElement('p');
        description.textContent = article.description;

        const imgDescription = document.createElement('p');
        imgDescription.classList.add('description');
        imgDescription.textContent = article.description;

        newsItem.appendChild(img);
        newsItem.appendChild(title);
        newsItem.appendChild(description);
        newsItem.appendChild(imgDescription);
        newsFeed.appendChild(newsItem);
    });

    const subscribeForm = document.getElementById('subscribe-form');
    subscribeForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const feedback = document.getElementById('subscribe-feedback');
        feedback.textContent = `Subscribed with email: ${document.getElementById('email').value}`;
    });
});