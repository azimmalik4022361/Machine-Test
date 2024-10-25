import pandas as pd
import os

# Define the Excel file name
file_name = 'users.xlsx'

# Function to add a user
def add_user():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    
    # Create a DataFrame for the new user
    new_user = pd.DataFrame([[name, email, phone]], columns=['Name', 'Email', 'Phone Number'])
    
    # Check if the file exists
    if os.path.exists(file_name):
        # Append to existing file
        new_user.to_excel(file_name, mode='a', header=False, index=False)
    else:
        # Create a new file
        new_user.to_excel(file_name, index=False)

    print("User added successfully!")

# Function to display users
def display_users():
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
        print("\nStored Users:")
        print(df.to_string(index=False))
    else:
        print("No users found!")

# Main function to run the program
def main():
    while True:
        print("\nOptions:")
        print("1. Add User")
        print("2. Display Users")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            add_user()
        elif choice == '2':
            display_users()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
