
print("Hello! I'm Elth. I'm your algorithms bot.")
print("Before starting please tell me your first name")
first_name = input()
print("Please tell me your last name")
last_name = input()
print("And your gender?")
print("['Male', 'female']")
gender = input()
print("May I know your age?")
age = input()
while age.isdigit() == False :
	print("I couldn't quite get how that response can be your age :/ Please enter your valid age.")
	age = input()
print("Congratulations! Registration Successful.")
full_name = first_name + ' ' + last_name
print("Hello %s , How are you? For a sample of my work I can show you how to make a transpose of a 3X3 matrix."%(full_name))
rows = [None]*3
print("Enter the first row of the matrix(3 integers space seperated).")
rows[0] = input()
print("Enter the second row of the matrix(3 integers space seperated).")
rows[1] = input()
print("Enter the third row of the matrix(3 integers space seperated).")
rows[2] = input()
matrix = [list(map(int, i.split())) for i in rows]
t_matrix = [[matrix[j][i] for j in range(3)] for i in range(3)]
print("This is the transpose of the input matrix")
for i in range (3):
	print("Row %s : %s"%(i+1,str(t_matrix[i])))
