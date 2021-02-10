# Parsley
Command line CLI to help you parse JSON within excel or csv files

## Install

```
$ git clone https://github.com/jsattari/Parsley.git
```
## Usage

```
$ parsley parse <filepath> jsoncol key key key
```

## Commands

```
Usage: parsley [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add         Add up contents of each row within the selected column
  avg         Find mean of the values in each row within a given column
  copy        Takes a file and copies it to Desktop as a csv
  drop        Drop listed column(s) from dataset
  getcolumns  Returns column headers of excel sheet
  getmax      Get the max of the values in each row
  getmin      Get the min of the values in each row
  med         Get the median of the values in each row
  parse       Parse values from a column that contains JSON structured data.
  preview     Show a snapshot of data
```
