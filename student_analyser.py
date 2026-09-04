students = [
    {"name": "Aman", "marks": 87},
    {"name": "Riya", "marks": 74},
    {"name": "Rahul", "marks": 92},
    {"name": "ajay", "marks": 34}
]

def get_grade():
    for i in students:
      if i["marks"] >= 90:
        return "A+ grade"
      elif i["marks"] >= 80:
        return "A grade"  
      elif i["marks"] >= 70:
        return "B grade"
      elif i["marks"] >= 60:
        return "C grade"
      elif i["marks"] >= 50:
        return "D grade"
      else:
        return "F grade"
        
def get_average():
    total = 0
    for i in students:
        total += i["marks"]
    return total/len(students)
    
    
def find_highest():
    highest = 0
    highest_student = None
    for i in students:
       if i["marks"] > highest:
            highest = i["marks"] # so that highest compare it self with every value in marks if it doesn't save the old value it will always compare it with its initial value not value in marks.
            highest_student = i
    if highest_student:
        return f"name {highest_student['name']} : marks {highest_student['marks']}"
    else:
       return "no student found"
       
    
def lowest():
     lowest = students[0]["marks"] #similar to nested dictionary 
     lowest_student = students[0]
     for i in students:
         if i["marks"] < lowest:
            lowest = i["marks"]
            lowest_student = i
     return f"name {lowest_student['name']} : marks {lowest_student['marks']}" #return stops the for loop so always use return outside of for loop block  
def pas():
    var = []
    for i in students:
        if i["marks"] > 50:
            var.append(i) 
    return f"number of students passed are {len(var)}\nnumber of students failed are {len(students) - len(var)}\npass percentage {(len(var)/len(students))*100}%" 
#easy peasy cheeze 

                                                                                                                           
name = input("enter name of the student  \n:")
marks = int(input ("enter marks of the student \n :"))

student = {
"name" : name,
"marks" : marks
}
students.append(student)

grade = get_grade()
print(grade)

average = get_average()
print(f"average marks of students is  {average}")

highest = find_highest()
print(f"highest score in students\n{highest}")

low = lowest()
print(f"lowest score in students\n{low}")

passed = pas()
print(passed)