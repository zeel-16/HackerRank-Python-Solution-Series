# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    n = int(input().strip())
    student = []
    for i in range(n):
        name =  input().strip()
        score = float(input().strip())
        student.append([name,score])
        
    
    unique_grades = set()
    for name , score in student:
        unique_grades.add(score)
    unique_grades = sorted(unique_grades)

if len(unique_grades)<2:
    print("No second highest")
else:
    second_lowest_grade = unique_grades[1]
    
    second_lowest_student  = []
    for name , score in student:
        if score == second_lowest_grade:
            second_lowest_student.append(name)
            
    second_lowest_student.sort()
    print("\n".join(second_lowest_student))
