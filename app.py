from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # allow cross-origin requests from your frontend

# 🧠 Database Connection
db_config = {
    'host': 'localhost',
    'user': 'root',          # change this if your MySQL username is different
    'password': 'Rutuja@01',          # add your MySQL password here
    'database': 'Fashion'    # your database name
}

# Utility function for DB connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# 🧺 ROUTE 1: Get all products
@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Product;")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(products)

# 👩 ROUTE 2: Add a new customer (POST /customers)
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO Customer (CustName, CustEmail, Phone, Address)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (
        data["CustName"], data["CustEmail"], data["Phone"], data["Address"]
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Customer added successfully!"}), 201

# 📦 ROUTE 3: Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT Orders.OrderID, Orders.OrderDate, Customer.CustName, Orders.TotalAmount, Orders.Status
        FROM Orders
        JOIN Customer ON Orders.CustomerID = Customer.CustomerID;
    """)
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(orders)

# ➕ ROUTE 4: Place a new order (POST /orders)
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    customer_id = data.get('CustomerID')
    total_amount = data.get('TotalAmount')
    status = data.get('Status', 'Pending')

    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO Orders (OrderDate, CustomerID, TotalAmount, Status) VALUES (CURDATE(), %s, %s, %s)"
    cursor.execute(query, (customer_id, total_amount, status))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Order created successfully!"}), 201

# 🔍 ROUTE 5: Home test route
@app.route('/')
def home():
    return "Fashion Store Backend is Running 🧥"

if __name__ == '__main__':
    app.run(debug=True)
