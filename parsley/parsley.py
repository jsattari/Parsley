import re
import json
import pandas as pd
import click
import os



@click.group()
def cli():
  pass
  # print("This method has these arguments: " + str(filename))


@cli.command()
@click.option('--filename', default=str, help='Absolute filepath of file intended for parsing')
@click.argument('filename', type=click.Path(exists=True))
def columns(filename):
  if filename.endswith('.csv'):
    df = pd.read_csv(filename)
    print('Columns: ' + str(df.columns.values))
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename)
    print('Columns: ' + str(df.columns.values))

@cli.command()
@click.option('--filename', default=str, help='Save a copy of file for editing')
@click.argument('filename', type=click.Path(exists=True))
def copy(filename):
  if filename.endswith('.csv'):
    df = pd.read_csv(filename)
    df.to_csv('~/Desktop/revised_' + filename, index=False)
    print('File saved at revised_' + filename)
  if filename.endswith('.xlsx'):
    df = pd.read_excel(filename)
    df.to_excel('~/Desktop/revised_' + filename, index=False)
    print('File saved at revised_' + filename)


if __name__ == '__main__':
  cli()
