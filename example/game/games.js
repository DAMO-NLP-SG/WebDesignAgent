document.addEventListener('DOMContentLoaded', () => {
    const images = [
        { imgSrc: 'black_myth_wukong.jpg', description: 'Black Myth Wukong - An epic journey inspired by the legendary Chinese novel Journey to the West.', video: 'black_myth_wukong_trailer.mp4' },
        { imgSrc: 'game2.jpg', description: 'Action Game 2 - Battle through futuristic landscapes with intense action.', video: 'game2_trailer.mp4' },
        { imgSrc: 'game3.jpg', description: 'Action Game 3 - Fight mythical creatures in a fantasy world.', video: 'game3_trailer.mp4' },
        // Add more images as needed
    ];

    const gallery = document.getElementById('gallery');

    images.forEach(image => {
        const galleryItem = document.createElement('div');
        galleryItem.className = 'gallery-item';

        const imgElement = document.createElement('img');
        imgElement.src = image.imgSrc;
        imgElement.alt = image.description;
        imgElement.title = image.description;

        const descriptionElement = document.createElement('p');
        descriptionElement.textContent = image.description;

        const buttonElement = document.createElement('button');
        buttonElement.textContent = 'Watch Trailer';
        buttonElement.onclick = () => {
            openModal(image.video);
        };

        galleryItem.appendChild(imgElement);
        galleryItem.appendChild(descriptionElement);
        galleryItem.appendChild(buttonElement);
        gallery.appendChild(galleryItem);
    });

    // Modal functionality
    const modal = document.createElement('div');
    modal.className = 'modal';
    modal.id = 'videoModal';
    const modalContent = document.createElement('div');
    modalContent.className = 'modal-content';
    const closeButton = document.createElement('span');
    closeButton.className = 'close';
    closeButton.innerHTML = '&times;';
    closeButton.onclick = closeModal;
    modalContent.appendChild(closeButton);
    modal.appendChild(modalContent);
    document.body.appendChild(modal);
});

function openModal(videoSrc) {
    const modal = document.getElementById('videoModal');
    const modalContent = modal.querySelector('.modal-content');
    const videoElement = document.createElement('video');
    videoElement.src = videoSrc;
    videoElement.controls = true;
    videoElement.autoplay = true;
    modalContent.appendChild(videoElement);
    modal.style.display = 'block';
}

function closeModal() {
    const modal = document.getElementById('videoModal');
    modal.style.display = 'none';
    const videoElement = modal.querySelector('video');
    if (videoElement) {
        videoElement.pause();
        videoElement.remove();
    }
}

window.onclick = function(event) {
    const modal = document.getElementById('videoModal');
    if (event.target === modal) {
        closeModal();
    }
};