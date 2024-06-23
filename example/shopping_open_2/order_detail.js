document.addEventListener('DOMContentLoaded', function () {
    const items = [
        { imgSrc: "product1.jpg", description: 'Description for product 1, such as a black phone' },
        { imgSrc: "product2.jpg", description: 'Description for product 2, such as a white laptop' }
        // Add more items as needed
    ];

    const itemDetailsSection = document.getElementById('items-container');

    if (items.length === 0) {
        document.getElementById('items-container').innerHTML = "<p>No items in this order.</p>";
    } else {
        items.forEach(item => {
            const itemDiv = document.createElement('div');
            itemDiv.className = 'item';

            const img = document.createElement('img');
            img.src = item.imgSrc;
            img.alt = item.description;
            img.title = item.description; // Tooltip

            const itemInfoDiv = document.createElement('div');
            itemInfoDiv.className = 'item-info';

            const descriptionP = document.createElement('p');
            descriptionP.textContent = item.description;

            itemInfoDiv.appendChild(descriptionP);
            itemDiv.appendChild(img);
            itemDiv.appendChild(itemInfoDiv);

            itemDetailsSection.appendChild(itemDiv);
        });
    }

    // Implement search functionality
    document.getElementById('search').addEventListener('input', function (e) {
        const searchTerm = e.target.value.toLowerCase();
        const items = document.querySelectorAll('.item');
        items.forEach(item => {
            const description = item.querySelector('.item-info p').textContent.toLowerCase();
            if (description.includes(searchTerm)) {
                item.style.display = 'flex';
            } else {
                item.style.display = 'none';
            }
        });
    });
});

function printInvoice() {
    window.print();
}