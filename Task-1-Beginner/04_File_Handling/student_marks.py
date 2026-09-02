file = open("student.txt", "w")

name = input("Enter student name: ")
marks = input("Enter student marks: ")

file.write("Student Name: " + name + "\n")
file.write("Marks: " + marks)

file.close()

file = open("student.txt", "r")

print(file.read())

file.close()