import csv

# Define the input and output file paths
input_file = 'pdata2.txt'
output_file = 'output.csv'

# Read the data from the input file and write it to the CSV file
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    # Define the delimiter (",") for the CSV writer
    csv_writer = csv.writer(outfile, delimiter=',')

    # Iterate through each line in the input file and split it by ","
    for line in infile:
        # Remove leading and trailing whitespace and split by ","
        data = line.strip().split(',')

        # Write the split data as a CSV row
        csv_writer.writerow(data)

print(f'Conversion complete. CSV file saved as "{output_file}".')
