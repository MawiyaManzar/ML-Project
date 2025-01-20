# ML Project: Machine Learning Workflow Automation
This repository contains a comprehensive machine learning pipeline, covering data ingestion, transformation, and model training. It is designed to be modular, reusable, and easy to understand.

Features
Environment Setup: Automate creating a Python virtual environment with all dependencies.
Data Pipeline: Includes:
Data ingestion (loading and splitting datasets).
Data transformation (handling missing values, scaling, encoding).
Model training with multiple algorithms.
Custom Exception Handling: Provides detailed error information for debugging.
Pre-built Scripts: Modularized for scalability and reusability.
Logging: Keeps track of all pipeline operations for transparency.
Installation and Setup
Prerequisites
Python 3.8+
Conda (optional for virtual environment management)
Git
Steps
Clone the repository:
bash
Copy
Edit
git clone https://github.com/MawiyaManzar/MLproject.git
Navigate to the project directory:
bash
Copy
Edit
cd MLproject
Create and activate a virtual environment:
bash
Copy
Edit
conda create -p venv python==3.8 -y
conda activate venv/
Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Project Structure
plaintext
Copy
Edit
MLproject/
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   ├── predict_pipeline.py
│   ├── utils/
│   ├── logger.py
│   ├── exception.py
├── artifacts/  # Directory for saving intermediate files (created during runtime)
├── requirements.txt
├── setup.py
├── README.md
Key Components
Data Ingestion:

Reads raw data (e.g., stud.csv).
Splits it into training and testing datasets.
Saves processed data in the artifacts/ directory.
Data Transformation:

Handles missing values.
Scales numerical features and encodes categorical features.
Saves the preprocessing pipeline as preprocessor.pkl.
Model Training:

Trains and evaluates multiple machine learning models.
Selects the best model based on performance.
Saves the trained model as model.pkl.
Error Handling:

Custom exceptions with detailed error messages, including file names and line numbers.
How to Run
Train the Pipeline
bash
Copy
Edit
python src/pipeline/train_pipeline.py
Predict
After training, use the trained model for predictions:

bash
Copy
Edit
python src/pipeline/predict_pipeline.py
Contributing
Feel free to fork this repository, make changes, and submit a pull request. Suggestions and feedback are welcome!
