# Air Quality Health Risk Predictor

This project predicts health risk levels based on air quality parameters using a machine learning model and provides a user-friendly GUI for predictions.

## Project Structure

```
Project_1/
├── air_quality_model.pkl      # Trained machine learning model (Logistic Regression)
├── gui2.py                   # Python GUI application for predictions
├── sppu_pune.csv             # Raw air quality data (Savitribai Phule Pune University)
├── vimannagar.csv            # Raw air quality data (Vimannagar)
└── tut1.ipynb                # Jupyter notebook for data analysis, model training, and export
```

## Features

- Predicts health risk (Low/High) based on air quality indicators: PM2.5, PM10, NO2, NO, CO, O3.
- Simple and intuitive GUI built with Tkinter.
- Model trained using logistic regression on real air quality datasets.

## How to Run

1. **Install dependencies**  
   Make sure you have Python 3 and the following packages:
   - numpy
   - scikit-learn
   - joblib
   - pandas
   - tkinter (usually included with Python)

   Install missing packages with:
   ```sh
   pip install numpy scikit-learn joblib pandas
   ```

2. **Ensure files are present**  
   - `air_quality_model.pkl` must be in the project directory.
   - `gui2.py` is the main application file.

3. **Run the GUI**
   ```sh
   python gui2.py
   ```

4. **Using the Application**
   - Enter values for PM2.5, PM10, NO2, NO, CO, and O3.
   - Click "Predict Health Risk" to see the predicted risk level.

## Model Training

- Data preprocessing, feature engineering, and model training are documented in [`tut1.ipynb`](tut1.ipynb).
- The model is trained on combined data from `sppu_pune.csv` and `vimannagar.csv`.
- The trained model is saved as `air_quality_model.pkl`.

## File Descriptions

- [`gui2.py`](gui2.py): Main GUI application for predictions.
- [`tut1.ipynb`](tut1.ipynb): Data analysis and model training notebook.
- `air_quality_model.pkl`: Serialized trained model.
- `sppu_pune.csv`, `vimannagar.csv`: Raw air quality datasets.

## Credits

- Data sources: Maharashtra Pollution Control Board, Indian Institute of Tropical Meteorology.
- Developed for ML
