def main():
    while (True):
        try:
            current_sex = input('Please select your sex. Press f for female, m for male: ')

            if (current_sex == 'f' or current_sex == 'm'):
                break
            else:
                print('Error sex. Try it again.\n')
        except ValueError as err:
            print("please enter a valid value!\n")

    while (True):
        try:
            current_weight = float(input('Please enter your current weight in kilograms: '))
            break
        except ValueError as err:
            print("please enter a valid value!\n")

    while(True):
        try:
            current_age = int(input('Please input your age: '))
            if (current_age < 3):
                print("You are too young too simple, sometimes naive!")
            else:
                break

        except ValueError as err:
            print("please enter a valid value!\n")

    while(True):
        try:
            sport_frequency = int(input('Please indicate the fequency that you work out every week\n'
                                        '0. Seldom(0 times)\n'
                                        '1. Occasionally(1 to 3 times)\n'
                                        '2. Sometimes(3 to 5 times)\n'
                                        '3. Regularly(6 to 7 times)\n'
                                        '4. Professional(more than 7 times)\n'
                                        'Please select from 0 to 4: '))
            if sport_frequency == 0:
                BMR_index = 1.2
                break
            elif sport_frequency == 1:
                BMR_index = 1.375
                break
            elif sport_frequency == 2:
                BMR_index = 1.55
                break
            elif sport_frequency == 3:
                BMR_index = 1.725
                break
            elif sport_frequency == 4:
                BMR_index = 1.9
                break
            else:
                print('Please select the right number. Try it again.\n')

        except ValueError as err:
            print("please enter a valid value!\n")



    if current_sex == 'f':
        calorieData = females(current_age, current_weight, BMR_index)
        print('\nYou should consume at least', calorieData[0] + calorieData[1],
              'Calories per day!\n')
        return calorieData

    elif current_sex == 'm':
        calorieData = males(current_age, current_weight, BMR_index)
        print('\nYou should consume at least', calorieData[0] + calorieData[1], 'Calories per day!\n')
        return calorieData


# reference: WHO formula & Harris Benedict Formula


def females(age, weight, BMR_index):
    if age >= 3 and age <= 9:
        Calorie = 22.5 * weight + 499
    elif age >= 10 and age <= 17:
        Calorie = 12.2 * weight + 746
    elif age >= 18 and age <= 29:
        Calorie = 14.7 * weight + 496
    elif age >= 30 and age <= 60:
        Calorie = 8.7 * weight + 829
    elif age >= 60:
        Calorie = 10.5 * weight + 596

    BMR = Calorie * (BMR_index - 1)

    return (int(BMR), int(Calorie))


def males(age, weight, BMR_index):
    if age >= 3 and age <= 9:
        Calorie = 22.7 * weight + 495
    elif age >= 10 and age <= 17:
        Calorie = 17.5 * weight + 651
    elif age >= 18 and age <= 29:
        Calorie = 15.3 * weight + 679
    elif age >= 30 and age <= 60:
        Calorie = 11.6 * weight + 879
    elif age >= 60:
        Calorie = 13.5 * weight + 487
    else:
        print("You are too young too simple, sometimes naive!")
    BMR = Calorie * (BMR_index - 1)

    return (int(BMR), int(Calorie))
