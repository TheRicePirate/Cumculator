def measurements():
    print("")
    print("========================")
    print("Enter 1 to input metric system units.")
    print("Enter 2 to input imperial system units.")
    print("========================")
    print("")


def gender():
    print("")
    print("========================")
    print("Enter 1 if you are male.")
    print("Enter 2 if you are female.")
    print("========================")
    print("")


def activity_levels():
    print("")
    print("========================")
    print("Enter 1 if you are sedentary.")
    print("Enter 2 if you are lightly active.")
    print("Enter 3 if you are moderately active.")
    print("Enter 4 if you are very active.")
    print("Enter 5 if you are extra active.")
    print("========================")
    print("")


print("Enter any number other than 1 to input metric system values.")
print("============================================================")
user_measurement_system = int(input("Enter 1 to switch to the imperial system: "))

BMR_raw = 0
daily_calories = 0


if user_measurement_system == 1:
    height = float(input("Input your height in feet and inches as a decimal: "))
    weight = float(input("Input your weight in lbs: "))
    age = int(input("Input your age as a whole number: "))
    print(gender())
    user_gender = int(input("Input your gender in accordance to the list: "))
    height_converted = height*30.48
    weight_converted = weight/2.205
    if user_gender == 1:
        BMR_raw = (10*weight_converted) + (6.25*height_converted) - (5*age) + 5
    elif user_gender == 2:
        BMR_raw = (10*weight_converted) + (6.25*height_converted) - (5*age) - 161
    else:
        print("Gender selection invalid, please enter your gender's corresponding numerical value in the list.")

else:
    height = float(input("Input your height in centimetres: "))
    weight = float(input("Input your weight in kg: "))
    age = int(input("Input your age as a whole number: "))
    print(gender())
    user_gender = int(input("Input your gender in accordance to the list: "))
    if user_gender == 1:
        BMR_raw = (10*weight) + (6.25*height) - (5*age) + 5
    elif user_gender == 2:
        BMR_raw = (10*weight) + (6.25*height) - (5*age) - 161
    else:
        print("Gender invalid, please enter your corresponding gender's numerical value in the list.")

print(activity_levels())

user_activity_level = int(input("Enter your corresponding activity level: "))

if user_activity_level == 1:
    daily_calories = BMR_raw*1.2
if user_activity_level == 2:
    daily_calories = BMR_raw*1.375
if user_activity_level == 3:
    daily_calories = BMR_raw*1.55
if user_activity_level == 4:
    daily_calories = BMR_raw*1.725
if user_activity_level == 5:
    daily_calories = BMR_raw*1.9
if user_activity_level < 1 or user_activity_level > 5:
    print("Please enter a valid activity level.")

print("")

print("In order to maintain your current weight, you must consume " + str(daily_calories) + " calories daily.")
print("")
calories_per_meal = daily_calories/3
print("Optimally, you should consume " + str((round(calories_per_meal, 2))) + " calories per 3 daily meals.")
print("")
print("Your BMR value " + str(round(BMR_raw, 2)))
print("")
calories_consumed_choice = int(input("If you know how many calories you have consumed today, enter 1. Otherwise,"
                                     " enter any other number: "))
print("")
if calories_consumed_choice == 1:
    calories_consumed = int(input("Input the quantity of calories you have consumed so far: "))
    print("")
    calories_remaining = daily_calories - calories_consumed
    print("You must consume " + str(
        (round(calories_remaining, 2))) + " more calories today to retain your current weight.")
    print("")
print("")
# ---------------------------------------- #

semen_calories = 0.7
semen_quantity = 3.4

semen_calories_calculated = int(daily_calories)/semen_calories
semen_required = semen_calories_calculated*semen_quantity

print("Additionally, in order to sustain your current weight by consuming semen, you would need to drink "
      + str(semen_required) + " ml of semen.")
