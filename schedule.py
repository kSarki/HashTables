import csv
from schedule_item import ScheduleItem

class Schedule:
    def __init__(self):
        self.items: list[ScheduleItem] = []

    def add_item(self, item: ScheduleItem) -> None:
        self.items.append(item)

    def load_from_csv(self, filename: str) -> None:
        with open(filename, encoding='utf-8') as f:
            for row in csv.DictReader(f):
                self.add_item(ScheduleItem(
                    date=row['date'],
                    time=row['time'],
                    title=row['title'],
                    description=row['description'],
                    location=row.get('location', '')
                ))

    def print_header(self) -> None:
        print(f"{'Date':<12}{'Time':<8}{'Title':<22}{'Location'}")
        print("-" * 60)

    def print_results(self, results: list[ScheduleItem]) -> None:
        self.print_header()
        for item in results:
            item.print()

    def print_all(self) -> None:
        self.print_results(self.items)

    def search(self, term: str) -> list[ScheduleItem]:
        term = term.lower()
        return [i for i in self.items if term in i.title.lower() or 
                term in i.description.lower() or term in i.location.lower()]

    def count(self) -> int:
        return len(self.items)
