import os
from roboflow import Roboflow
import cv2
import supervision as sv
import matplotlib.pyplot as plt
import numpy as np

# Get the API key from the environment variable
api_key = os.getenv("ROBOFLOW_API_KEY")
if not api_key:
    raise ValueError("Please set the ROBOFLOW_API_KEY environment variable")

# Initialize the Roboflow client with the API key
rf = Roboflow(api_key=api_key)

# Access your project (replace "coin-qcv02-w8hku" with your project slug) and select version 4
project = rf.workspace().project("coin-qcv02-w8hku")
model = project.version(4).model

# Infer on image and get predictions
image_path = "m5.jpg"
result = model.predict(image_path).json()

# Define the coin values mapping
class_mapping = {
    '1 halala': 0.01,
    '2 halala': 0.02,
    '5 halala': 0.05,
    '10 halala': 0.10,
    '25 halala': 0.25,
    '50 halala': 0.50,
    '100 halala': 1.00,
    'one riyal': 1.00,
    'two riyal': 2.00
}

# Initialize counters
total_sum = 0
coin_count = 0

# Prepare detection data and compute totals
for pred in result["predictions"]:
    coin_count += 1
    total_sum += class_mapping.get(pred['class'], 0)

# Print the results
print(f"Total coins detected: {coin_count}")
print(f"The total sum is: {total_sum:.2f} Riyal(s)")
