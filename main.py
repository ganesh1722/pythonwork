import csv


# Function to sort the CSV file
def sort_csv(input_file_path, output_file_path, field_to_sort_by):
    with open(input_file_path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file,quoting=csv.QUOTE_ALL)
        rows = sorted(reader, key=lambda row: row[field_to_sort_by])

    # Write sorted rows to a new CSV file
    with open(output_file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)


# Replace 'input.csv', 'output.csv', and 'field_to_sort_by' with your file paths and field name
input_file = 'C:\\Users\\tpugsund\\Downloads\\product_master_20240405.csv'
output_file = 'C:\\Users\\tpugsund\\Downloads\\product_master_20240405_sorted.csv'
sortfield = 'group_reference'

sort_csv(input_file, output_file, sortfield)
print("CSV file sorted successfully.")
