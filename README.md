# 🏨 Hotel Customer Management System

## 📌 Project Overview

The **Hotel Customer Management System** is a desktop-based application developed to manage hotel customer information efficiently.

This system allows users to add, view, update, and delete customer records through a simple graphical user interface. Customer information is stored securely in a MySQL database.

The project is developed using **Python Tkinter** for GUI development and **MySQL** for database management.

---

# 🎯 Project Objectives

| No | Objective |
|---|---|
| 01 | Develop a simple hotel customer management application |
| 02 | Manage customer information digitally |
| 03 | Store customer records in a database |
| 04 | Reduce manual record keeping |
| 05 | Demonstrate Python and database integration |

---

# 🚀 Features

| Feature | Description |
|---|---|
| Add Customer | Add new customer details to the system |
| View Customer | Display all customer information |
| Update Customer | Edit existing customer details |
| Delete Customer | Remove customer records |
| Database Connection | Connect application with MySQL database |
| User Interface | Interactive graphical interface |

---

# 🖥️ System Interface

The system provides a user-friendly interface including:

- 🏨 Hotel management dashboard
- 📝 Customer input forms
- 🔘 Action buttons
- 📋 Customer data display table
- 🗄️ Database integration

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Graphical User Interface |
| MySQL | Database management |
| XAMPP | Local database server |
| VS Code | Development environment |

---

# 📂 Project Structure

| File Name | Description |
|---|---|
| `main.py` | Contains GUI design and customer management functions |
| `database.py` | Handles MySQL database connection |
| `README.md` | Project documentation |

---

# 🗄️ Database Design

## Database Name

`hotel_db`

## Table Name

`customers`

| Field Name | Data Type | Description |
|---|---|---|
| id | INT | Unique customer ID (Primary Key) |
| name | VARCHAR(100) | Customer name |
| phone | VARCHAR(20) | Customer contact number |
| room_no | VARCHAR(20) | Allocated room number |

---

# 🔄 CRUD Operations

| Operation | Function | Description |
|---|---|---|
| Create | Add Customer | Insert new customer records |
| Read | View Customer | Retrieve customer information |
| Update | Update Customer | Modify existing records |
| Delete | Delete Customer | Remove customer records |

---

# 💻 Code Implementation

The project uses a simple modular structure.

| File | Responsibility |
|---|---|
| `main.py` | Handles GUI, buttons, and customer operations |
| `database.py` | Creates MySQL database connection |

The system uses:

- Python functions for customer operations
- Tkinter widgets for GUI design
- MySQL queries for data management

---

# ⚙️ Installation Guide

## Requirements

| Software | Requirement |
|---|---|
| Python | Required |
| MySQL | Required |
| XAMPP | Required for local database |
| VS Code | Recommended IDE |

---

## Install Python Package

Run:

```bash
pip install mysql-connector-python
```

---

# 🗃️ Database Setup

Create database:

```sql
CREATE DATABASE hotel_db;
```

Create table:

```sql
CREATE TABLE customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    room_no VARCHAR(20)
);
```

---

# ▶️ How to Run

| Step | Action |
|---|---|
| 1 | Start XAMPP |
| 2 | Start MySQL service |
| 3 | Open project in VS Code |
| 4 | Run main.py |
| 5 | Use the application |

Run command:

```bash
python main.py
```

---

# 📸 Application Screenshots

## 🏠 Home Interface

![Home Interface](screenshot/Screenshot%202026-07-09%20155306.png)

**Description:**  
This is the main interface of the Hotel Customer Management System. Users can enter customer details and access all customer management functions through a simple graphical user interface.

---

## ➕ Add Customer

![Add Customer](screenshot/Screenshot%202026-07-09%20155340.png)

**Description:**  
This screen displays the customer registration form where users can enter customer details such as name, phone number, and room number before saving the information into the MySQL database.

---

## 📋 Customer Records

![Customer Records](screenshot/Screenshot%202026-07-09%20155405.png)

**Description:**  
This screen displays all customer records stored in the MySQL database. Users can view, update, and delete customer information efficiently.

---

# 🔮 Future Improvements

| Improvement | Description |
|---|---|
| Room Management | Manage room availability |
| Booking System | Handle customer reservations |
| Payment System | Manage hotel payments |
| Employee Management | Manage staff details |
| Login System | Add user authentication |
| Reports | Generate management reports |

---

# ✅ Conclusion

The **Hotel Customer Management System** provides an efficient solution for managing hotel customer records.

This project demonstrates the practical application of Python GUI development, database connectivity, and CRUD operations. The system can be further expanded into a complete Hotel Management System.

---

# 👨‍💻 Developer

Developed as a Python Database Management System Project.
