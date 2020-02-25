import json
from sklearn.model_selection import train_test_split

ALL_REGRESSORS = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3
}

ALL_CLASIFIRES = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3
}

class ModelManager:
    def __init__(self, model_name, task_type='regr', config=None):
        self.model = None
        if task_type == 'regr':
            self.model = ALL_REGRESSORS[model_name]
        elif task_type == 'class':
            self.model = ALL_CLASIFIRES[model_name]
        if config != None:
            self.model.set_params(config)

    def run(self, X, y, ratio):
        train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=ratio, \
            random_state=0)
        self.model.fit(train_X, train_y)
        predict = self._predict(test_X)
        metrics = self.calculate_matrics(predict, test_y)
        print(metrics)

    def _predict(self,X):
        return self.model.predict(X)

    @staticmethod
    def calculate_metrics(self, predict_y, true_y):
        raise NotImplementedError
    
    @staticmethod
    def save_metrics(metrics, file_name):
        with open('experiments/'+file_name+'json') as file:
            json.dump(metrics, file, ensure_ascii=False)

    
