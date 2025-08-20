# Student-Management-System
This repository contains a Student Management System developed as a final project for a Database Management course. The system demonstrates the integration of a normalized relational database with a graphical user interface, highlighting practical applications of database concepts and Python programming.

# Student Management System

A database management project implementing a simple Student Management System using **MySQL** and **Python (Tkinter)**.  
This system provides basic student account functionality through a graphical user interface (GUI) connected to a normalized relational database.

---

## Features
- Register new students with unique email addresses  
- User login with credential verification  
- Update account details (name and/or password)  
- Delete accounts from the system  
- All GUI actions interact directly with the MySQL database using parameterized SQL queries  

---

## Requirements
- Python 3.x  
- Libraries:  
  - `pymysql`  
  - `tkinter`  
- MySQL Server (localhost)  
- MySQL Workbench  

---

## Installation and Usage
1. Start the MySQL server locally.  
2. Run the provided schema script to create the database:  
   ```bash
   mysql -u root -p < students_schema.sql

