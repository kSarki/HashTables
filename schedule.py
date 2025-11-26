import csv
from schedule_item import ScheduleItem

class Schedule:
    def __init__(self):
        self.items: list[ScheduleItem] = []

    def add_item(self, item: ScheduleItem) -> None:
        self.items.append(item)

    def load_from_csv(self, filename: str) -> None:
        with open(filename, encoding='utf-8-sig') as f:
            for row in csv.DictReader(f):
                self.add_item(ScheduleItem(
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
        print(f"{'Subj':4} {'Catalog':6} {'Section':6} {'Component':8} "
              f"{'Sess':4} {'Units':3} {'TotEnrl':6} {'CapEnrl':6} Instructor")

    def print_results(self, results: list[ScheduleItem]) -> None:
        self.print_header()
        for item in results:
            item.print()

    def print_all(self) -> None:
        self.print_results(self.items)

    def find_by_subject(self, subject: str) -> list[ScheduleItem]:
        return [i for i in self.items if i.subject == subject]

    def find_by_subject_catalog(self, subject: str, catalog: str) -> list[ScheduleItem]:
        return [i for i in self.items if i.subject == subject and i.catalog == catalog]

    def find_by_instructor(self, last_name: str) -> list[ScheduleItem]:
        return [i for i in self.items if i.instructor.split(',')[0] == last_name]
