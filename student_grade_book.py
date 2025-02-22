# Student grade book, exercise 3

#Initializing the dictionary with students and their grades
students_grades = [
    {'name': 'Adam', 'grades': [100, 92, 87]},
    {'name': 'Kyle', 'grades': [99, 72, 79]},
    {'name': 'Anthony', 'grades': [10, 32, 54]},
]

# Takes in a students name and a list of their grades, then adds it to the students_grades list as a dict
def add_student(name:str, grades:list):
    students_grades.append({'name': name, 'grades': grades})

#Function for viewing every student in the dictionary
def view_students():
    for entry in students_grades:
        name = entry['name']
        grades = entry['grades']
        print(f"Student {name} has grades of {', '.join(str(grade) for grade in grades)}")

#Function for calculating the average grade based on a list of grades and returns it
def calculate_average_grade(grades:list):
    average = sum(grades) / len(grades)
    return f"{average:.2f}"

#Function for finding the highest grade that a student has and prints it
def find_highest_grade():
    highest_grades:list = []
    for entry in students_grades:
        # fetches name and grades from current student being iterated over
        name:str = entry['name']
        grades:list = entry['grades']
        # puts their name and finds highest grade by sorting the list then reversing it so index 0 is the highest
        highest_grades.append({'name': name, 'highest_grade': f"{sorted(grades, reverse=True)[0]:.2f}"})

    # Sorts the highest_grades list by its values 'highest_grade' entry, reverses it to make sure index 0 is highest
    result = sorted(highest_grades, key=lambda h:h['highest_grade'], reverse=True)[0]
    print(f"{result['name']} has the highest grade of {result['highest_grade']}")

#Function for finding the student with the lowest grade and prints it
def find_lowest_grade():
    lowest_grades: list = []
    for entry in students_grades:
        # fetches name and grades from current student being iterated over
        name: str = entry['name']
        grades: list = entry['grades']
        # puts their name and finds lowest grade by sorting their grades so index 0 is the lowest
        lowest_grades.append({'name': name, 'lowest_grade': f"{sorted(grades)[0]:.2f}"})

    # Sorts the highest_grades list by its values 'highest_grade' entry, reverses it to make sure index 0 is highest
    result = sorted(lowest_grades, key=lambda h: h['lowest_grade'])[0]
    print(f"{result['name']} has the lowest grade of {result['lowest_grade']}")

# Goes through students_grades looking for target_name. If it is found, it is deleted. If not, nothing happens
def remove_student(target_name:str):
    for index, entry in enumerate(students_grades):
        current_name:str = entry['name']
        if current_name == target_name:
            del students_grades[index]

# sorts students into dicts of their name and average grade, then returns them sorted based on optional descending arg
def sort_students_by_average(descending:bool=False):
    averages = []
    for entry in students_grades:
        # fetches name and grades for the current student being iterated over
        name = entry['name']
        grades = entry['grades']
        # calculates the average grade of the student
        average = sum(grades) / len(grades)
        # Creates a dict of the students name and their average, then adds it to a list
        averages.append({"name": name, "average": f"{average:.2f}"})

    # Sorts the dicts by the dicts 'average' key and orders it based on the optional descending arg
    results = sorted(averages, key=lambda a:a['average'], reverse=descending)
    return results

# Just put all user input needs into this function. So splitting, validating type, and creating bools from input
def user_prompt_validation(prompt:str, desired_type:type=str, comma_seperated:str=None):
    result = []
    user_input = input(prompt)
    if comma_seperated:
        user_input = user_input.replace(' ', '').split(comma_seperated)
        for value in user_input:
            result.append(desired_type(value))
    else:
        result = desired_type(user_input)

    if desired_type == bool:
        if user_input == 1:
            return True
        elif user_input == 2:
            return False

    return result

# Prompts user to continue
def user_continue_prompt():
    input("Enter any key to continue: ")

# Displays the main user interface
def user_interface():
    while True:
        # Main menu
        print("1. Add Student\n"
              "2. View Students\n"
              "3. Calculate Average Grade\n"
              "4. Find Highest Grade\n"
              "5. Find Lowest Grade\n"
              "6. Sort Students by Average\n"
              "7. Remove Student\n"
              "8. Exit\n")

        # Gets user input then clears screen
        menu_input = input("Enter your choice: ")

        # Runs the corresponding function based on the users selection
        match menu_input:
            # adds student to grade book
            case '1':
                try:
                    # takes in students name and grade then calls add_student
                    student_name = user_prompt_validation("Enter student name: ", str)
                    grades = user_prompt_validation("Enter grades (comma seperated): ", int, ',')
                    add_student(student_name, grades)
                    print(f"Added student {student_name} with grades {grades}")
                    user_continue_prompt()
                except Exception as e:
                    print(f"Error occurred: {e}")

            # Lists students are their grades
            case '2':
                view_students()
                user_continue_prompt()

            # Lists students average grades
            case '3':
                # iterates through students_grades, formats the info and calculates their average based w calculate_average_grade
                for entry in students_grades:
                    name = entry['name']
                    grades = entry['grades']
                    print(f"{name} has an average of {calculate_average_grade(grades)}")
                user_continue_prompt()

            # Finds student with highest grade
            case '4':
                find_highest_grade()
                user_continue_prompt()

            # Finds student with lowest grade
            case '5':
                find_lowest_grade()
                user_continue_prompt()

            # Lists students by average in ascending or descending order
            case '6':
                while True:
                    try:
                        # grabs desired order and calls sort_students_by_average based on it, then formats/prints whats returned
                        order = user_prompt_validation("Sort Students by Average Grade (1 for descending, 2 for ascending): ", int)
                        match order:
                            case 1:
                                students_by_average = sort_students_by_average(True)
                            case 2:
                                students_by_average = sort_students_by_average(False)
                            case _:
                                students_by_average = None
                                print(f"{order} is not a valid input")
                                user_continue_prompt()

                        if students_by_average:
                            for index, entry in enumerate(students_by_average):
                                name = entry['name']
                                average = entry['average']
                                print(f"{index + 1}: {name} has an average of {average}")
                            user_continue_prompt()
                            break

                    except ValueError as e:
                        print(f"ValueError during case 6: {e}")

            # Removes student from list
            case '7':
                try:
                    # grabs students name and runs the remove_student func
                    student_name = user_prompt_validation("Enter a student name to remove: ", str)
                    remove_student(student_name)
                    print(f"Removed {student_name}")
                    user_continue_prompt()
                except Exception as e:
                    print(f"An error has occurred: {e}")

            # Exits program
            case '8':
                raise KeyboardInterrupt

            # catches invalid inputs
            case _:
                print(f"{menu_input} is not a valid input")
                user_continue_prompt()

# entrypoint
if __name__ == '__main__':
    try:
        # runs the user interface loop
        user_interface()
    except KeyboardInterrupt:
        # Exits gracefully
        print("\nExiting...")
        exit(0)
