import csv

# List of input CSV files
input_files = [
    './data/daily_sales_data_0.csv',
    './data/daily_sales_data_1.csv',
    './data/daily_sales_data_2.csv'
]

# Output CSV file
output_file = 'merged_filtered_sales.csv'

# Column headers to retain
output_columns = ['sales','date', 'region']

# Initialize a list to store merged data
merged_data = []

for file in input_files:
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            if row['product'].lower() == 'pink morsel': 
                row['sales'] = float(row['quantity']) * float(row['price'][1:])
                merged_data.append(row)

with open(output_file, mode='w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=output_columns)
    csv_writer.writeheader()
    
    for row in merged_data:
        csv_writer.writerow({
            'sales': '$'+str(row['sales']),
            'date': row['date'],
            'region': row['region']
        })

print(f"Merged and filtered data written to {output_file}")
