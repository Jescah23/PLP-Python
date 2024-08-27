# Task 1: File Creation
try:
    with open('my_file.txt', 'w') as file:
        file.write("This is the first line.\n")
        file.write("Here is the second line with a number: 123\n")
        file.write("And this is the third line.\n")
    print("File 'my_file.txt' created and written successfully.")

except PermissionError:
    print("Permission denied: Unable to write to the file.")
except Exception as e:
    print(f"An error occurred while creating or writing to the file: {e}")

finally:
    print("File creation step completed.")

# Task 2: File Reading and Display
try:
    with open('my_file.txt', 'r') as file:
        contents = file.read()
        print("\nContents of 'my_file.txt':")
        print(contents)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except PermissionError:
    print("Permission denied: Unable to read the file.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

finally:
    print("File reading step completed.")

# Task 3: File Appending
try:
    with open('my_file.txt', 'a') as file:
        file.write("Appending the fourth line.\n")
        file.write("Appending the fifth line with text.\n")
        file.write("Appending the sixth line with another number: 456\n")
    print("Additional lines appended successfully.")

except PermissionError:
    print("Permission denied: Unable to append to the file.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

finally:
    print("File appending step completed.")
