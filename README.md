# Анализ биохимических данных крови с помощью методов машинного обучения
## Введение

## Пример использования

<pre><code>python main.py -h
usage: main.py [-h] [--features [FEATURES [FEATURES ...]]] [--target TARGET]
               [--ratio RATIO]
               data_path task_type model_name

main.py data_path=full_nhanes.csv task_type=regr model_name=RF
Blood aging

positional arguments:
  data_path             Path to data
  task_type             Regression or classification (regr/class)
  model_name            Model name

optional arguments:
  -h, --help            show this help message and exit
  --features [FEATURES [FEATURES ...]]
                        Names of features for train model
  --target TARGET       Name of column to prediction
  --ratio RATIO         Raito test / train
</code></pre>
