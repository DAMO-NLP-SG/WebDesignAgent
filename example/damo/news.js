document.addEventListener("DOMContentLoaded", function() {
    const newsContainer = document.getElementById("news-container");

    const newsItems = [
        { imgSrc: "image1.jpg", description: "Breaking News: Market hits all-time high. This is a colorful cat image." },
        { imgSrc: "image2.jpg", description: "In-Depth: The impact of climate change. This is an artistic representation of a cat in a firey background." },
        { imgSrc: "image3.jpg", description: "Expert Opinion: Trends in the tech industry. This is a vibrant image of a futuristic cat." },
        { imgSrc: "image4.jpg", description: "Breaking News: Market hits all-time high. This is a news conference image." },
        { imgSrc: "image5.jpg", description: "In-Depth: The impact of climate change. This is an image of a mythical dragon." },
        { imgSrc: "image6.jpg", description: "Expert Opinion: Trends in the tech industry. This is an image of a golden statue in a temple." }
    ];

    newsItems.forEach(item => {
        const newsItemDiv = document.createElement("div");
        newsItemDiv.className = "news-item";

        const img = document.createElement("img");
        img.src = item.imgSrc;
        img.alt = item.description;

        const desc = document.createElement("p");
        desc.textContent = item.description;

        newsItemDiv.appendChild(img);
        newsItemDiv.appendChild(desc);

        newsContainer.appendChild(newsItemDiv);
    });
});

function shareArticle(platform) {
    alert(`Sharing on ${platform} is not yet implemented.`);
}

function postComment() {
    const commentInput = document.getElementById("comment-input");
    const commentsList = document.getElementById("comments-list");

    if (commentInput.value.trim() === "") {
        alert("Comment cannot be empty.");
        return;
    }

    const comment = document.createElement("p");
    comment.textContent = commentInput.value;
    commentsList.appendChild(comment);

    commentInput.value = "";
}