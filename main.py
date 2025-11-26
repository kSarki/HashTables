from schedule import Schedule

def main():
    schedule = Schedule()
    schedule.load_from_csv("courses.csv")
    print("Schedule loaded.")

    while True:
        print("\n1. Display all  2. By subject  3. By subject+catalog  4. By instructor  5. Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            schedule.print_all()
        elif choice == "2":
            results = schedule.find(subject=input("Subject: ").strip())
            schedule.print_results(results)
        elif choice == "3":
            subj = input("Subject: ").strip()
            cat = input("Catalog: ").strip()
            schedule.print_results(schedule.find(subject=subj, catalog=cat))
        elif choice == "4":
            results = schedule.find(instructor=input("Instructor last name: ").strip())
            schedule.print_results(results)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
