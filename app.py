def pounds_to_kg(pounds):
    return pounds * 0.453592  # 1 pound is approximately equal to 0.453592 kilograms 

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def weight_bmi(bmi): # Parameters for distinguishing weight classes
    if bmi < 18.5:
        return 'Underweight'
    elif 18.4 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

def main():
    weight_unit = input("Enter 'lbs' if you want to enter weight in pounds, or 'kg' for kilograms: ").lower()
    while weight_unit not in ['lbs', 'kg']:
        weight_unit = input("Invalid input. Please enter 'lbs' or 'kg': ").lower()
# Implemented error handling incase the user enters a 
    weight = float(input("Enter your weight: "))
    if weight_unit == 'lbs':
        weight = pounds_to_kg(weight)
# BMI is calculated using the metric system therefore, conversions must be made.
    height_feet = float(input("Enter your height in feet: "))
    height_meters = height_feet * 0.3048  # 1 foot is equal .3048 meters.

    bmi = calculate_bmi(weight, height_meters)
    print('BMI:', bmi)
    
    category = weight_bmi(bmi)
    print('Category:', category)

if __name__ == '__main__':
    main()
