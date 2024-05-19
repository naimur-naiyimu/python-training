-- Create the database
CREATE DATABASE school;
USE school;

-- Create the student_attendance table
CREATE TABLE student_attendance (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    class VARCHAR(50),
    date DATE,
    status ENUM('present', 'absent')
);

-- Insert sample student attendance records
INSERT INTO student_attendance (student_name, class, date, status) VALUES 
('John Doe', '10A', '2024-05-19', 'present'),
('Jane Smith', '10A', '2024-05-19', 'absent'),
('Mike Brown', '10B', '2024-05-19', 'present');

-- Query to find the number of students who are present today
SELECT COUNT(*) AS present_count
FROM student_attendance
WHERE date = CURDATE() AND status = 'present';

-- Query to find the number of students who are absent today
SELECT COUNT(*) AS absent_count
FROM student_attendance
WHERE date = CURDATE() AND status = 'absent';

-- Query to list all students who are present today
SELECT student_name, class
FROM student_attendance
WHERE date = CURDATE() AND status = 'present';

-- Query to list all students who are absent today
SELECT student_name, class
FROM student_attendance
WHERE date = CURDATE() AND status = 'absent';
