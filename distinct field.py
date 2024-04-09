import csv
# Function to sort the CSV file
def distinct_csv(input_file_path, output_file_path, field_name):

    distinct_value=set()
    with open(input_file_path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file,quoting=csv.QUOTE_ALL)
        for row in reader:
            distinct_value.add(row[field_name])

    # Write sorted rows to a new CSV file
    with open(output_file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file,quoting=csv.QUOTE_ALL)
        writer.writerow([field_name])
        for value in distinct_value:
            writer.writerow([value])


# Replace 'input.csv', 'output.csv', and 'field_to_sort_by' with your file paths and field name
input_file = 'C:\\Users\\tpugsund\\Downloads\\product_master_20240405_sorted.csv'
output_file = 'C:\\Users\\tpugsund\\Downloads\\product_master_20240405_distinct.csv'
sortfield = 'group_reference'

distinct_csv(input_file, output_file, sortfield)
print("CSV file distincted successfully.")
