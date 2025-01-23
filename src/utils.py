import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    """Save an object to a file using pickle.

    This function creates the directory if it doesn't exist, and then saves the given object to the specified file path.
    """
    try:
        # Get the directory path from the file path
        dir_path = os.path.dirname(file_path)

        # Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        # Open the file in write-binary mode and save the object using pickle
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        # Raise a custom exception if an error occurs
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """Evaluate multiple models using GridSearchCV and return a report.

    This function takes training and testing data, a dictionary of models, and a dictionary of parameters.
    It performs hyperparameter tuning using GridSearchCV and evaluates the models on the test data.
    """
    try:
        report = {}

        # Iterate over the models
        for i in range(len(list(models))):
            model = list(models.values())[i]
            params = param[list(models.keys())[i]]

            # Perform GridSearchCV for hyperparameter tuning
            gs = GridSearchCV(model, params, cv=3)
            gs.fit(X_train, y_train)

            # Get the best model and evaluate it on the test data
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            # Calculate the R2 score and store it in the report
            report[list(models.keys())[i]] = r2_score(y_test, y_pred)

        return report

    except Exception as e:
        # Raise a custom exception if an error occurs
        raise CustomException(e, sys)

def load_object(file_path):
    """Load an object from a file using pickle."""
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        # Raise a custom exception if an error occurs
        raise CustomException(e, sys)