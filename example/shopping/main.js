// main.js
document.addEventListener('DOMContentLoaded', () => {
  const products = [
    { imgSrc: 'product1.jpg', description: 'Description for product 1, such as a black phone' },
    { imgSrc: 'product2.jpg', description: 'Description for product 2, such as a modern smart lock' },
    { imgSrc: 'product3.jpg', description: 'Description for product 3, such as a colorful 3D illustration' },
    { imgSrc: 'product4.jpg', description: 'Description for product 4, such as an elegant tea set' }
  ];

  const productsContainer = document.getElementById('products');
  products.forEach(product => {
    const productDiv = document.createElement('div');
    productDiv.classList.add('product-item');
    
    const img = document.createElement('img');
    img.src = product.imgSrc;
    img.alt = product.description;
    img.setAttribute('description', product.description);
    
    const desc = document.createElement('p');
    desc.textContent = product.description;
    
    productDiv.appendChild(img);
    productDiv.appendChild(desc);
    productsContainer.appendChild(productDiv);
  });
});