document.addEventListener("DOMContentLoaded", function() {
    const suppliers = [
        {imgSrc: "supplier1.jpg", description: 'Supplier 1 - High quality electronics', rating: 4.5, location: 'USA', category: 'Electronics', verification: 'Gold'},
        {imgSrc: "supplier2.jpg", description: 'Supplier 2 - Affordable fashion', rating: 4.0, location: 'China', category: 'Fashion', verification: 'Silver'},
        // Add more supplier objects as required
    ];

    const supplierList = document.getElementById('supplier-list');
    const searchBar = document.getElementById('search-bar');

    function displaySuppliers(suppliers) {
        supplierList.innerHTML = '';
        suppliers.forEach(supplier => {
            const supplierItem = document.createElement('div');
            supplierItem.className = 'supplier-item';
            supplierItem.innerHTML = `
                <img src="${supplier.imgSrc}" alt="${supplier.description}" description="${supplier.description}">
                <div class="supplier-details">
                    <h3>${supplier.description}</h3>
                    <p>Rating: ${supplier.rating}</p>
                    <p>Location: ${supplier.location}</p>
                    <p>Category: ${supplier.category}</p>
                    <p>Verification: ${supplier.verification}</p>
                    <button onclick="location.href='supplier_profile.html'">View Profile</button>
                </div>
                <div class="supplier-badge ${supplier.verification.toLowerCase()}">${supplier.verification}</div>
            `;
            supplierList.appendChild(supplierItem);
        });
    }

    function sortSuppliers(criteria) {
        const sortedSuppliers = suppliers.sort((a, b) => a[criteria] > b[criteria] ? 1 : -1);
        displaySuppliers(sortedSuppliers);
    }

    function filterSuppliers(criteria) {
        const filteredSuppliers = suppliers.filter(supplier => supplier[criteria]);
        displaySuppliers(filteredSuppliers);
    }

    function searchSuppliers(query) {
        const filteredSuppliers = suppliers.filter(supplier => supplier.description.toLowerCase().includes(query.toLowerCase()));
        displaySuppliers(filteredSuppliers);
    }

    searchBar.addEventListener('input', (e) => {
        searchSuppliers(e.target.value);
    });

    displaySuppliers(suppliers);
});