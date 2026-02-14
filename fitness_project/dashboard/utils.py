def calculate_bmi(weight, height):
    # height is in centimeters, convert to meters for BMI calculation
    height_in_meters = height / 100
    return round(weight / (height_in_meters * height_in_meters), 2)

def bmi_category(bmi):
    if bmi <18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi <30:
        return "Overweight"
    else:
        return "Obese"