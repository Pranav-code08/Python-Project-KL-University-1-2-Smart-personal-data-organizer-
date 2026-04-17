from models.person import Person
from utils.validators import validate_age, validate_email, validate_phone
from utils.file_ops import read_json, write_json, write_csv
from analysis.analyzer import analyze_data
from analysis.visualizer import show_charts

# Load data from JSON (if file empty, returns [])
data = read_json()

def add_record():
    global data
    try:
        name = input("Enter name: ").strip()
        age = input("Enter age: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()
        gender = input("Enter gender: ").strip()
        city = input("Enter city: ").strip()
        interests = input("Enter interests (comma-separated): ").split(",")

        # Validations
        if not validate_age(age):
            print("Invalid age")
            return
        if not validate_email(email):
            print("Invalid email")
            return
        if not validate_phone(phone):
            print("Invalid phone")
            return

        person = Person(name, int(age), phone, email, gender, city, interests)
        data.append(person.to_dict())
        write_json(data)
        print("Record added successfully")

    except Exception as e:
        print("Error:", e)


def display_all():
    if not data:
        print("No records found")
        return

    print("\n=== All Records ===")
    for record in data:
        print("-" * 40)
        for key, value in record.items():
            print(f"{key}: {value}")


def search():
    key = input("Enter name to search: ").lower()
    found = False
    for record in data:
        if key in record["name"].lower():
            print("-" * 40)
            for k, v in record.items():
                print(f"{k}: {v}")
            found = True

    if not found:
        print("No record found")


def menu():
    while True:
        print("\n====== SMART PERSONAL DATA ORGANIZER ======")
        print("1. Add Record")
        print("2. Display All Records")
        print("3. Search by Name")
        print("4. Export Data to CSV")
        print("5. Analyze Data")
        print("6. View Charts")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            display_all()
        elif choice == "3":
            search()
        elif choice == "4":
            write_csv(data)
            print("Data exported to CSV successfully")
        elif choice == "5":
            analyze_data(data)
        elif choice == "6":
            show_charts(data)
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()