# Salon Inventory Management System

A full-stack **Salon Inventory Management System** built with **Django REST API** and **React**.
The system helps salons manage product inventory, distributors, orders, product usage, and product sales.

---

# Project Overview

This project provides a simple inventory solution for salons to manage:

* Product catalog
* Distributor management
* Product ordering
* Inventory tracking
* Product sales
* Product usage within salon services

The system is divided into two parts:

**Backend:** Django + Django REST Framework
**Frontend:** React + Axios + Bootstrap

---

# Technologies Used

### Backend

* Python
* Django
* Django REST Framework
* SQLite (default database)

### Frontend

* React
* Axios
* React Router
* Bootstrap

### Version Control

* Git
* GitHub

---

# Project Structure

```
salon-inventory-system
│
├── backend
│   │
│   ├── salon_inventory
│   │   ├── settings.py
│   │   ├── urls.py
│   │
│   ├── inventory
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── services.py
│   │   ├── signals.py
│   │
│   └── manage.py
│
├── frontend
│   │
│   ├── src
│   │   ├── api
│   │   │   └── api.js
│   │   │
│   │   ├── components
│   │   │   └── Navbar.js
│   │   │
│   │   ├── pages
│   │   │   ├── Products.js
│   │   │   ├── Distributors.js
│   │   │   ├── Orders.js
│   │   │   ├── Inventory.js
│   │   │   ├── Sales.js
│   │   │   └── Usage.js
│   │   │
│   │   ├── App.js
│   │   └── index.js
│   │
│   └── package.json
│
└── README.md
```

---

# Features

### Product Menu

Stores all products available in the salon.

Example products:

* Shampoo
* Hair color
* Wax
* Facial cream

Each product contains:

* Name
* SKU
* Product type
* Cost price
* Selling price
* Unit

---

### Distributor Management

Stores information about product suppliers.

Fields include:

* Distributor name
* Phone
* Email
* Address

---

### Product Orders

Allows salons to order products from distributors.

Order contains:

* Distributor
* Order date
* Order items
* Order status
* Total amount

---

### Inventory Management

Tracks product stock available in the salon.

Inventory increases when:

* New products are ordered

Inventory decreases when:

* Products are sold
* Products are used for salon services

---

### Product Sales

Tracks products sold to customers.

Example:

Customer buys shampoo
Inventory quantity decreases automatically.

---

### Product Usage

Tracks products used internally for salon services.

Example:

Hair color used for hair coloring service
Inventory quantity decreases.

---

# Backend Setup (Django)

### 1. Clone the repository

```
git clone https://github.com/yourusername/salon-inventory-system.git
cd salon-inventory-system/backend
```

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install django
pip install djangorestframework
pip install django-cors-headers
```

### 4. Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin User

```
python manage.py createsuperuser
```

### 6. Start Backend Server

```
python manage.py runserver
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

# API Endpoints

| Endpoint           | Description              |
| ------------------ | ------------------------ |
| /api/products/     | List and create products |
| /api/distributors/ | Manage distributors      |
| /api/orders/       | Create and view orders   |
| /api/inventory/    | View inventory           |
| /api/sales/        | Record product sales     |
| /api/usage/        | Record product usage     |

---

# Frontend Setup (React)

### 1. Navigate to frontend folder

```
cd ../frontend
```

### 2. Install Dependencies

```
npm install
npm install axios
npm install react-router-dom
npm install bootstrap
```

### 3. Start React Server

```
npm start
```

Frontend will run at:

```
http://localhost:3000
```

---

# API Configuration

File:

```
src/api/api.js
```

Example:

```
import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api/"
});

export default API;
```

---

# Inventory Workflow

```
Distributor
      │
      ▼
Product Order
      │
      ▼
Inventory Updated
      │
 ┌────┴────┐
 ▼         ▼
Sales     Usage
 ▼         ▼
Stock ↓   Stock ↓
```

---

# Future Improvements

Possible enhancements:

* Inventory dashboard
* Sales analytics
* Low stock alerts
* Product categories
* Barcode support
* Multi-branch inventory
* Authentication and role management

---

# Author
Hemish Pansuriya
Salon Inventory Management System
Full-Stack Project using Django and React

---
