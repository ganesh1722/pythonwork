import csv
# Function to sort the CSV file
def comparecsv(file, field_name):

    distinct_values=set()
    with open(file, 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file,quoting=csv.QUOTE_ALL)
        for row in reader:
            distinct_values.add(row[field_name])
    return distinct_values


# Replace 'input.csv', 'output.csv', and 'field_to_sort_by' with your file paths and field name
file1 = 'C:\\Users\\tpugsund\\Downloads\\product_groups_20240409.csv'
file2 = 'C:\\Users\\tpugsund\\Downloads\\product_master_20240405_sorted.csv'
sortfield = 'group_reference'

group_set=comparecsv(file1, sortfield)
prod_set=comparecsv(file2, sortfield)
missing_values=prod_set-group_set
print("Values in prod file which is not in group file", missing_values)
print(len(group_set))
print(len(prod_set))
missing_values1=group_set-prod_set
print("Values in group file which is not in prod file", missing_values1)
