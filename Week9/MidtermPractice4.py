from datetime import datetime, date
import math

def main():
    print("=== Welcome John Lourde Aquino ===")
    
    while True:
        total_pages = 0
        pages_read = 0
        
        # Loop for Total Pages
        while True:
            total_str = input("How many pages does the book have?: ")
            try:
                total_pages = int(total_str)
                if total_pages <= 0:
                    print("Invalid input. Total pages must be a positive number greater than 0.\n")
                    continue  # Restarts this specific prompt loop
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
                
        # Loop for Pages Read
        while True:
            read_str = input("How many pages have you read?: ")
            try:
                pages_read = int(read_str)
                if pages_read < 0:
                    print("Invalid input. Pages read cannot be a negative number.\n")
                    continue  # Restarts this specific prompt loop
                if pages_read > total_pages:
                    print(f"Invalid input. You cannot read more than the total pages ({total_pages}).\n")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
                
        # Date Input Loop
        issue_date = None
        due_date = None
        
        while True:
            try:
                issue_str = input("Issue date (YYYY-MM-DD): ")
                issue_date = datetime.strptime(issue_str, "%Y-%m-%d").date()
                
                due_str = input("Due date (YYYY-MM-DD): ")
                due_date = datetime.strptime(due_str, "%Y-%m-%d").date()
                
                if due_date < issue_date:
                    print("Due date cannot be before issue date. Please re-enter dates.\n")
                    continue  
                    
                break  
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.\n")

        # Calculations
        today = date.today()
        percentage = (pages_read / total_pages) * 100
        pages_left = total_pages - pages_read
        
        remaining_days = (due_date - today).days

        print(f"\nYou have read {percentage:.0f}% of the book.")
        print(f"You have {pages_left} pages left to read.")

        if pages_left == 0:
            print("You have finished the book!")
        elif remaining_days > 0:
            pages_per_day = math.ceil(pages_left / remaining_days)
            print(f"You should read {pages_per_day} pages per day.")
        else:
            print("The book must be returned now.")

        if remaining_days < 0:
            print("Your book is overdue.")
        elif remaining_days == 0:
            print("Your book is due today.")
        else:
            print(f"You have {remaining_days} days remaining.")

        break  

if __name__ == "__main__":
    main()
