
#Time and Calendar Exercise

print("Time and Calendar Exercise")


# part 1

# the time class is defined to represent a time of day.
class Time:
    # this __init__ method is responsible for initializing the time object with hour, minute, and second values.
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour              # the hour is set
        self.minute = minute          # the minute is set
        self.second = second          # the second is set

    # this __str__ method returns a string of the time in hh:mm:ss format
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"  # this includes leading zeros

    # the is_valid method checks whether the time is valid with hours in 0-23, minutes and seconds in 0-59
    def is_valid(self):
        return (0 <= self.hour < 24 and      # the hour is required to be in the range 0 to 23
                0 <= self.minute < 60 and    # the minute is required to be in the range 0 to 59
                0 <= self.second < 60)       # the second is required to be in the range 0 to 59

    # this __lt__ method provides a comparison between two time objects.
    def __lt__(self, other):
        return (self.hour, self.minute, self.second) < (other.hour, other.minute, other.second)  # the comparison is based on tuple

    # this to_seconds method converts the time object to the total number of seconds since 00:00:00.
    def to_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second  # the conversion is done by multiplying hours by 3600, minutes by 60, and adding seconds

    # the from_seconds class method creates a time object from a total number of seconds.
    @classmethod
    def from_seconds(cls, total_seconds):
        seconds_in_day = 24 * 3600              # the number of seconds in one day is computed.
        total_seconds %= seconds_in_day         # the total seconds are wrapped to remain within one day.
        hour = total_seconds // 3600            # the hour is computed by integer division by 3600.
        total_seconds %= 3600                   # the total seconds are reduced by the hours component.
        minute = total_seconds // 60            # the minute is computed by integer division by 60.
        second = total_seconds % 60             # the remaining seconds are computed.
        return cls(hour, minute, second)        # a new time object is returned with the computed values.

    # the add_time method computes the sum of two time objects and returns a new time object.
    def add_time(self, other):
        total = self.to_seconds() + other.to_seconds()  # the sum of total seconds from both time objects is calculated.
        return Time.from_seconds(total)                 # the total seconds are converted back into a time object.

    # the subtract_time method computes the difference between two time objects and returns a new time object.
    def subtract_time(self, other):
        total = self.to_seconds() - other.to_seconds()  # the difference in total seconds is calculated
        return Time.from_seconds(total)                 # the difference is converted back into a time object

    # this __add__ method loads the + operator to add two time objects
    def __add__(self, other):
        return self.add_time(other)  # the addition operation is performed using the add_time method

    # this __sub__ method loads the - operator to subtract one time object from another
    def __sub__(self, other):
        return self.subtract_time(other)  # the subtraction operation is performed using the subtract_time method

# test 1 scripts
print("Below are Part 1 Tests")

t1 = Time(9, 30, 45)
t2 = Time(2, 45, 30)

# the object are printed using its __str__ method.
print("time 1:", t1)  # expected to be "time 1: 09:30:45".

print("time 2:", t2)  # expected to be "time 2: 02:45:30".

# the validity of the objects is checked and printed.
print("t1 is valid:", t1.is_valid())  # expected to be true.

print("t2 is valid:", t2.is_valid())  # expected to be true.

# comparison is performed to check if t1 occurs before t2
print("t1 < t2:", t1 < t2)  # the result is expected to be false since 09:30:45 is after 02:45:30.

# the two time objects are added together and the result is stored in t3
t3 = t1 + t2 
print("t1 + t2 =", t3)  # the sum is printed after conversion back to time format.

# the second time object is subtracted from the first and the result is stored in t4.
t4 = t1 - t2 
print("t1 - t2 =", t4)  # the difference is printed after conversion back to time format



# part 2


