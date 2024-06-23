document.addEventListener("DOMContentLoaded", () => {
    const items = [
        { imgSrc: "product1.jpg", description: "A sleek and stylish smartwatch with various features." },
        { imgSrc: "product2.jpg", description: "A premium skincare product for a glowing complexion." },
        { imgSrc: "product3.jpg", description: "Innovative product packaging for various items." },
        // Add more items as needed
    ];

    const itemContainer = document.getElementById('item-container');
    items.forEach(item => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'item';
        
        const img = document.createElement('img');
        img.src = item.imgSrc;
        img.alt = item.description;
        img.setAttribute('description', item.description);
        
        const desc = document.createElement('p');
        desc.innerText = item.description;
        
        itemDiv.appendChild(img);
        itemDiv.appendChild(desc);
        itemContainer.appendChild(itemDiv);
    });
});

function printInvoice() {
    window.print();
}