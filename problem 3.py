print("Problem 03 ~ Assignment 4".center(42, "="))
print("\033[91m=" * 42)
print("\033[94mCMPE-103-MODULE-2-FILE-HANDLING-IN-PYTHON")
print("\033[91m=" * 42)

# writing a method in python where the user can write a multiple line of context
# and will store into a text file named "mylife.txt"

# pseudocode
# open, create a text file to store the input lines
with open("mylife.txt", "w") as problem_three_lines_file:
    # ask the user for an input that will serve as context lines
    # establish a loop that ask the user for a line until there is none
    while True:
         my_line = input("\033[93mEnter a line: ")
         # write the input line to the file
         problem_three_lines_file.write(my_line + "\n")
         # ask the user if there is more lines to input
         add_line = input("\033[96mAre there more lines y/n?: ")
         # if the user enter n, exit the loop
         if add_line.lower() == "n":
             break

# print the lines entered to the created file
print("\033[92m~" * 60)
print("\033[94mGreat! Your text file named mylife.txt is now saved and created.")
print("\033[92m~" * 60)