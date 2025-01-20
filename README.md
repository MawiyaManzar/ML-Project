# ML Project: Student Performance Prediction

## Overview

This project is a machine learning application designed to predict student performance based on various features such as gender, ethnicity, parental education level, lunch type, and test preparation course. The goal is to build a model that can accurately predict a student's math score using regression techniques.

---

## Features

- **Data Ingestion**: Automatically reads and splits the dataset into training and testing sets.
- **Data Transformation**: Handles missing values, scales numerical features, and encodes categorical features.
- **Model Training**: Trains multiple regression models and selects the best-performing one.
- **Prediction Pipeline**: Allows for easy prediction on new data using the trained model.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MawiyaManzar/MLproject.git
   cd MLproject
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the Package**:
   ```bash
   pip install -e .
   ```

---

## Usage

### Data Ingestion

To ingest and split the dataset:
```bash
python src/components/data_ingestion.py
```

### Data Transformation

To preprocess the data:
```bash
python src/components/data_transformation.py
```

### Model Training

To train the model and evaluate its performance:
```bash
python src/components/model_trainer.py
```

### Prediction

To make predictions using the trained model:
```bash
python src/pipeline/predict_pipeline.py
```

---

## Project Structure

```
MLproject/
├── artifacts/                  # Stores processed data and models
│   ├── data.csv                # Raw dataset
│   ├── train.csv               # Training dataset
│   ├── test.csv                # Testing dataset
│   ├── preprocessor.pkl        # Preprocessing pipeline
│   └── model.pkl               # Trained model
├── notebooks/                  # Jupyter notebooks for exploration
│   └── data/                   # Dataset folder
│       └── stud.csv            # Original dataset
├── src/                        # Source code
│   ├── components/             # Data ingestion, transformation, and model training
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/               # Prediction pipeline
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── exception.py            # Custom exception handling
│   ├── logger.py               # Logging configuration
│   └── utils.py                # Utility functions
├── requirements.txt            # List of dependencies
└── setup.py                    # Package configuration
```

---

## Dependencies

- **Python Libraries**:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `catboost`
  - `xgboost`
  - `Flask` (for deployment)

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or feedback, feel free to reach out:

- **Name**: Mawiya Manzar
- **Email**: mawiyamanzar@gmail.com
- **GitHub**: [MawiyaManzar](https://github.com/MawiyaManzar)

---

## Acknowledgments

- Thanks to the open-source community for providing the tools and libraries used in this project.
- Special thanks to the dataset providers for making the data publicly available.

---

This README provides a comprehensive guide to understanding, installing, and using the ML project. It is designed to be beginner-friendly while still providing all the necessary details for advanced users.
