#!/usr/bin/env python3

import pandas as pd
import click
from .seasoning import *  # pylint: disable=unused-wildcard-import


@click.group()
def cli():
  pass
  # print("This method has these arguments: " + str(filename))


@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for manipulation')
@click.argument('filename', type=click.Path(exists=True))
def get_columns(filename):
  '''Returns column headers of excel sheet'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename)
    print('Columns: ' + str(df.columns.values))
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename)
    print('Columns: ' + str(df.columns.values))
  else:
    print('File type is not acceptable, please use xlsx or csv')


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
  else:
    print('File type is not acceptable, please use xlsx or csv')


@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for manipulation')
@click.option('--column', help='Column that contains JSON array')
@click.option('--keys', help='Values to parse from JSON array')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('column')
@click.argument('keys', nargs=-1, required=True)
def parse(filename, column, keys):
  '''Parse values from a column that
  contains JSON structured data'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename)
    for key in keys:
      df[f'list_of_{key}'] = df[column].apply(lambda x: regex_parse(key, x))
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print('File saved at ~/Desktop/revised_file.csv')
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename)
    for key in keys:
      df[f'list_of_{key}'] = df[column].apply(lambda x: regex_parse(key, x))
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print('File saved at ~/Desktop/revised_file.csv')
  else:
    print('File type is not acceptable, please use xlsx or csv')


if __name__ == '__main__':
  cli()
