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

🏨 Hotel Customer Management System

📌 Project Overview

The Hotel Customer Management System is a desktop application developed to manage hotel customer information efficiently. This system provides an easy and organized way to add, view, update, and delete customer records.

The application is developed using Python Tkinter for the graphical user interface and MySQL Database for data storage. The system helps reduce manual record management and improves the efficiency of hotel customer handling.

---

🎯 Project Objectives

No| Objective
1| Develop a user-friendly hotel customer management application
2| Store customer information using a structured database
3| Perform customer record management operations efficiently
4| Reduce manual data handling
5| Demonstrate Python GUI and database integration

---

🚀 Main Features

Feature| Description
Add Customer| Add new customer details into the database
View Customer| Display all customer records
Update Customer| Modify existing customer information
Delete Customer| Remove customer records from the system
Database Connection| Connect Python application with MySQL database
User Interface| Provide an interactive graphical interface

---

🖥️ System Modules

Module| Function| Description
Customer Management| Add Customer| Enter and save new customer details
Customer Management| View Customer| Display registered customer information
Customer Management| Update Customer| Edit customer records
Customer Management| Delete Customer| Remove customer information
Database Management| MySQL Connection| Store and retrieve customer data

---

🗄️ Database Design

Database Name

hotel_db

Customer Table

Field Name| Data Type| Key| Description
id| INT| Primary Key| Unique customer identification number
name| VARCHAR(100)| -| Customer full name
phone| VARCHAR(20)| -| Customer contact number
room_no| VARCHAR(20)| -| Assigned hotel room number

---

🔄 CRUD Operations

Operation| Function| Description
Create| Add Customer| Insert new customer records into database
Read| View Customer| Retrieve customer information
Update| Update Customer| Change existing customer details
Delete| Delete Customer| Remove unwanted customer records

---

🛠️ Technologies Used

Technology| Purpose
Python| Main programming language
Tkinter| Graphical User Interface development
MySQL| Database management
XAMPP| Local MySQL server environment
VS Code| Application development

---

📂 Project Structure

File Name| Description
main.py| Contains GUI design and customer management functions
database.py| Handles MySQL database connection
README.md| Project documentation

---

⚙️ Installation Requirements

Requirement| Description
Python| Required to run the application
MySQL| Required for database storage
XAMPP| Used to run MySQL server
VS Code| Used for coding and development

---

📥 Installation Steps

Step 1: Clone Repository

Download or clone the project from GitHub.

Step 2: Install Required Package

Run:

pip install mysql-connector-python

Step 3: Create Database

Create database:

CREATE DATABASE hotel_db;

Create table:

CREATE TABLE customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    room_no VARCHAR(20)
);

---

▶️ How to Run

Step| Action
1| Start XAMPP
2| Start MySQL service
3| Open project using VS Code
4| Run main.py
5| Manage customer records using the application

Command:

python main.py

---

📸 Application Screenshots

Home Interface

(Add your screenshot here)

---

Add Customer Interface

(Add your screenshot here)

---

Customer Records

(Add your screenshot here)

---

🔮 Future Improvements

Improvement| Description
Room Management| Manage hotel rooms and availability
Booking System| Add customer reservation features
Payment Module| Manage customer payments
Employee Management| Manage hotel staff information
Login System| Add secure user authentication
Report Generation| Generate customer and booking reports

---

✅ Conclusion

The Hotel Customer Management System provides an efficient solution for managing hotel customer information. The project demonstrates the practical use of Python GUI development, MySQL database connectivity, and CRUD operations in a real-world management system.

This project can be further expanded into a complete Hotel Management System by adding booking, payment, room, and employee management modules.

---

👨‍💻 Developer

Developed as a Python Database Management System Project.
