import csv
from schedule_item import ScheduleItem

class Schedule:
    def __init__(self):
        self.entries: dict[str, ScheduleItem] = {}

    def add_entry(self, item: ScheduleItem) -> None:
        self.entries[item.get_key()] = item

    def load_from_csv(self, filename: str) -> None:
        with open(filename, encoding='utf-8-sig', newline='') as f:
            for row in csv.DictReader(f):
                self.add_entry(ScheduleItem(
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

    def print_header(self) -> None:
        print("Subj Catalog Section Component Sess Units TotEnrl CapEnrl Instructor")

    def print_results(self, results: list[ScheduleItem]) -> None:
        self.print_header()
        for item in results:
            item.print()

    def print_all(self) -> None:
        self.print_results(list(self.entries.values()))

    def find(self, subject="", catalog="", instructor="") -> list[ScheduleItem]:
        results = list(self.entries.values())
        if subject:
            results = [i for i in results if i.subject == subject]
        if catalog:
            results = [i for i in results if i.catalog == catalog]
        if instructor:
            results = [i for i in results if i.instructor.split(',')[0] == instructor]
        return results
