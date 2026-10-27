#Add student records
student = {
    "name" : ["Nisha","Harsha","Harshita","Parnika"],
    "id" : [101,102,103,104],
    "marks" : [91,93,94,96]
}

#View all student records
print(student.items())

#Search for student using their ID
print("\n",student.get("id"))

#Update student details
print("\n", student.update({"marks"[2] : 95}))
