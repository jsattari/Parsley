#!/usr/bin/env python3

import pandas as pd
import click
import json
import csv
from .seasoning import *  # pylint: disable=unused-wildcard-import


@click.group()
def cli():
  pass

# command for viewing cols (returns list)
@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for manipulation')
@click.argument('filename', type=click.Path(exists=True))
def getcolumns(filename):
  '''Returns headers of xlsx or csv'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename)
    print('Columns: ' + str(df.columns.values))
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename)
    print('Columns: ' + str(df.columns.values))


# command that creates copy of file from specified path
@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for manipulation')
@click.argument('filename', type=click.Path(exists=True))
def copy(filename):
  '''Takes a file and copies it to Desktop as a csv'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename)
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print('File saved at ~/Desktop/revised_file.csv')
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename)
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print('File saved at ~/Desktop/revised_file.csv')


# command for parsing column that contains JSON array
# Must specify values to parse out
@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for manipulation')
@click.option('--column', help='Column that contains JSON array')
@click.option('--keys', help='Values to parse from JSON array')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('column', required=True)
@click.argument('keys', nargs=-1, required=True)
def parse(filename, column, keys):
  '''Parse values from a column that
  contains JSON structured data.'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename)
    for key in keys:
      df[f'list_of_{key}'] = df[column].apply(lambda x: regex_parse(key, x))
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print(df.head())
    print('File saved at ~/Desktop/revised_file.csv')
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename)
    for key in keys:
      df[f'list_of_{key}'] = df[column].apply(lambda x: regex_parse(key, x))
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print('File saved at ~/Desktop/revised_file.csv')


# Sum values from within a column
@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for manipulation')
@click.option('--column', help='Column to be summed')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('column')
def add(filename, column):
  '''Add up contents of each row within
  the selected column'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename)
    df[f'add_{column}'] = df[column].apply(lambda x: addup(x))
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print('file saved at ~/Desktop/revised_file.csv')
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename)
    df[f'add_{column}'] = df[column].apply(lambda x: addup(x))
    df.to_excel('~/Desktop/revised_file.xlsx', index=False)
    print('file saved at ~/Desktop/revised_file.xlsx')


# Find avg of values within a column
@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for manipulation')
@click.option('--column', help='Column to be averaged')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('column')
def avg(filename, column):
  '''Find the mean of the values in each row
  within a given column'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename)
    df[f'avg_{column}'] = df[column].apply(lambda x: avgup(x))
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print('file saved at ~/Desktop/revised_file.csv')
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename)
    df[f'avg_{column}'] = df[column].apply(lambda x: avgup(x))
    df.to_excel('~/Desktop/revised_file.xlsx', index=False)
    print('file saved at ~/Desktop/revised_file.xlsx')


# drop column from dataset
@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for manipulation')
@click.option('--columns', help='Column(s) to drop')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('columns', nargs=-1, required=True)
def drop(filename, columns):
  '''Drop listed column(s) from dataset'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename)
    for i in columns:
      df = df.drop(f'{i}', axis=1)
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print('file saved at ~/Desktop/revised_file.csv')
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename)
    for i in columns:
      df = df.drop(f'{i}', axis=1)
    df.to_excel('~/Desktop/revised_file.xlsx', index=False)
    print('file saved at ~/Desktop/revised_file.xlsx')


@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for manipulation')
@click.argument('filename', type=click.Path(exists=True))
def preview(filename):
  '''Show a snapshot of data'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename, error_bad_lines=False).replace("'", '', regex=True)
    print(df.head())
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename).replace("'", '', regex=True)
    print(df.head())

@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for manipulation')
@click.option('--columns', help='Column(s) to compute max value')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('columns', nargs=-1, required=True)
def getmax(filename, columns):
  '''Get the max of the values in each row'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename, error_bad_lines=False).replace("'", '', regex=True)
    for col in columns:
      df[f'max_{col}'] = df[f'{col}'].apply(lambda x: max_val(x))
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print('file saved at ~/Desktop/revised_file.csv')
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename).replace("'", '', regex=True)
    for col in columns:
      df[f'max_{col}'] = df[f'{col}'].apply(lambda x: max_val(x))
    df.to_excel('~/Desktop/revised_file.xlsx', index=False)
    print('file saved at ~/Desktop/revised_file.xlsx')

@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for manipulation')
@click.option('--columns', help='Column(s) to compute min values')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('columns', nargs=-1, required=True)
def getmin(filename, columns):
  '''Get the min of the values in each row'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename, error_bad_lines=False).replace("'", '', regex=True)
    for col in columns:
      df[f'min_{col}'] = df[f'{col}'].apply(lambda x: min_val(x))
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print('file saved at ~/Desktop/revised_file.csv')
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename).replace("'", '', regex=True)
    for col in columns:
      df[f'min_{col}'] = df[f'{col}'].apply(lambda x: min_val(x))
    df.to_excel('~/Desktop/revised_file.xlsx', index=False)
    print('file saved at ~/Desktop/revised_file.xlsx')

@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for manipulation')
@click.option('--columns', help='Column(s) to compute median values')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('columns', nargs=-1, required=True)
def med(filename, columns):
  '''Get the median of the values in each row'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename, error_bad_lines=False).replace("'", '', regex=True)
    for col in columns:
      df[f'median_{col}'] = df[f'{col}'].apply(lambda x: med_val(x))
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print('file saved at ~/Desktop/revised_file.csv')
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename).replace("'", '', regex=True)
    for col in columns:
      df[f'median_{col}'] = df[f'{col}'].apply(lambda x: med_val(x))
    df.to_excel('~/Desktop/revised_file.xlsx', index=False)
    print('file saved at ~/Desktop/revised_file.xlsx')


if __name__ == '__main__':
  cli()
