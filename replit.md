# Course Schedule Search Program

## Overview
A Python command-line application for managing and searching college course schedules loaded from CSV files.

## Project Structure
- `schedule_item.py` - ScheduleItem dataclass (subject, catalog, section, component, session, units, enrollment, instructor)
- `schedule.py` - Schedule class for managing courses with search functionality
- `main.py` - Main program with interactive menu
- `courses.csv` - Course schedule data

## Program Flow
1. main.py loads CSV data into Schedule
2. User selects menu option (display all, search by subject, search by subject+catalog, search by instructor, quit)
3. Results displayed in formatted output

## Recent Changes
- 2025-11-26: Updated to course schedule format (subjects, catalogs, sections, instructors)
- 2025-11-18: Initial project setup with Python 3.11

## Features
- Load course data from CSV files using csv.DictReader
- Display all courses with formatted output
- Search by subject (e.g., BIO, CS, MATH)
- Search by subject + catalog number
- Search by instructor last name

## User Preferences
- Clean, simplified code structure
- Course schedule format for academic use
