import json
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from xgboost import XGBRegressor, XGBClassifier
from sklearn import svm

ALL_REGRESSORS = {
    "RF": RandomForestRegressor(),
    "XGBoost": XGBRegressor(),
    "SVM": svm.SVR(),
    "LogReg": 3,
    "Dis_tree": 4
}

ALL_CLASIFIRES = {
    "RF": RandomForestClassifier(),
    "XGBoost": XGBClassifier(),
    "SVM": svm.SVC(),
    "LogReg": 3,
    "Dis_tree": 4
}

class ModelManager:
    def __init__(self, model_name, task_type='regr', config=None):
        self.model = None
        self.task_type = task_type
        if task_type == 'regr':
            self.model = ALL_REGRESSORS[model_name]
        elif task_type == 'class':
            self.model = ALL_CLASIFIRES[model_name]
        if config != None:
            self.model.set_params(config)

    def run(self, X, y, ratio):
        print("Training...")
        train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=ratio, \
            random_state=0)
        self.model.fit(train_X, train_y)
        print("Predict...")
        predict = self._predict(test_X)
        metrics = self.calculate_metrics(predict, test_y)
        print(metrics)

    def _predict(self,X):
        return self.model.predict(X)

    def calculate_metrics(self, predict_y, true_y):
        if self.task_type == 'regr':
            return self.regression_metrics(predict_y, true_y)
        else:
            return self.classification_metrics(predict_y, true_y)

    def regression_metrics(self, y_pred, y_true):
        r2 = r2_score(y_true, y_pred)
        mae = np.abs(y_pred - y_true).mean()
        return {
            'R^2': r2,
            'mae': mae
            }

    def classification_metrics(self, predict_y, true_y):
        return {'classification':'1'}

    @staticmethod
    def save_metrics(metrics, file_name):
        with open('experiments/'+file_name+'json') as file:
            json.dump(metrics, file, ensure_ascii=False)

    def run_task(self, task):
        raise NotImplementedError
