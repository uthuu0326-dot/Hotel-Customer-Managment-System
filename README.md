🏨 Hotel Customer Management System

📌 Project Overview

The Hotel Customer Management System is a desktop-based application developed to manage hotel customer information efficiently. 
This system helps hotel staff to store, view, update, and delete customer records using a simple and user-friendly graphical interface.
The application is developed using Python Tkinter for the user interface and MySQL Database for data storage. 
It provides an organized way to manage customer details and reduces manual record management.

---

🎯 Project Objectives

- To develop a simple hotel customer management application.
- To store customer details in a structured database.
- To provide an easy-to-use graphical user interface.
- To perform basic CRUD operations (Create, Read, Update, Delete).
- To improve efficiency in managing hotel customer records.

---

🚀 Features

👤 Customer Management

➕ Add Customer

- Add new customer information to the system.
- Store customer name, phone number, and room number.

👀 View Customer

- Display all registered customers.
- Retrieve customer information from the database.

✏️ Update Customer

- Modify existing customer details.

🗑 Delete Customer

- Remove customer records from the database.

---

🖥️ User Interface

The system provides a graphical user interface with:

- Hotel dashboard design
- Input forms
- Action buttons
- Customer data table
- User-friendly navigation

---

🛠️ Technologies Used

Technology| Purpose
Python| Programming Language
Tkinter| GUI Development
MySQL| Database Management
XAMPP| Local Server Environment
VS Code| Code Development

---

Table Fields:

Field| Description
id| Unique Customer ID
name| Customer Name
phone| Contact Number
room_no| Allocated Room Number

---

⚙️ Installation Guide

1. Install Required Software

Install:

- Python
- MySQL / XAMPP
- Visual Studio Code

---

2. Install Python Library

Run:

pip install mysql-connector-python

---

3. Create Database

Open phpMyAdmin and create:

CREATE DATABASE hotel_db;

Create customer table:

CREATE TABLE customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    room_no VARCHAR(20)
);

---

▶️ How to Run

1. Start XAMPP.
2. Start MySQL service.
3. Open project folder in VS Code.
4. Run:

python main.py

5. Use the application interface to manage customer records.


🔮 Future Improvements

Future versions can include:

- Room Management Module
- Booking Management
- Payment Management
- Employee Management
- Customer Search Function
- Report Generation
- Login Authentication System

---

👨‍💻 Developer

Developed as a Python Database Management Project.



