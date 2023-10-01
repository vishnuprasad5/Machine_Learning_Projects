
from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

app = Flask(__name__)

current_directory = os.path.dirname(os.path.realpath(__file__))

csv_file_path = os.path.join(current_directory, '..', 'data', 'Clean_car_data.csv')
model_file_path = os.path.join(current_directory, '..', 'model', 'car_price_prediction.pkl')

car = pd.read_csv(csv_file_path)

with open(model_file_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')

def index():
    manufacturer = sorted(car['Manufacturer'].unique())
    car_models = [
        {'manufacturer': row['Manufacturer'], 'name': row['Model']} for index, row in car.iterrows()
    ]
    year = sorted(car['Prod. year'].unique(), reverse=True)
    category = sorted(car['Category'].unique())
    leather = sorted(car['Leather interior'].unique())
    fuel = sorted(car['Fuel type'].unique())
    gear_box = sorted(car['Gear box type'].unique())
    return render_template(
        'index.html',
        manufacturer=manufacturer,
        car_models=car_models,
        year=year,
        category=category,
        leather=leather,
        fuel=fuel,
        gear_box=gear_box
    )

@app.route('/predict', methods=['POST'])
def predict():
    manufacturer = request.form.get('manufacturer')
    car_model = request.form.get('model')
    year = request.form.get('year')
    category = request.form.get('category')
    leather = request.form.get('leather')
    fuel = request.form.get('fuel')
    gear_box = request.form.get('gear_box')
    engine_vol = request.form.get('engine_vol')
    kms_driven = request.form.get('km')
    cylinder = request.form.get('cylinder')
    air_bag = request.form.get('air_bag')

    data = {
            'Levy' : [779.0],
            'Manufacturer': [manufacturer],
            'Model': [car_model],
            'Prod. year': [year],
            'Category': [category],
            'Leather interior': [leather],
            'Fuel type': [fuel],
            'Gear box type': [gear_box],
            'Engine volume': [engine_vol],
            'Mileage': [kms_driven],
            'Cylinders': [cylinder],
            'Airbags': [air_bag]
        }

    input_data = pd.DataFrame(data)

    prediction = model.predict(input_data)

    return str(prediction[0])

if __name__ == '__main__':
    app.run(debug=True)

