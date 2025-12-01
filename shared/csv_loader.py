"""CSV loading utility for course schedule data."""

import csv
from .schedule_item import ScheduleItem


def load_courses_from_csv(filename: str) -> list[ScheduleItem]:
    """
    Load course data from a CSV file using DictReader.
    
    Args:
        filename: Path to the CSV file (expects UTF-8-sig encoding)
        
    Returns:
        List of ScheduleItem objects parsed from the CSV
        
    Expected CSV columns:
        Subject, Catalog, Section, Component, Session, Units, TotEnrl, CapEnrl, Instructor
    """
    items = []
    with open(filename, encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            items.append(ScheduleItem(
                subject=row['Subject'],
                catalog=row['Catalog'],
                section=row['Section'],
                component=row['Component'],
                session=row['Session'],
                units=int(row['Units']),
                tot_enrl=int(row['TotEnrl']),
                cap_enrl=int(row['CapEnrl']),
                instructor=row['Instructor']
            ))
    return items
