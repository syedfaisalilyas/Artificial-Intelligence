# Task1
weightInKgs=int(input("Enter weight into kgs"))
weightInPounds=weightInKgs*2.2046
print(weightInPounds)

# Task2
prices =[20,50,80,10,56,89]
sum=0
for i in prices:
  sum+=i
print(sum)

# Task3
def findMax(a,b):
  if a>b & a==b:
    return a
  else:
    return b
print(findMax(8,9))

# Task4
def deepMind(n):
  if n%3==0:
    return "deep"
  elif n%5==0:
    return "mind"
  elif n%3==0 & n%5==0:
    return "deepmind"
  else:
    return "false input"
print(deepMind(15))

# Task5
listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(listA)):
    if listA[i] < 5:
        listA[i] = 0
    elif listA[i] > 5:
        listA[i] = 1
    else:
        listA[i] = 5

print(listA)



# Task6
listA = [1,2,3,4,5,6,7,8,9,10]
result = [x ** 2 for x in listA]
print(result)

# Task7
b1 = ['Hello', 'in','first']
b2 = ['Students','the','recitation']
print(b1+b2)

# Task8
ali_marks = {
    "Mathematics": (100, 85),
    "Physics": (100, 78),
    "Chemistry": (100, 92),
    "English": (100, 88),
    "Computer Science": (100, 95)
}
for course, (total_marks, obtained_marks) in ali_marks.items():
    print(f"Subject: {course}")
    print(f"Total Marks: {total_marks}")
    print(f"Obtained Marks: {obtained_marks}")
    print("\n")
   
# Task 9
class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def addition(self):
        return self.n1 + self.n2

    def multiplication(self):
        return self.n1 * self.n2

    def division(self):
        if self.n2 != 0:
            return self.n1 / self.n2
        else:
            return "Error! Division by zero."

    def square(self):
        return self.n1 ** 2, self.n2 ** 2

    def subtraction(self):
        return self.n1 - self.n2
    
calc = Calculator(10, 5)
print("Addition:", calc.addition())           
print("Multiplication:", calc.multiplication())  
print("Division:", calc.division())           
print("Square:", calc.square())               
print("Subtraction:", calc.subtraction())     