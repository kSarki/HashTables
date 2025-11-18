from schedule import Schedule


def display_menu():
    print("\n" + "="*60)
    print(" "*20 + "SCHEDULE SEARCH PROGRAM")
    print("="*60)
    print("\nMenu Options:")
    print("1. View All Schedule Items")
    print("2. Search Schedule Items")
    print("3. Load Schedule from CSV")
    print("4. Exit")
    print("="*60)


def main():
    schedule = Schedule()
    csv_filename = "schedule_data.csv"
    
    print("\nWelcome to the Schedule Search Program!")
    print(f"Loading schedule from '{csv_filename}'...")
    
    if schedule.load_from_csv(csv_filename):
        print(f"Successfully loaded {schedule.get_count()} schedule items!")
    else:
        print("No schedule loaded. You can load one from the menu.")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\n--- ALL SCHEDULE ITEMS ---")
            schedule.display_all()
        
        elif choice == "2":
            search_term = input("\nEnter search term: ").strip()
            if search_term:
                print(f"\n--- SEARCH RESULTS FOR: '{search_term}' ---")
                results = schedule.search(search_term)
                schedule.display_items(results)
            else:
                print("Search term cannot be empty.")
        
        elif choice == "3":
            filename = input("\nEnter CSV filename (default: schedule_data.csv): ").strip()
            if not filename:
                filename = "schedule_data.csv"
            
            schedule = Schedule()
            if schedule.load_from_csv(filename):
                print(f"Successfully loaded {schedule.get_count()} schedule items!")
            else:
                print("Failed to load schedule.")
        
        elif choice == "4":
            print("\nThank you for using the Schedule Search Program!")
            print("Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
