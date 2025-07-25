import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import joblib

# Load the trained model
model_path = 'air_quality_model.pkl'
if not os.path.exists(model_path):
    tk.Tk().withdraw()
    messagebox.showerror("Model Not Found", f"Could not find '{model_path}'. Please ensure the model file is in the correct path.")
    exit(1)
model = joblib.load(model_path)

# ----------------- MAIN WINDOW -------------------
root = tk.Tk()
root.title("Air Quality Health Risk Predictor")
root.geometry("600x550")
root.configure(bg="#f7f9fc")  # Soft background
root.resizable(False, False)

# ----------------- STYLES -------------------
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", font=("Segoe UI", 11), background="#f7f9fc")
style.configure("TEntry", font=("Segoe UI", 11), padding=6)
style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=6, background="#008CBA", foreground="white")
style.map("TButton",
          background=[("active", "#007bb5")],
          foreground=[("active", "white")])

# ----------------- TITLE BAR -------------------
title_bar = tk.Frame(root, bg="#0077b6", height=70)
title_bar.pack(fill='x')

title_label = tk.Label(title_bar, text="Air Quality Health Risk Predictor", font=("Segoe UI", 18, "bold"), bg="#0077b6", fg="white")
title_label.pack(pady=15)

# ----------------- INPUT FORM -------------------
form_frame = tk.Frame(root, bg="#f7f9fc", padx=30, pady=20)
form_frame.pack()

labels = ['PM2.5', 'PM10', 'NO2', 'NO', 'CO', 'O3']
entries = {}

for i, label in enumerate(labels):
    ttk.Label(form_frame, text=label + ":").grid(row=i, column=0, pady=10, sticky="w")
    entry = ttk.Entry(form_frame, width=30)
    entry.grid(row=i, column=1, pady=10)
    entries[label] = entry

# ----------------- RESULT LABEL -------------------
result_frame = tk.Frame(root, bg="#f7f9fc")
result_frame.pack(pady=20)

result_label = tk.Label(result_frame, text="", font=("Segoe UI", 14, "bold"), bg="#f7f9fc")
result_label.pack()

# ----------------- PREDICT FUNCTION -------------------
def predict_risk():
    try:
        values = [float(entries[label].get()) for label in labels]
        input_data = np.array([values])
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            result_label.config(text="Predicted Risk: HIGH ⚠️", fg="#d90429")
        else:
            result_label.config(text="Predicted Risk: LOW ✅", fg="#2a9d8f")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for all fields.")

# ----------------- BUTTON -------------------
btn = ttk.Button(root, text="Predict Health Risk", command=predict_risk)
btn.pack(pady=10)

# ----------------- FOOTER -------------------
footer = tk.Label(root, text="Designed for ML Presentation", font=("Segoe UI", 9), bg="#f7f9fc", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
