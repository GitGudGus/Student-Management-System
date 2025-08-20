# Student-Management-System
This repository contains a Student Management System developed as a final project for a Database Management course. The system demonstrates the integration of a normalized relational database with a graphical user interface, highlighting practical applications of database concepts and Python programming.

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

3. Launch the GUI application:

```bash
python app.py
```

4. Use the interface to:

Register a new student

Log in with valid credentials

Update account information

Delete an account 

