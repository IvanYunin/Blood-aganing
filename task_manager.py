import json
import numpy as np

class Task:
    def __init__(self, task_name, task_type, model_type, model_name,
     features="ALL", config=None):
        self.task_name = task_name
        self.task_type = task_type
        self.model_type = model_type
        self.model_name = model_name
        self.features = features
        self.config = config

    def __dict__(self):
        return {
        "task_name": self.task_name,
        "task_type": self.task_type,
        "model_type": self.model_type,
        "model_name": self.model_name,
        "features": self.features,
        "config": self.config
        }
class TaskManager:
    def __init__(self, config_file=None):
        self.queue = []
        #self.parse_config()

    def parse_config(self):
        raise NotImplementedError
    
    def add_task_enum(self, task_name, task_type, model_type, model_name,
     param, min, max, step):
        for idx, p in enumerate(np.arange(min, max, step)):
            self.queue.append(Task(task_name+str(idx),
            task_type,
            model_type,
            model_name,
            config = {param: p.item()}).__dict__()
            )
    
    def add_to_queue(self, task):
        self.queue.append(task)

    def dump_queue(self, file_name):
        with open(file_name+'.json', 'w') as file:
            json.dump(self.queue, file, ensure_ascii=False, indent=4)
        
    def get_queue(self,file_name):
        self.queue = json.loads(file_name)