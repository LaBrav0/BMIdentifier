from flask import Flask, render_template, request

app = Flask(__name__)

def pounds_to_kg(pounds):
    return pounds * 0.453592  # 1 pound is approximately equal to 0.453592 kilograms 

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def weight_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight_unit = request.form['weight_unit']
        weight = float(request.form['weight'])
        if weight_unit == 'lbs':
            weight = pounds_to_kg(weight)
        
        height_feet = float(request.form['height'])
        height_meters = height_feet * 0.3048  # Convert height to meters

        bmi = calculate_bmi(weight, height_meters)
        category = weight_bmi(bmi)

        return render_template('result.html', bmi=bmi, category=category)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
