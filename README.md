This is for a class at BHCC;

Time and Calendar Exercise
Overview
Create a system of classes to represent time, dates, and appointments in a calendar application.
Part 1: Time Class
First, create a Time class similar to the example in previous chapters:
1. Create a Time class with attributes for hours, minutes, and seconds
2. Add a __str__ method that formats the time as "HH:MM:SS"
3. Write a method is_valid that checks if the time is valid (hours 0-23, minutes 0-59, seconds 0-
59)
4. Implement a __lt__ method to compare times chronologically
5. Add methods to add and subtract times, ensuring proper carry/borrow operations
   
Part 2: Date Class
Create a Date class to represent calendar dates:
1. Initialize with year, month, and day attributes
2. Add a __str__ method that formats the date as "YYYY-MM-DD"
3. Write a method is_valid that checks if the date is valid (considering month lengths and leap
years)
4. Implement __lt__ to compare dates chronologically
5. Add a method to calculate the day of the week for any date
   
Part 3: Appointment Class
Create an Appointment class that inherits from both Date and Time:
1. Create a new class DateTime that combines date and time information
2. Create an Appointment class that inherits from DateTime and adds:
A title attribute
A duration attribute (in minutes)
A location attribute
A description attribute
3. Add a method conflicts_with that checks if two appointments overlap
4. Implement a __str__ method to format the appointment information nicely
   
Part 4: Calendar Class
Create a Calendar class to manage a collection of appointments:
1. Initialize with a name and an empty list of appointments
2. Add methods to add and remove appointments
3. Create a method to find all appointments on a given date
4. Implement a method to find conflicts among all appointments
5. Add a method to print a formatted daily or weekly view of appointments
   
Part 5: Specialized Calendar Types
Create at least two specialized calendar types that inherit from Calendar:
1. WorkCalendar - with methods specific to work appointments
2. SchoolCalendar - with methods specific to academic appointments
Each specialized calendar might have its own rules about valid appointment times, conflict resolution,
or display formats.

Testing
Create a script that demonstrates all features of your calendar system:
1. Create instances of different times, dates, and appointments
2. Test the validation methods
3. Test for appointment conflicts
4. Create specialized calendars and demonstrate their unique features
   
This exercise gives you practice with:
Multiple inheritance
Method overriding
Date and time manipulation
Complex validation logic
Designing a coherent class hierarchy
Submit your solution as well-documented Python code with appropriate comments and test cases.
