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
# write the input line to the file
# ask the user if there is more lines to input
# if the user enter n, exit the loop
# print the lines entered to the created file