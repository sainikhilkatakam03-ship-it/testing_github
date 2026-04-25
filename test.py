print('Hello World')

def calculate_total(marks):
    """
    Calculates and returns the total sum of all marks in the list.
    """
    return sum(marks)


def calculate_average(marks):
    """
    Calculates and returns the average of marks by calling calculate_total().
    """
    total = calculate_total(marks)
    return total / len(marks)


def get_grade(average):
    """
    Returns a grade based on the average:
    'A' if average > 90,
    'B' if average > 75,
    otherwise 'C'.
    """
    if average > 90:
        return "A"
    elif average > 75:
        return "B"
    else:
        return "C"


def display_report(marks):
    """
    Displays the total, average, and grade by calling the respective functions.
    """
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)

    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")


# Test the solution
marks_list = [88, 76, 95, 60, 82]
display_report(marks_list)