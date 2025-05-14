# Create a school portal for checking students grades

Is_user_a_student_of_this_school = str(input("Are you a student of this school input 'yes' or 'no' : "))
if Is_user_a_student_of_this_school.upper() == "YES":
    print("PORTAL LOADING !!! " * 3)
elif Is_user_a_student_of_this_school.upper() == "NO":
    print("Exiting...")
    exit()

def student_details():
    student_first_name = input('Input your first name : ')
    student_last_name = input('Input your last name : ')
    student_full_name = student_first_name.title() + " " + student_last_name.title()
    student_school = input("Enter school name : ")
    student_gender = input("Enter your gender (Male or Female) : ")
    student_exam_number = input(f"{student_full_name}, Please enter your registration/exam number : ")
    student_seat_number = input("Enter your seat number : ")
    print()
    print()
    print()
    print(f'Fullname : {student_full_name.title()}')
    print(f'SCHOOL NAME : {student_school.title()}')
    print(f'Gender : {student_gender.title()}')
    print(f'Exam/registration number : {student_exam_number}')
    print(f"Seat number : seat number {student_seat_number}")

def grade_calculation():
    print("The score inputed is from a scale of 1 - 100 !!!")
    English = int(input("Input your english score : "))
    Mathematics = int(input("Input your Mathematics score : "))
    Physics = int(input("Input your Physics score : "))
    Chemistry = int(input("Input your Chemistry score : "))
    ICT = int(input("Input your ICT score : "))
    Subjects_and_grade = {"English":English , "Mathematics":Mathematics, "Physics":Physics,"Chemistry":Chemistry,"ICT":ICT}
    print()
    print()
    print()
    print(f"Subjects: \n {Subjects_and_grade}")
    pass_mark = 50
    import math
    Cummulative_score = sum(Subjects_and_grade.values())
    number_of_subjects = len(Subjects_and_grade.values())
    Average_score = Cummulative_score/number_of_subjects
    print(f'your cummulative average score is {Average_score}')
    if Average_score>= 50 :
        print(f'Status : Pass !!!')
    elif Average_score< 50 :
        print(f'Status : Fail ')
student_details()
grade_calculation()


def tryagain():
    student_details()
    grade_calculation()

user_try_again = str(input("Do you want to check your score again (yes or no) ? "))
user_trial = 0
max_trial = 5
while user_trial<max_trial:
    if user_try_again.title() == "Yes":
        tryagain()
    user_trial+=1
    print(f'You have {max_trial - user_trial} trials left !!!')
    
    if user_try_again.title() == "No":
        print("Thank you!!")
        exit()

    if user_trial == max_trial:
        print("You've exceeded your maximum trial\n rerun to use portal !!")
        print("LOGGING OUT !!!")
        exit()
# Created by dami and enoch...
