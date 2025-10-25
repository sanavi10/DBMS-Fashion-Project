// Fetch only clothing products from the backend
fetch('/products?category=clothing')
  .then(response => response.json())
  .then(products => {
    const container = document.getElementById('clothing-container');
    container.innerHTML = '';

    products.forEach(p => {
      const card = document.createElement('div');
      card.classList.add('product-card');
      card.innerHTML = `
        <img src="${p.image}" alt="${p.name}">
        <h3>${p.name}</h3>
        <p>₹${p.price}</p>
      `;
      container.appendChild(card);
    });
  })
  .catch(err => console.error('Error fetching clothing products:', err));