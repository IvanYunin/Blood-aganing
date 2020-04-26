import numpy as numpy
from data_manager import DataManager

def train(model, X, y):
    model.fit(X,y)
    return model

def calculate_regression_metrics(model, text_X, test_y):
    raise NotImplementedError

def calculate_classification_metrics(model, text_X, test_y):
    raise NotImplementedError

def save_configuration(model, data_info, results): # save model params and result on current data 
    raise NotImplementedError

