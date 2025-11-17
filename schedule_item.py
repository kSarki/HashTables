class ScheduleItem:
    def __init__(self, date, time, title, description, location=""):
        self.date = date
        self.time = time
        self.title = title
        self.description = description
        self.location = location
    
    def __str__(self):
        return f"{self.date} {self.time} - {self.title} at {self.location}"
    
    def __repr__(self):
        return f"ScheduleItem(date='{self.date}', time='{self.time}', title='{self.title}')"
    
    def matches_search(self, search_term):
        search_term = search_term.lower()
        return (search_term in self.title.lower() or 
                search_term in self.description.lower() or 
                search_term in self.location.lower() or
                search_term in self.date or
                search_term in self.time)
    
    def display(self):
        print(f"\n{'='*60}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        if self.location:
            print(f"Location: {self.location}")
        print(f"{'='*60}")
