# Schedule Search Program

## Overview
A Python command-line application for managing and searching schedule items loaded from CSV files with intelligent recommendations.

## Project Structure
- `schedule_item.py` - ScheduleItem class definition
- `schedule.py` - Schedule class for managing collections of schedule items
- `main.py` - Main program entry point following specific flowchart
- `run.py` - Recommendation engine that analyzes schedule data
- `schedule_data.csv` - Sample schedule data

## Program Flow
1. main.py starts
2. Load CSV file for schedule times
3. Use csv.DictReader to parse data
4. Create Schedule() instance
5. Create ScheduleItem objects from CSV rows
6. Call run.py recommend() function for analysis
7. Program ends

## Recent Changes
- 2025-11-18: Restructured program to follow specific flowchart with recommendation feature
- 2025-11-17: Initial project setup with Python 3.11

## Features
- Load schedule data from CSV files using csv.DictReader
- Automatic schedule item creation and management
- Intelligent recommendation system analyzing meetings, trainings, and interviews
- Display all schedule items with formatted output
- Top 3 upcoming items highlight

## User Preferences
- Follow specific flowchart structure for program execution
- Include recommendation analysis at program end
