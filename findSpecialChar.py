import csv
import re

# regex pattern to find non word, non space character
regex_pattern=r'[^\w\s]'

# function to open the csv file, loop through row, loop through value in row
# add it to a set if it matches the regex and return the set
def print_specialchar(file):
    distinct_char = set()
    with open(file, 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for value in row:
                special_chars=re.findall(regex_pattern,value)
                distinct_char.update(special_chars)
    return distinct_char
#describe file path and call the function to get the set and print the output
file1 = 'C:\\Users\\tpugsund\\Downloads\\product_groups_20240410.csv'
file2 = 'C:\\Users\\tpugsund\\Downloads\\product_master_20240410.csv'
output=print_specialchar(file1)
output.update(print_specialchar(file2))
print('\n'.join(output))