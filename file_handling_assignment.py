# Create a new text file named "my_file.txt" in write mode ('w')
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Python is awesome!\n")
    print("File 'my_file.txt' created and initial content written successfully.")
except PermissionError:
    print("Permission denied to create/write to 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File creation and writing process completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("\nContents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1\n")
        file.write("Appending line 2\n")
        file.write("Appending line 3\n")
    print("\nAdditional content appended to 'my_file.txt' successfully.")
except PermissionError:
    print("Permission denied to append to 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred: {e}")

# Error Handling
try:
    with open("non_existing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File 'non_existing_file.txt' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Error handling process completed.")
