# Scratch Parse
Lists and counts the blocks of a given Scratch 3 Project JSON file, developed for the Creative Computing Lab at the Harvard Graduate School of Education. 

## Setup
1. Make sure you've installed Python 3.
2. Navigate the terminal to the downloaded repository.
3. Make sure you have all Scratch 3 Project JSON files in the same directory. This can be batch downloaded by the Scratch-Studio-Scrape tool found here: https://github.com/GSE-CCL/scratch-studio-scrape
4. All set!

## Usage
Inputs: blockify.py [options]
- -p: Project ID. Will list and count the blocks from the JSON of given project ID. 

...more inputs coming soon!

## Examples
List and count the blocks of a project with ID `ID_NUMBER`:

```python blockify.py -p ID_NUMBER```

This will return a list of unique blocks as well as a dictionary that counts the frequency of each block. 
