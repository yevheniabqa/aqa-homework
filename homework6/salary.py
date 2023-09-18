import csv

exchange_rate = 36.6

input_file = 'test_file.csv'

converted_data = []

with open(input_file, mode='r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:  # type: dict
        for key, value in row.items():
            if not key:
                continue

            row[key] = float(value) * exchange_rate
        converted_data.append(row)

output_file = 'salaries_uah.csv'

with open(output_file, mode='w', newline='') as file:
    fieldnames = converted_data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerows(converted_data)

print(f"Converted and saved salaries to {output_file}")