# the date class is defined to represent a calendar date.
class Date:
    # this __init__ method initializes the date object with year, month, and day.
    def __init__(self, year, month, day):
        self.year = year          # the year attribute is assigned to the year
        self.month = month        # the month attribute is assigned to the month
        self.day = day            # the day attribute is assigned to the day

    # this __str__ method returns a string representation of the date in "yyyy-mm-dd" format.
    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"  # the date is formatted with leading zeros.

    # this is_valid method checks whether the date is valid and considers month lengths and leap years.
    def is_valid(self):
        if self.month < 1 or self.month > 12:
            return False         # the month is invalid if it is not between 1 and 12
        if self.day < 1:
            return False         # the day is invalid if it is less than 1
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            max_day = 31         # max 31 days
        elif self.month in [4, 6, 9, 11]:
            max_day = 30         # max 30 days
        elif self.month == 2:
            if self.is_leap_year():
                max_day = 29     # february max 29 days in a leap year
            else:
                max_day = 28     # february max 28 days in a non-leap year
        else:
            return False         # the month is invalid if it does not match any valid month
        return self.day <= max_day  # the day is valid if it does not exceed the maximum for the month

    # this is_leap_year method checks whether the year is a leap year.
    def is_leap_year(self):
        return (self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0))
        # the year is a leap year if divisible by 4 and not by 100, unless it is divisible by 400.

    # this __lt__ method compares two date objects chronologically.
    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)
        # the comparison is performed by converting the date attributes into tuples.

    def day_of_week(self):
        year = self.year                   # the current year is stored in a variable
        month = self.month                 # the current month is stored in a variable
        day = self.day                     # the current day is stored in a variable
        if month < 3:
            year -= 1                      # adjusts the year for january and february
        month_offsets = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]  # lists of month specific offsets
        index = (year + year // 4 - year // 100 + year // 400 + month_offsets[month - 1] + day) % 7  # calculate the index for the day of the week
        week_days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # list of weekday names
        return week_days[index]  # returns the weekday corresponding to the index

# tests 2 scripts

print("\n Below are the tests for part 2")

date1 = Date(2000, 1, 1)
print("date:", date1)     # the output is expected to be "2000-01-01"
print("day of week:", date1.day_of_week())  # the result is expected to be saturday


date2 = Date(2023, 12, 25)
print("date:", date2)       # the output is expected to be "2023-12-25"
print("day of week:", date2.day_of_week())  # the result is expected to be monday

date3 = Date(1776, 7, 4)
print("date:", date3)       # the output is expected to be "1776-07-04"
print("day of week:", date3.day_of_week())  # the result is expected to be thursday


#part 3

# this datetime class is defined to combine date and time information
class DateTime(Date, Time):
    # this __init__ method initializes the datetime object with date and time components.
    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        Date.__init__(self, year, month, day)    # the date portion is initialized using the date class
        Time.__init__(self, hour, minute, second)  # the time portion is initialized using the time class

    # this __str__ method returns a string representation that combines date and time.
    def __str__(self):
        return f"{Date.__str__(self)} {Time.__str__(self)}" 

# this appointment class is defined to represent an appointment
class Appointment(DateTime):
    # this __init__ method initializes the appointment object with datetime and some attributes
    def __init__(self, year, month, day, hour, minute, second, title, duration, location, description):
        DateTime.__init__(self, year, month, day, hour, minute, second)  # the datetime is initialized
        self.title = title              # the title is assigned
        self.duration = duration        # the duration is assigned in minutes
        self.location = location        # the location is assigned
        self.description = description  # the description is assigned

    # this conflicts_with method checks whether two appointments overlap.
    def conflicts_with(self, other):
        # checks if they are on different dates
        if (self.year, self.month, self.day) != (other.year, other.month, other.day):
            return False  # returns if the appointments are on different dates and do not conflict
        self_start = self.hour * 60 + self.minute  # the start time in minutes for the first appointment
        self_end = self_start + self.duration       # the end time for the first appointment
        other_start = other.hour * 60 + other.minute  # the start time in minutes for the second appointment
        other_end = other_start + other.duration     # the end time for the second appointment
        return self_start < other_end and other_start < self_end  # the appointments conflict if their time overlap

    # this __str__ method returns a formatted string representation of the appointment
    def __str__(self):
        return (f"appointment: {self.title}\n"
                f"date: {Date.__str__(self)}\n"
                f"time: {Time.__str__(self)}\n"
                f"duration: {self.duration} minutes\n"
                f"location: {self.location}\n"
                f"description: {self.description}")

# test 3 scripts

print("\n below are tests for part 3")

# creating four appointments

appt1 = Appointment(2023, 5, 15, 10, 0, 0, "meeting with team", 60, "conference room", "discuss project updates")
print("appointment 1:")
print(appt1)
print()

appt2 = Appointment(2023, 5, 15, 10, 30, 0, "client call", 30, "office", "call with important client")
print("appointment 2:")
print(appt2)
print()

appt3 = Appointment(2023, 5, 15, 12, 0, 0, "lunch with manager", 45, "restaurant", "discuss strategy")
print("appointment 3:")
print(appt3)
print()

appt4 = Appointment(2023, 5, 16, 10, 0, 0, "daily standup", 60, "online", "daily team meeting")
print("appointment 4:")
print(appt4)
print()

# this test checks if appointment 1 conflicts with appointment 2 (expected to be true because their times overlap).
print("appointment 1 conflicts with appointment 2:", appt1.conflicts_with(appt2))  # expected: true

# this test checks if appointment 1 conflicts with appointment 3 (expected to be false because their times do not overlap).
print("appointment 1 conflicts with appointment 3:", appt1.conflicts_with(appt3))  # expected: false

# this test checks if appointment 1 conflicts with appointment 4 (expected to be false because the dates are different).
print("appointment 1 conflicts with appointment 4:", appt1.conflicts_with(appt4))  # expected: false

#part 4

# the calendar class is defined to manage a collection of appointments
class Calendar:
    # this __init__ method initializes the calendar with a name and an empty list of appointments.
    def __init__(self, name):
        self.name = name  # the name attribute is set to the name.
        self.appointments = []  # the appointments attribute is initialized as an empty list.

    # this add_appointment method adds an appointment to the calendar.
    def add_appointment(self, appointment):
        self.appointments.append(appointment)  # the appointment is added to the appointments list.

    # this remove_appointment method removes an appointment from the calendar.
    def remove_appointment(self, appointment):
        if appointment in self.appointments:
            self.appointments.remove(appointment)  # the appointment is removed if it exists in the list.

    # this appointments_on_date method returns a list of appointments that occur on the given date
    def appointments_on_date(self, date):
        return [appt for appt in self.appointments
                if (appt.year, appt.month, appt.day) == (date.year, date.month, date.day)]
        # the appointments are filtered by matching the year, month, and day with the given date

    # this find_conflicts method returns a list of conflicting appointments
    def find_conflicts(self):
        conflicts = []  # the conflicts list is initialized to store pairs of conflicting appointments.
        n = len(self.appointments)  # the total number of appointments is stored
        for i in range(n):
            for j in range(i + 1, n):
                if self.appointments[i].conflicts_with(self.appointments[j]):
                    conflicts.append((self.appointments[i], self.appointments[j]))
                    # the conflicting pair is added if the two appointments overlap
        return conflicts

    # this print_daily_view method prints a formatted view of appointments on a date
    def print_daily_view(self, date):
        daily_appts = self.appointments_on_date(date)  # the appointments for the date are filtered
        daily_appts.sort(key=lambda appt: appt.to_seconds())
        # the appointments are sorted by their time by converting into seconds.
        print(f"daily view for {date}:")  # a header is printed with the date
        if not daily_appts:
            print("no appointments found")  # a message is printed if there are no appointments
        else:
            for appt in daily_appts:
                print("-" * 40)
                print(appt)
            print("-" * 40)

    # this print_weekly_view method prints a formatted view of appointments for a specified date range
    def print_weekly_view(self, start_date, end_date):
        weekly_appts = [appt for appt in self.appointments
                        if (appt.year, appt.month, appt.day) >= (start_date.year, start_date.month, start_date.day)
                        and (appt.year, appt.month, appt.day) <= (end_date.year, end_date.month, end_date.day)]
        # the appointments are filtered by checking if they fall between the start and end dates
        weekly_appts.sort(key=lambda appt: (appt.year, appt.month, appt.day, appt.to_seconds()))
        # the appointments are sorted by date and then by time
        print(f"weekly view from {start_date} to {end_date}:")  # a header is printed with the date range, same as abovr.
        if not weekly_appts:
            print("no appointments found")  # a message is printed if there are no appointments, also same as above.
        else:
            current_date = None  # the current_date variable is initialized to group appointments by the date
            for appt in weekly_appts:
                appt_date = (appt.year, appt.month, appt.day)
                if appt_date != current_date:
                    current_date = appt_date
                    print("=" * 40)
                    print(f"date: {appt.year:04d}-{appt.month:02d}-{appt.day:02d}")
                    # a new date header is printed once new date is encountered
                print("-" * 40)
                print(appt)
            print("=" * 40)

# test 4 scripts

print(("\n below are the tests for part 4"))


cal = Calendar("work calendar")  # a calendar object is instantiated with the name work calendar

# making multiple appointments
appt1 = Appointment(2023, 5, 15, 10, 0, 0, "meeting with team", 60, "conference room", "discuss project updates")
appt2 = Appointment(2023, 5, 15, 10, 30, 0, "client call", 30, "office", "call with important client")
appt3 = Appointment(2023, 5, 15, 12, 0, 0, "lunch with ceo", 45, "restaurant", "discuss strategy")
appt4 = Appointment(2023, 5, 16, 9, 0, 0, "daily standup", 30, "online", "daily team meeting")
appt5 = Appointment(2023, 5, 17, 14, 0, 0, "project review", 90, "meeting room", "review project progress")

# appointments are added to the calendar
cal.add_appointment(appt1) 
cal.add_appointment(appt2)
cal.add_appointment(appt3) 
cal.add_appointment(appt4) 
cal.add_appointment(appt5) 

# the daily view is printed for may 15, 2023
print("\n--- daily view test ---") #\n is used to give us a line of space
test_date = Date(2023, 5, 15)  
cal.print_daily_view(test_date)  # the daily view for the specified date is printed

# weekly view is printed from may 15, 2023 to may 17, 2023
print("\n--- weekly view test ---") 
start_date = Date(2023, 5, 15) 
end_date = Date(2023, 5, 17)    
cal.print_weekly_view(start_date, end_date)  # the weekly view for the specified date range is printed

# find_conflicts method test
print("\n--- conflicts test ---")
conflict_list = cal.find_conflicts()  # the conflicting appointments are found
if not conflict_list:
    print("no conflicts found")  # a message is printed if there are no conflicts
else:
    for conflict in conflict_list:
        print("-" * 40)
        print("conflict between:")
        print(conflict[0])
        print("and")
        print(conflict[1])
    print("-" * 40)

# the remove_appointment method is tested by removing appt2
cal.remove_appointment(appt2)  # appt2 is removed from the calendar
print("\n--- after removing an appointment ---")
cal.print_daily_view(test_date)  # the daily view is printed again for may 15, 2023 to show the updated appointments


#part 5

# this workcalendar class is defined to manage work appointments with some rules
class WorkCalendar(Calendar):
    # the add_appointment method only accept appointments within work hours 8:00 to 18:00.
    def add_appointment(self, appointment):
        if appointment.hour < 8 or appointment.hour >= 18:
            print(f"workcalendar: appointment '{appointment.title}' not added; not within work hours.")
        else:
            super().add_appointment(appointment)

    # this print_work_schedule method prints a weekly view for work appointments
    def print_work_schedule(self, start_date, end_date):
        print("work schedule:")
        self.print_weekly_view(start_date, end_date)


# this schoolcalendar class is defined to manage academic appointments
class SchoolCalendar(Calendar):
    # this add_appointment method only accepts appointments within school hours 8:00 to 16:00.
    def add_appointment(self, appointment):
        if appointment.hour < 8 or appointment.hour >= 16:
            print(f"schoolcalendar: appointment '{appointment.title}' not added; not within school hours.")
        else:
            super().add_appointment(appointment)

    # this print_class_schedule method prints a daily view for school appointments
    def print_class_schedule(self, date):
        print("class schedule for", date)
        self.print_daily_view(date)


# tests 5 script

print("\n below are the tests for part 5\n")

work_cal = WorkCalendar("work calendar") 

# creats several appointments to test workcalendar
appt_a = Appointment(2023, 6, 1, 7, 30, 0, "early meeting", 30, "office", "discussion")  # an appointment before work hours
appt_b = Appointment(2023, 6, 1, 9, 0, 0, "team meeting", 60, "conference room", "monthly meeting")  # an appointment within work hours
appt_c = Appointment(2023, 6, 1, 18, 0, 0, "evening review", 45, "office", "end of day review")  # an appointment at the end of work hours

# adds the appointments to the workcalendar
work_cal.add_appointment(appt_a)  # the appointment is rejected because it is before work hours
work_cal.add_appointment(appt_b)  # the appointment is accepted because it is within work hours
work_cal.add_appointment(appt_c)  # the appointment is rejected because it is not within work hours

# prints the weekly view for the workcalendar between june 1, 2023 and june 7, 2023
print("\n--- work calendar weekly view test ---")
start_date = Date(2023, 6, 1) 
end_date = Date(2023, 6, 7)    
work_cal.print_work_schedule(start_date, end_date)  # weekly view is printed

# creates a schoolcalendar object with a name
school_cal = SchoolCalendar("school calendar")

# creates several appointment objects to test schoolcalendar
appt_d = Appointment(2023, 6, 2, 7, 50, 0, "early class", 45, "classroom", "math class")  # an appointment before school hours
appt_e = Appointment(2023, 6, 2, 10, 0, 0, "science lecture", 60, "auditorium", "biology")  # an appointment within school hours
appt_f = Appointment(2023, 6, 2, 16, 10, 0, "after school club", 60, "club room", "gaming club")  # an appointment after school hours

# adds the appointments to the schoolcalendar
school_cal.add_appointment(appt_d)  # this appointment is rejected because it is before school hours
school_cal.add_appointment(appt_e)  # this appointment is accepted because it is within school hours
school_cal.add_appointment(appt_f)  # this appointment is rejected because it is after school hours

# print the daily view for the schoolcalendar on june 2, 2023
print("\n--- school calendar daily view test ---")
test_date_school = Date(2023, 6, 2)
school_cal.print_class_schedule(test_date_school)  # the daily class schedule is printed.
