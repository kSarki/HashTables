import sys
sys.path.insert(0, '..')
from shared import ScheduleItem, load_courses_from_csv
from .tree import BST


class Schedule:
    def __init__(self):
        self.tree = BST()

    def load_from_csv(self, filename: str) -> None:
        items = load_courses_from_csv(filename)
        for item in items:
            self.tree.insert(item.get_key(), item)

    def print_header(self) -> None:
        print(f"{'Subj':4} {'Catalog':6} {'Section':6} {'Component':8} "
              f"{'Sess':4} {'Units':3} {'TotEnrl':6} {'CapEnrl':6} Instructor")

    def print_results(self, results: list[ScheduleItem]) -> None:
        self.print_header()
        for item in results:
            item.print()

    def print_all(self) -> None:
        self.print_results(self.tree.inorder())

    def find_by_subject(self, subject: str) -> list[ScheduleItem]:
        return self.tree.find_by_prefix((subject,))

    def find_by_subject_catalog(self, subject: str, catalog: str) -> list[ScheduleItem]:
        return self.tree.find_by_prefix((subject, catalog))

    def find_by_instructor(self, last_name: str) -> list[ScheduleItem]:
        all_items = self.tree.inorder()
        return [i for i in all_items if i.instructor.split(',')[0] == last_name]
