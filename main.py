import csv
from schedule import Schedule
from schedule_item import ScheduleItem
import run


def main():
    print("\n" + "="*60)
    print(" "*15 + "SCHEDULE SEARCH PROGRAM - START")
    print("="*60)
    
    csv_filename = "schedule_data.csv"
    
    print(f"\nStep 1: Loading file '{csv_filename}'...")
    
    try:
        with open(csv_filename, 'r', encoding='utf-8') as file:
            print("Step 2: Using csv.DictReader to read the file...")
            reader = csv.DictReader(file)
            
            print("Step 3: Creating Schedule() instance...")
            schedule = Schedule()
            
            print("Step 4: Creating ScheduleItem objects...")
            for row in reader:
                item = ScheduleItem(
                    date=row['date'],
                    time=row['time'],
                    title=row['title'],
                    description=row['description'],
                    location=row.get('location', '')
                )
                schedule.add_item(item)
            
            print(f"Step 5: schedule.load_from_csv completed!")
            print(f"Successfully loaded {schedule.get_count()} schedule items!")
            
            print("\n" + "="*60)
            print(" "*20 + "ALL SCHEDULE ITEMS")
            print("="*60)
            schedule.display_all()
            
            print("\nStep 6: Calling run.py recommend() function...")
            run.recommend(schedule)
            
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*60)
    print(" "*20 + "PROGRAM END")
    print("="*60)


if __name__ == "__main__":
    main()
