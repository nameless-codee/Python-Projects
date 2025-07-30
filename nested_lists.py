if __name__ == '__main__':
    students = []

    for _ in range(int(input('Enter the number of students: '))):
        name = input('Enter the name of the student: ')
        score = float(input('Enter the score of the student: '))
        students.append([name, score])

    # Find unique scores and sort them to find the second lowest score
    # Using set to get unique scores and then sorting them (without any duplicates)
    # sorted() will sort the scores in ascending order
    unique_scores = sorted(set(score for _, score in students))
    second_lowest_score = unique_scores[1]

    # Get students with the second lowest score
    second_lowest_students = [name for name, score in students if score == second_lowest_score]

    # Prints names alphabetically
    for student in sorted(second_lowest_students):
        print(student)