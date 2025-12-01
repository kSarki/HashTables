"""Entry point for running the BST version of the course schedule program."""

import sys
sys.path.insert(0, 'bst_app')
from bst_app.schedule import Schedule


def main():
    """Main function to run the BST-based course schedule search."""
    schedule = Schedule()
    schedule.load_from_csv("courses.csv")
    print(f"Course schedule loaded (BST version). Tree height: {schedule.get_tree_height()}")

    while True:
        print("\n1. Display all  2. By subject  3. By subject+catalog  4. By instructor  5. Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            schedule.print_all()
        elif choice == "2":
            results = schedule.find_by_subject(input("Subject: ").strip())
            schedule.print_results(results)
        elif choice == "3":
            subj = input("Subject: ").strip()
            cat = input("Catalog: ").strip()
            schedule.print_results(schedule.find_by_subject_catalog(subj, cat))
        elif choice == "4":
            results = schedule.find_by_instructor(input("Instructor last name: ").strip())
            schedule.print_results(results)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
