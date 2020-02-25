import pandas as pd
import numpy as np

class DataManager:
    def __init__(self, path):
        self.data_path = pd.load_scv(path)

    def take_some_features(self, features):
        data = self.load_data()
        return data[features]

    def load_data(self):
        return pd.load_scv(self.data_path)

    @staticmethod
    def get_X_y(data, target):
        X = data.drop(target, axis = 1).values
        y = data[target].values
        return X, y

    # @staticmethod
    # def train_test_split(data):
    #     return None
    
    # def concat_table(self, new_table):
    #     self.data = pd.concat([self.data, new_table])

