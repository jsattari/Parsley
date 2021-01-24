import re
import json
import pandas as pd
import fire
import os


class parsley:
  def __init__(self, path):
    self.path = pd.read_csv(path)

  def columns(self):
    df = self.path
    col_list = list(df.columns)
    for i in range(0, len(col_list)):
        print(col_list[i])
    #print('Columns: ' + (col_list))


if __name__ == '__main__':
  fire.Fire(parsley)
