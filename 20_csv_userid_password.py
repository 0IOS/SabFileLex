import csv

def create_csv():
    n = int(input("How many users? "))
    f = open("passwords.csv", "w", newline="")
    writer = csv.writer(f)
    writer.writerow(["UserID", "Password"])
    for i in range(n):
        uid = input("Enter user ID: ")
        pwd = input("Enter password: ")
        writer.writerow([uid, pwd])
    f.close()
    print("passwords.csv created successfully!")

def search_password():
    search_id = input("Enter user ID to search: ")
    f = open("passwords.csv", "r")
    reader = csv.reader(f)
    found = False
    for row in reader:
        if row and row[0] == search_id:
            print("Password for", search_id, "is:", row[1])
            found = True
            break
    f.close()
    if not found:
        print("User ID", search_id, "not found!")

print("1. Create CSV")
print("2. Search Password")
choice = input("Enter your choice: ")

if choice == '1':
    create_csv()
elif choice == '2':
    search_password()
else:
    print("Invalid choice!")
