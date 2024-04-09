from flask import Flask, render_template, request

app = Flask(__name__)

def pounds_to_kg(pounds):
    return pounds * 0.453592  #1 pound is approximately equal to 0.453592 kilograms 

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2) #Algorithm to perform BMI calculation based on parameters entered.
    return bmi

def weight_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight' #Parameters which determine BMI category.
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

@app.route('/', methods=['GET', 'POST']) #Flask framework routes are defined when the user needs a path 
def index(): #GET requests are important for retrieving data from the server
    if request.method == 'POST': #POST requests are used to submit data to the server
        weight_unit = request.form['weight_unit'] 
        weight = float(request.form['weight'])
        if weight_unit == 'lbs':
            weight = pounds_to_kg(weight)
        
        height_feet = float(request.form['height'])
        height_meters = height_feet * 0.3048  # Convert height to meters

        bmi = calculate_bmi(weight, height_meters)
        category = weight_bmi(bmi) 

        return render_template('result.html', bmi=bmi, category=category)
    return render_template('ui.html')

if __name__ == '__main__':
    app.run(debug=True)
