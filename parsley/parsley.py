#!/usr/bin/env python3

import pandas as pd
import click
from .seasoning import * # pylint: disable=unused-wildcard-import

@click.group()
def cli():
  pass
  # print("This method has these arguments: " + str(filename))


@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for parsing')
@click.argument('filename', type=click.Path(exists=True))
def columns(filename):
  '''Returns column headers of excel sheet'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename)
    print('Columns: ' + str(df.columns.values))
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename)
    print('Columns: ' + str(df.columns.values))


@cli.command()
@click.option('--filename', help='Absolute filepath of file intended for copying')
@click.argument('filename', type=click.Path(exists=True))
def copy(filename):
  '''Takes a file and copies it to Desktop'''
  if filename.endswith('.csv'):
    df = pd.read_csv(filename)
    df.to_csv('~/Desktop/revised_file.csv', index=False)
    print('File saved at ~/Desktop/revised_file.csv')
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename)
    df.to_excel('~/Desktop/revised_file.xlsx', index=False)
    print('File saved at ~/Desktop/revised_file.xlsx')


if __name__ == '__main__':
  cli()
