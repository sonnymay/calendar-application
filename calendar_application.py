import datetime

# In-memory data storage for events
events = {}

def print_menu():
    print("---- Calendar Application ----")
    print("1. Add Event")
    print("2. View Events")
    print("3. Delete Event")
    print("4. Exit")
    
def add_event():
    date_str = input("Enter event date (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        title = input("Enter event title: ")
        
        if date in events:
            events[date].append(title)
        else:
            events[date] = [title]
            
        print("Event added successfully!")
        
    except ValueError:
        print("Invalid date format")

def view_events():
    date_str = input("Enter date to view events (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        
        if date in events:
            print(f"Events on {date_str}:")
            for event in events[date]:
                print(f" - {event}")
        else:
            print(f"No events on {date_str}")

    except ValueError:
        print("Invalid date format")

def delete_event():
    date_str = input("Enter date of the event to delete (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        
        if date in events:
            print(f"Events on {date_str}:")
            for idx, event in enumerate(events[date], start=1):
                print(f"{idx}. {event}")
            event_idx = int(input("Enter the number of the event you want to delete: "))
            
            if 1 <= event_idx <= len(events[date]):
                del events[date][event_idx-1]
                print("Event deleted successfully!")
            else:
                print("Invalid event number")
        else:
            print(f"No events on {date_str}")

    except ValueError:
        print("Invalid date format or event number")
        

while True:
    print_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_event()
    elif choice == "2":
        view_events()
    elif choice == "3":
        delete_event()
    elif choice == "4":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
