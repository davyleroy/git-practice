# define a list of courses
courses = [
    "Python Programming",
    "Web Development",
    "Data Science",
    "Machine Learning"
]

# display the menu of courses
print("Select a course:")
for i in range(len(courses)):
    print(f"{i+1}. {courses[i]}")

# prompt the user for their selection
selection = int(input("Enter the number of the course you want to take: "))

# executing the corresponding code block based on the user's selection
if selection == 1:
    print("You have selected Python Programming.")
    # add code to start the Python Programming course
elif selection == 2:
    print("You have selected Web Development.")
elif selection == 3:
    print("You have selected Data Science.")
elif selection == 4:
    print("You have selected Machine Learning.")
else:
    print("Invalid selection.")
