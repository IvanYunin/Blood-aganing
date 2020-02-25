import sys
import argparse
import pandas as pd
from data_manager import DataManager
from model_manager import ModelManager
from sklearn.model_selection import train_test_split

def make_parser():
    parser = argparse.ArgumentParser(description='Blood aging')
    parser.add_argument('data_path', type=str, help='Path to data')
    parser.add_argument('--features', type=str, nargs="*", default='ALL',\
        help='Names of features for train model')
    parser.add_argument('task_type', type=str, help='Regression or classification (regr/class')
    parser.add_argument('model_name', type=str, help='Model name')
    parser.add_argument('--target', type=str, default='age', help='Name of column to prediction')
    # parser.add_argument('--test_data_path', type=str, default=None, help='Path to test data')
    parser.add_argument('--ratio', type=float, default=0.2, help='Raito test / train')
    return parser

def main():
    parser = make_parser()
    args = parser.parse_args()
    data_mngr = DataManager(args.data_path)
    data = pd.DataFrame()
    model_mngr = ModelManager(args.model_name, args.task_type)
    if args.features == 'ALL':
        data = data_mngr.load_data()
    else:
        data = data_mngr.take_some_features(args.features)
 
    X, y = DataManager.get_X_y(data, args.target)
    
    # train
    # test
    # save results



if __name__ == '__main__':
    sys.exit(main())