l = []
temp_list = []  # declaration of lists that are used in program
d = {}
id = []
last = []
first = []
year = []
term = []
degree = []


def display(temp_list):  # function that displays students records
    for i in temp_list:  # For each record in list
        print(i, end='')  # print data


def lastname():  # function that prints records based on last name
    global l, last, id, first, year, term, term, degree


str = input("Enter certain string:")  # Read pattern from user
str = str.lower()
for i in range(len(last)):  # For each record in list
    last[i] = last[i].lower()  # store data in lower case
print(l[0])
for i in range(len(last)):  # for each record in list
    if str in last[i]:  # check if entered substring is in main string
        print(id[i], end=" ")  # If present then print that record
print(last[i].title(), end="\t")  # print data of that record from lists
print(first[i], end="\t")
print(year[i], end="\t")
print(term[i], end="\t")
print(degree[i])


def grad_year():  # method to print record based on year
    y = int(input("Enter year"))  # Read input from user


for i in range(len(year)):  # For each record in list
    if y == int(year[i]):  # check for year
        print(id[i], end=" ")  # If year is found then print that record
print(last[i], end="\t")  # print data of that record from lists
print(first[i], end="\t")
print(year[i], end="\t")
print(term[i], end="\t")
print(degree[i])


def summary():  # method that displays summary
    total = len(id)


degree_set = list(set(degree))  # identify unique degrees from list
for i in degree_set:  # For each unique degree in list
    print("Number of students in degree", end=' ')  # print number of students
print(i, end=':')
print(degree.count(i))
print("Percent of students in degree", end=' ')  # print percent of students in that degree
print(i, end=':')
print((degree.count(i) * 100) / total)


def main():  # main method definition
    global l, last, id, first, year, term, term, degree


f = open("Students.txt", "r")  # open file in read mode
l = list(f.readlines())  # store data into list
temp_list = l[:]
for i in range(len(l)):  # For each record in list, obtain data in required format.
    l[i] = l[i][:-1]

l[i] = l[i].replace(" ", " ")

l[i] = " ".join(l[i].split())

for i in range(1, len(l)):  # For each record, store the details in relevant lists
    temp = l[i].split(" ")
id.append(temp[0])
last.append(temp[1])
first.append(temp[2])
year.append(temp[3])
term.append(temp[4])
degree.append(temp[5])
while (1):  # print menu until user inputs 5.
    print("1.display all student records")  # print choices on console
    print("2.display student whose last name begins with")
    print("3.display students whose graduation year is:")
    print("4.Summary report")
    print("5.quit")
    ch = int(input("Enter choice"))  # Read choice from user
    if ch == 1:
        display(temp_list)  # Call display() if ch is 1
    elif ch == 2:
        lastname()  # call lastname() if ch is 2
    elif ch == 3:
        grad_year()  # call grad_year() if ch is 3
    elif ch == 4:
        summary()  # call summary() if ch is 4
    elif ch == 5:
        exit(0)  # exit if input is 5
    else:
        print("Enter valid input")
        continue

main()  # call the main method to start the execution
