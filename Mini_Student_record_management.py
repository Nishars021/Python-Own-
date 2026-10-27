#Add student records
student = {
    "name" : ["Nisha","Harsha","Harshita","Parnika"],
    "id" : [101,102,103,104],
    "marks" : [91,93,94,96]
}

# #View all student records
# print(student.items())

#Search for student using their ID
s_id = int(input("Enter ID : "))

if s_id in student["id"] : 
    i = student["id"].index(s_id)

    print("Name : ",student["name"][i])
    print("Marks : ",student["marks"][i])
else :
    print("Student not found")



