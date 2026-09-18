Name = input("Enter your Name: ")
Age = int(input("Enter Age: "))
City = input("Enter City: ")
College = input("Enter College: ")
Currentlearningtopic = input("Enter Current LearningTopic: ")
YearsOfExp = float(input("How many years of Experience: "))
IsLikePython = input("Do you like Python? yes/no: ").lower()
salary_input = input("Expected Salary(e,g., 200k or 200000): ")

#Convert Salary if user user enters "200k" format
if salary_input.endswith("k"):
    ExpectedSalary = int(float(salary_input[:-1]) * 1000)
else:
    ExpectedSalary = int(salary_input)

#Convert yes/no to boolean
LikePythonBool = (IsLikePython == "yes")

print("\n------- USER PROFILE ---------")

print(f"Name:{Name} | DataType: {type(Name)}")
print(f"Age:{Age} | DataType: {type(Age)}")
print(f"City:{City} | DataType: {type(City)}")
print(f"College:{College} | DataType: {type(College)}")
print(f"Currentlearningtopic:{Currentlearningtopic} | DataType: {type(Currentlearningtopic)}")
print(f"YearsOfExp:{YearsOfExp} | DataType: {type(YearsOfExp)}")
print(f"IsLikePython:{LikePythonBool} | DataType: {type(LikePythonBool)}")
print(f"ExpectedSalary:{ExpectedSalary} |  Datatype: {type(ExpectedSalary)}")
