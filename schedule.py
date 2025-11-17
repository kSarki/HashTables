import csv
from schedule_item import ScheduleItem


class Schedule:
    def __init__(self):
        self.items = []
    
    def add_item(self, schedule_item):
        self.items.append(schedule_item)
    
    def load_from_csv(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    item = ScheduleItem(
                        date=row['date'],
                        time=row['time'],
                        title=row['title'],
                        description=row['description'],
                        location=row.get('location', '')
                    )
                    self.add_item(item)
            return True
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return False
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return False
    
    def search(self, search_term):
        results = [item for item in self.items if item.matches_search(search_term)]
        return results
    
    def get_all_items(self):
        return self.items
    
    def display_all(self):
        if not self.items:
            print("\nNo schedule items found.")
            return
        
        print(f"\n{'='*60}")
        print(f"Total Schedule Items: {len(self.items)}")
        print(f"{'='*60}")
        for item in self.items:
            item.display()
    
    def display_items(self, items):
        if not items:
            print("\nNo items found matching your search.")
            return
        
        print(f"\n{'='*60}")
        print(f"Found {len(items)} item(s)")
        print(f"{'='*60}")
        for item in items:
            item.display()
    
    def get_count(self):
        return len(self.items)
