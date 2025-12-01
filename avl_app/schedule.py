"""Schedule adapter using AVL Tree for course storage."""

import sys
sys.path.insert(0, '..')
from shared import ScheduleItem, load_courses_from_csv
from .tree import AVL


class Schedule:
    """
    Course schedule manager using AVL Tree as the underlying data structure.
    
    Courses are stored with composite keys (subject, catalog, section).
    AVL self-balancing ensures O(log n) operations even with sorted input.
    """
    
    def __init__(self):
        """Initialize schedule with empty AVL tree."""
        self.tree = AVL()

    def load_from_csv(self, filename: str) -> None:
        """Load courses from CSV file into the AVL tree."""
        items = load_courses_from_csv(filename)
        for item in items:
            self.tree.insert(item.get_key(), item)

    def print_header(self) -> None:
        """Print column headers for course output."""
        print(f"{'Subj':4} {'Catalog':6} {'Section':6} {'Component':8} "
              f"{'Sess':4} {'Units':3} {'TotEnrl':6} {'CapEnrl':6} Instructor")

    def print_results(self, results: list[ScheduleItem]) -> None:
        """Print a list of courses with header."""
        self.print_header()
        for item in results:
            item.print()

    def print_all(self) -> None:
        """Display all courses in sorted order via in-order traversal."""
        self.print_results(self.tree.inorder())

    def find_by_subject(self, subject: str) -> list[ScheduleItem]:
        """Find all courses matching the given subject code."""
        return self.tree.find_by_prefix((subject,))

    def find_by_subject_catalog(self, subject: str, catalog: str) -> list[ScheduleItem]:
        """Find all courses matching subject and catalog number."""
        return self.tree.find_by_prefix((subject, catalog))

    def find_by_instructor(self, last_name: str) -> list[ScheduleItem]:
        """Find all courses taught by instructor with given last name."""
        all_items = self.tree.inorder()
        return [i for i in all_items if i.instructor.split(',')[0] == last_name]

    def get_tree_height(self) -> int:
        """Return the height of the underlying AVL tree."""
        return self.tree.height()
