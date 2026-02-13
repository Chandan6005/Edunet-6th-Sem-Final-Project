def calculate_bmi(weight, height):
    return round(weight / (height * height), 2)

def bmi_category(bmi):
    if bmi <18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi <30:
        return "Overweight"
    else:
        return "Obese"