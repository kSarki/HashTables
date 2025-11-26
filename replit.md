# Schedule Search Program

## Overview
A simplified Python command-line application for managing and searching schedule items loaded from CSV files.

## Project Structure
- `schedule_item.py` - ScheduleItem dataclass (date, time, title, description, location)
- `schedule.py` - Schedule class for managing items with search functionality
- `main.py` - Main program with interactive menu
- `schedule_data.csv` - Sample schedule data

## Program Flow
1. main.py loads CSV data into Schedule
2. User selects menu option (display all, search, quit)
3. Results displayed in formatted output

## Recent Changes
- 2025-11-26: Simplified code - cleaner structure, fewer lines, same functionality
- 2025-11-18: Initial project setup with Python 3.11

## Features
- Load schedule data from CSV files using csv.DictReader
- Display all schedule items with formatted output
- Search across title, description, and location fields
- Simple 3-option menu interface

## User Preferences
- Clean, simplified code structure
- Minimal lines while maintaining readability
