# College Management System
This project is a Command Line Interface (CLI) application for a College Management System

## Technical Details
* Language: Python
* Architecture: Object-Oriented Programming utilizing Inheritance (`Person` -> `Student`, `Staff` -> `Academic`).
* Simplicity: Kept to basic coding principles without complex constructor (`__init__`) functions, utilizing sequential `setup()` methods to define class attributes.

## Features
* Interactive CLI: Users can navigate a simple terminal menu to execute commands.
* Enrollment Logic: Students can attempt to enroll in courses, and the system verifies course capacity before confirming a seat.
* Grading System: Academic staff (Lecturers) can assign grades to enrolled students.
* Course Tracking: The database monitors and outputs live course capacities and current student rosters.