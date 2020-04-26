import sys
import argparse
import pandas as pd
from data_manager import DataManager
from model_manager import ModelManager
from task_manager import TaskManager

def make_parser():
    parser = argparse.ArgumentParser(description='Tasks')
    parser.add_argument('make_queue', type=bool, help='Path to data')
    parser.add_argument('param', type=str, help='Param')
    return parser

def main():
    parser = make_parser()
    args = parser.parse_args()
    task_mngr = TaskManager()
    task_mngr.add_task_enum("test","test_type","regr","RF", args.param, 10, 100, 10)
    task_mngr.dump_queue("q")
if __name__ == '__main__':
    sys.exit(main())