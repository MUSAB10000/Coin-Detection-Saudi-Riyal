# Coin Detection and Summing Project

This project uses the Roboflow API to detect coins in an image, count them, and calculate their total value. The coin values are determined based on a predefined mapping of coin classes to their corresponding monetary values.

## Features

- **Coin Detection:** Uses a pre-trained model on Roboflow.
- **Counting & Summing:** Counts the detected coins and calculates the total value.
- **Environment Variables:** API key is securely loaded from an environment variable.

## Prerequisites

- Python 3.6 or higher
- A [Roboflow](https://roboflow.com/) API key

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
2. **Install Dependencies:**
   
   ```bash
   pip install roboflow opencv-python supervision matplotlib numpy python-dotenv
3. **Set Up Environment Variables:**
     Create a `.env` file in the root of the project and add your Roboflow API key:

   ```bash
   ROBOFLOW_API_KEY=your_api_key_here
## Code Overview
- he main script (coins.py) performs the following tasks:

- Loads the Roboflow API key from an environment variable.

- Connects to the Roboflow project and model.

- Processes the inference results to count coins and sum their values.

- Prints the results to the console.
## License
Please note that all models hosted by Roboflow are covered by a commercial model license. If you are using these models in your project, you must comply with Roboflow's licensing and pricing terms. For more details, please refer to the [Roboflow Licensing and Pricing](https://roboflow.com/pricing) page.


