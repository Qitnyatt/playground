# https://www.codewars.com/kata/calculate-bmi/train/python


def bmi(weight, height):
    bmi_calculated = weight / (height ** 2)

    if bmi_calculated <= 18.5:
        return 'Underweight'

    if bmi_calculated <= 25.0:
        return 'Normal'

    if bmi_calculated <= 30.0:
        return 'Overweight'

    if bmi_calculated > 30:
        return 'Obese'
