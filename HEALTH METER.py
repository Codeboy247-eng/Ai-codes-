# This is a Health-meter program code
import time
import sys


def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def patient_health_analysis():
    patient_name = str(input("Please enter your name dear patient : "))
    patient_gender = str(input("Are you a Male or Female (input 'M' or 'F') ? "))

    if patient_gender.upper() == "M":
        pronoun = "Mr"
        print(f'Welcome {pronoun} {patient_name.title()}')

    elif patient_gender.upper() == "F":
        pronouns = "Miss or Mrs"
        print(f'Welcome {pronouns} {patient_name.title()}')
    else:
        print("Check your input!!!")

    patient_weight = eval(input("Please input your weight(Weight in KG) : "))

    patient_height = eval(input("Please input your height(Height in Fts) : "))
    patient_height_in_meters = patient_height * 1.83
    patient_bmi = patient_weight/patient_height_in_meters**2
    print()
    type_text(""""> Analyzing...""")
    type_text(f"PATIENT'S INFORMATION : \n")
    type_text(f'PATIENT NAME----> {patient_name}')
    type_text(f'Patient bmi(body-mass index) ----> {patient_bmi}')
    if patient_bmi >= 18.5 and patient_bmi <= 24.9:
        type_text("<Smiles> You're in the healthy range\n Keep it up !!!")
    elif patient_bmi < 18.5:
        type_text("Dear Patient, your body mass index is lower than the normal range and approaching underweight....")
        see_remedy = input("Press enter to see remedy")
        type_text("""> Increase caloric intake : \n Gradually add more calories to your diet by incorporating nutrient-dense foods\n """)
        type_text("""> Foods such as Whole grains,lean proteins, healthy fats, and diary products""")
        type_text("""> You should also engage in resistance exercises to increase muscle mass""")
    elif patient_bmi > 24.9:
        type_text("""Dear Patient, your body mass index is higher than the normal range and approaching Obesity or Overweight ...""")
        see_remedy = input("Press enter to see remedy")
        type_text("""> Limit the intake of processed foods like sugary beverages, and high calorie snacks...""")
        type_text("""Aim for at least 150 minutes or Two and half hours of moderate-intensity cardio per week to burn calories...""")


def check_health_status_again():
    do_you_want_to_use_again = input("If you want to check again input 'y',if not input 'n' : ")
    if do_you_want_to_use_again.lower() == 'y':
        while True:
            patient_health_analysis()
    elif do_you_want_to_use_again.lower() == 'f':
        type_text("""Thank you for using our program, and remember 'Health is Wealth'!""")
        type_text("""Exiting...""")
        exit()


patient_health_analysis()
check_health_status_again()

print("Created by Bamidele Damilola...")
