import sys
from statistics import mean
import time
import os
admins = {'Python':'bacon', 'Maks':'qwerty'}
studensts = {'Alex': [92, 76, 88], 'Jeff': [78, 88, 93], 'Sam': [89, 92, 93]}

class Grade(object):
    def __init__(self):
        print(
        """\t\tWelcome to grade central

        [1] - Enter Grades
        [2] - Remove Student
        [3] - Student Average Grades
        [4] - Exit

    What wolud you like to do taday? (Enter a number)
        """)
        while True:
            number = input()
            try:
                if int(number) in range(1, 5):
                    break
                else:
                    print("You must enter a number between 1 and 4!!!")

            except:
                print("You must enter a number between 1 and 4!!!")
                continue

        print("You choice number: ", number)
        if int(number) == 1:
            Grade.enter(self)

        elif int(number) == 2:
            Grade.removing(self)

        elif int(number) == 3:
            Grade.avg(self)

        elif int(number) == 4:
            Grade.close(self)

    def enter(self):
        while True:
            student = input("Enter the student's name: \t")
            student = student.title()
            if student in studensts:
                    break
            else:
                print("You must enter a existing student name!!!")
                print("List of students: ", end="")
                print([element for element in studensts.keys()])
                continue

        while True:
            grade = input("Enter the student's score: \t")
            try:
                grade = int(grade)
                break
            except:
                print("You must enter the number of points!!!")
                continue
        studensts[student].append(int(grade))
        print("adding grade...")
        time.sleep(1)
        print("the rating {} has been added students {}: \t".format(grade, student), end="")
        print(studensts[student])
        input("\nTo return to the main menu, press enter.")

    def removing(self):
        while True:
            print("Do you really want to delete a student?")
            question = input("\t\t[yes] or [no] \n")
            question = question.lower()
            if question == "yes":
                while True:
                    removable = input("What student to remove?: \t")
                    removable = removable.title()
                    if removable in studensts:
                            break
                    else:
                        print("You must enter a existing student name!!!")
                        print("List of students: ", end="")
                        print([element for element in studensts.keys()])
                        continue

                del studensts[removable]
                print("removing student...")
                time.sleep(2)
                print("Done")
                time.sleep(1)
                print(studensts)
                input("\nTo return to the main menu, press enter.")
                break
            elif question == "no":
                break
            else:
                print("you have to answer 'yes' or 'no'!!!")
                continue

    def avg(self):
        while True:
            ask = input("Enter the name of the student you want to calculate the grade point average. \t")
            ask = ask.title()
            if ask in studensts:
                    break
            else:
                print("You must enter a existing student name!!!")
                print("List of students: ", end="")
                print([element for element in studensts.keys()])
                continue
        time.sleep(1)
        print("The average student {} grade is: ".format(ask), end="")
        print(mean(studensts[ask]))
        time.sleep(1)
        input("\nTo return to the main menu, press enter.")
    def close(self):
        while True:
            print("Do you really want to leave the program?")
            quit = input("\t\t[yes] or [no] \n")
            quit = quit.lower()
            if quit == "yes":
                print("Thank you and see you next time...")
                time.sleep(1)
                sys.exit()
            elif quit == "no":
                break
            else:
                print("you have to answer 'yes' or 'no'!!!")
                continue

class main(object):
    def __init__(self):
        while True:
            login = input("Enter login: ")
            if login in admins:
                while True:
                    password = input("Enter password: ")
                    if admins[login] == password:
                        print("Welcome, {} \n".format(login))
                        while True:
                            Grade()
                    else:
                        print("Wrong password!!!")
                break
            else:
                print("Wrong login!!!")

main()