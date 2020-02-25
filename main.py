import sys
import argparse
import pandas as pd
from data_manager import DataManager

ALL_REGRESSORS = {
    "RandomForest": 0,
    "1":1,
    "2":2,
    "3":3
}

ALL_CLASIFIRES = {
    "RandomForest": 0,
    "1":1,
    "2":2,
    "3":3
}


def make_parser():
    parser = argparse.ArgumentParser(description='Blood aging')
    parser.add_argument('data_path', type=str, help='Path to data')
    parser.add_argument('--features', type=str,nargs="*", default='ALL',\
        help='Names of features for train model')
    parser.add_argument('task_type', type=str, help='Regression or classification (regr/class')
    parser.add_argument('model_name', type=str, help='Model name')
    # parser.add_argument('--target', type=str, default='age', help='Target')
    parser.add_argument('--test_data_path', type=str, default=None, help='Path to test data')
    return parser

def main():
    parser = make_parser()
    args = parser.parse_args()
    data_mngr = DataManager(args.data_path)
    data = pd.DataFrame()
    model = None #!!1
    if args.features == 'ALL':
        data = data_mngr.load_data()
    else:
        data = data_mngr.take_some_features(args.features)

    if args.task_type == 'regr':
        model = ALL_REGRESSORS[args.model_name]
    elif args.task_type == 'class':
        model = ALL_CLASIFIRES[args.model_name]
    
    # split
    # train
    # test
    # save results


if __name__ == '__main__':
    sys.exit(main())