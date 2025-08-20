-- Create and use the database
CREATE DATABASE IF NOT EXISTS university_db;
USE university_db;

-- Students table: for registration & login system
CREATE TABLE students (
  student_id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  email VARCHAR(100) UNIQUE,
  password VARCHAR(100)
);

-- Departments
CREATE TABLE departments (
  department_id INT PRIMARY KEY AUTO_INCREMENT,
  department_name VARCHAR(100)
);

-- Professors (linked to departments)
CREATE TABLE professors (
  professor_id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  address VARCHAR(100),
  phone_number VARCHAR(20),
  email VARCHAR(100),
  department_id INT,
  FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Courses (linked to professors)
CREATE TABLE courses (
  course_id INT PRIMARY KEY AUTO_INCREMENT,
  course_name VARCHAR(100),
  professor_id INT,
  start_time TIME,
  end_time TIME,
  room_number VARCHAR(20),
  FOREIGN KEY (professor_id) REFERENCES professors(professor_id)
);

-- Enrolments 
CREATE TABLE enrolments (
  student_id INT,
  course_id INT,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Student Schedules (optional custom view per student)
CREATE TABLE schedules (
  student_id INT,
  course_id INT,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

SHOW TABLES;
DESCRIBE students;
DESCRIBE enrolments;
DESCRIBE schedules;

SELECT * FROM students;

