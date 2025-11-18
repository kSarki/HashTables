from datetime import datetime


def recommend(schedule):
    print("\n" + "="*60)
    print(" "*15 + "SCHEDULE RECOMMENDATIONS")
    print("="*60)
    
    items = schedule.get_all_items()
    
    if not items:
        print("\nNo schedule items to analyze.")
        return
    
    print(f"\nAnalyzing {len(items)} schedule items...")
    
    meetings = []
    trainings = []
    interviews = []
    
    for item in items:
        title_lower = item.title.lower()
        if 'meeting' in title_lower:
            meetings.append(item)
        if 'training' in title_lower or 'workshop' in title_lower:
            trainings.append(item)
        if 'interview' in title_lower:
            interviews.append(item)
    
    print("\n--- RECOMMENDATIONS ---")
    print(f"✓ Total Meetings: {len(meetings)}")
    print(f"✓ Training/Workshop Sessions: {len(trainings)}")
    print(f"✓ Interviews Scheduled: {len(interviews)}")
    
    if len(items) > 0:
        print(f"\n→ You have {len(items)} scheduled items this week.")
        
        if len(meetings) > 5:
            print("→ Recommendation: You have many meetings. Consider consolidating some.")
        
        if len(trainings) > 0:
            print(f"→ Great! You have {len(trainings)} training session(s) for professional development.")
        
        if len(interviews) > 0:
            print(f"→ Note: {len(interviews)} interview(s) scheduled. Prepare accordingly!")
    
    print("\n--- TOP 3 UPCOMING ITEMS ---")
    for i, item in enumerate(items[:3], 1):
        print(f"\n{i}. {item.title}")
        print(f"   {item.date} at {item.time}")
        print(f"   Location: {item.location}")
    
    print("\n" + "="*60)
    print("Recommendation analysis complete!")
    print("="*60)
