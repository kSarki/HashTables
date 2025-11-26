from schedule import Schedule

def main():
    schedule = Schedule()
    schedule.load_from_csv("schedule_data.csv")
    print(f"Loaded {schedule.count()} items.")

    while True:
        print("\n1. Display all  2. Search  3. Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            schedule.print_all()
        elif choice == "2":
            term = input("Search: ").strip()
            schedule.print_results(schedule.search(term))
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
