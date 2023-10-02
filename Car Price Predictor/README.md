# Car Price Predictor Project

## Overview

The Car Price Predictor project aims to create a machine learning-based solution to estimate the price of a car based on various features and specifications. This project leverages Python for data processing and machine learning, along with HTML and CSS to build a user-friendly web interface for inputting car details and receiving price estimates.

## Requirements

### Python Libraries
- **NumPy:** A library for numerical computing in Python.
- **Pandas:** A data manipulation and analysis library.
- **Matplotlib:** A data visualization library for creating static, animated, and interactive visualizations in Python.
- **Seaborn:** A data visualization library based on Matplotlib, designed to make statistical graphics more attractive and informative.
- **Scikit-Learn:** A machine learning library for Python.

### Web Framework
- **Flask:** A lightweight and versatile web framework for Python. Flask is used to create the web application that hosts the car price prediction feature.

### Web Design
- **HTML and CSS:** For creating a user-friendly web interface.

## Project Structure

```plaintext
Car Price Predictor/
├── data/
│   ├── car__price_prediction.csv    # Dataset containing car features and prices
│   ├── Clean_car_data.csv           # Cleaned Dataset for app
├── model/
│   ├── car_price_prediction.pkl     # Trained machine learning model
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css            # CSS file for styling the web page
│   ├── template/
│   │   ├── index.html               # HTML template for the web page
│   ├── web_app.py                   # Python script for the web application (Flask)
├── notebook/
│   ├── car_price_prediction.ipynb   # Jupyter Notebook for data exploration & model training
├── Web Page/
│   ├── image.png                    # Image of the web page interface
│   ├── WebPage-video.mp4            # Video showing how the web page works
├── README.md                        # Project README file
```

## Usage
### Data Preparation and Model Training:
1. Explore and preprocess the car dataset using the ‘car_price_prediction.ipynb’ Jupyter Notebook located in the ‘notebook/’ directory.

2. Train the machine learning model to predict car prices using the same ‘car_price_prediction.ipynb‘ notebook.

### Web Application (Powered by Flask):
1. Launch the web application for car price prediction by running the web_app.py script in the app/ directory.
### Input Features:
* Users can input various features and specifications of a car, such as make, model, year, mileage, and more.
### Price Prediction:
* After entering the car details, the Flask-based web application will use the trained model to estimate the car's price and display it to the user.
## Credits
* Image: The beautiful car image used in this project is courtesy of Tabea Schimpf.
* Image Link: Unsplash - Tabea Schimpf's Portfolio 
## Acknowledgments
Special thanks to the open-source community for the Python libraries used in this project, and to Flask for powering the web application.
