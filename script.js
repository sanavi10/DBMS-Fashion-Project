// 🧠 Sample data (you can later fetch this from backend MySQL via Flask or Node.js)
// 🧠 Fetch data from Flask backend instead of hardcoding
// ✅ Fetch product data dynamically from Flask backend
fetch("http://127.0.0.1:5000/products")
  .then(response => response.json())
  .then(products => {
    const productList = document.getElementById("product-list");
    productList.innerHTML = ""; // Clear any old data

    products.forEach(p => {
      const card = document.createElement("div");
      card.classList.add("product-card");

      // Adjust property names to match your database columns
      card.innerHTML = `
        <img src="${p.ProdImageURL || 'https://via.placeholder.com/200'}" alt="${p.ProdName}">
        <h3>${p.ProdName}</h3>
        <p>${p.ProdDescription}</p>
        <p class="price">₹${p.ProdPrice}</p>
        <button class="shop-btn">Add to Cart</button>
      `;

      productList.appendChild(card);
    });
  })
  .catch(err => console.error("⚠️ Error fetching products:", err));


// 🧩 Dynamically display products
const productList = document.getElementById("product-list");
products.forEach((p) => {
  const card = document.createElement("div");
  card.classList.add("product-card");
  card.innerHTML = `
        <img src="${p.img}" alt="${p.name}">
        <h3>${p.name}</h3>
        <p>${p.description}</p>
        <p class="price">₹${p.price}</p>
        <button class="shop-btn">Add to Cart</button>
    `;
  productList.appendChild(card);
});


fetch("http://127.0.0.1:5000/customers")
  .then(response => response.json())
  .then(customers => {
    const customerList = document.getElementById("customer-list");
    customerList.innerHTML = ""; // clear old data
    customers.forEach(c => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${c.CustName}</td>
        <td>${c.CustEmail}</td>
        <td>${c.Phone}</td>
        <td>${c.Address}</td>
      `;
      customerList.appendChild(row);
    });
  })
  .catch(err => console.error(err));