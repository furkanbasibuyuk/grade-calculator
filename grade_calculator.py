def grade_calculator(line):
    line = line[:-1]
    list1 = line.split(",")
    name = list1[0]
    grade1 = int(list1[1])
    grade2 = int(list1[2])
    grade3 = int(list1[3])
    optimum_grade = grade1*(3/10) + grade2*(3/10) + grade3*(4/10)
    
    if (optimum_grade >= 90):
        letter = "AA"
    elif (optimum_grade >= 85):
        letter = "BA"
    elif (optimum_grade >= 80):
        letter = "BB"
    elif (optimum_grade >= 75):
        letter ="CB"
    elif (optimum_grade >= 70):
        letter = "CC"
    elif (optimum_grade >= 65):
        letter = "DC"
    elif (optimum_grade >= 60):
        letter = "DD"
    elif (optimum_grade >= 55):
        letter = "FD"
    else:
        letter = "FF"
    
    return name + "---------------------> " + letter + "\n"

with open ("grades.txt","r",encoding="utf-8") as file:
    
    grade_list = []
    
    for i in file:
        grade_list.append(grade_calculator(i))
        
    with open ("final_grades.txt","w") as file2:
        for i in grade_list:
            file2.write(i)