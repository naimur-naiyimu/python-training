def add_record(database, name, phone_number, blood_group):
    record = {"Name": name, "Phone Number": phone_number, "Blood Group": blood_group}
    database.append(record)
    print("Record added successfully!")

def display_records(database):
    if not database:
        print("No records found.")
    else:
        print("Database Records:")
        for i, record in enumerate(database, start=1):
            print(f"{i}. Name: {record['Name']}, Phone Number: {record['Phone Number']}, Blood Group: {record['Blood Group']}")

def find_record(database, search_key, search_value):
    found_records = []
    
    for record in database:
        if record.get(search_key) == search_value:
            found_records.append(record)

    if not found_records:
        print(f"No records found with {search_key} = {search_value}.")
    else:
        print("Found Records:")
        for i, record in enumerate(found_records, start=1):
            print(f"{i}. Name: {record['Name']}, Phone Number: {record['Phone Number']}, Blood Group: {record['Blood Group']}")

# Database initialization (empty list)
blood_group_database = []

while True:
    print("\nOptions:")
    print("1. Add Record")
    print("2. Display Records")
    print("3. Find Record by Name")
    print("4. Find Record by Blood Group")
    print("5. Exit")

    choice = input("Enter your choice (1, 2, 3, 4, or 5.): ")

    if choice == "1":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        blood_group = input("Enter blood group: ")
        add_record(blood_group_database, name, phone_number, blood_group)
    elif choice == "2":
        display_records(blood_group_database)
    elif choice in ["3", "4"]:
        if choice == "3":
            search_key = "Name"
        elif choice == "4":
            search_key = "Blood Group"
        search_value = input(f"Enter the {search_key} to search: ")
        find_record(blood_group_database, search_key, search_value)
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")