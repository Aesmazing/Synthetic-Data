#Aeslyn Broghton
#NOV 29,2023
#EXAM 2 PT 2 

import csv
import random

def analyze_csv(file_path, target_column, threshold):
    try:
        distribution_data = {}
        count_over_threshold = 0
        count_under_threshold = 0

        with open(file_path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for column, value in row.items():
                    if column != "Name":
                        if column not in distribution_data:
                            distribution_data[column] = {}
                        if value not in distribution_data[column]:
                            distribution_data[column][value] = 0
                        distribution_data[column][value] += 1

                    if column == target_column:
                        if float(value) > threshold:
                            count_over_threshold += 1
                        else:
                            count_under_threshold += 1

        return distribution_data, count_over_threshold, count_under_threshold
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the file path.")
        return None, 0, 0
    except Exception as e:
        print(f"An unexpected error occurred while analyzing the CSV file: {e}")
        return None, 0, 0

def generate_random_customer(distribution_data):
    random_customer = {}

    for field, counts in distribution_data.items():
        random_value = random.choice(list(counts.keys()))
        random_customer[field] = random_value

    return random_customer

def number_records_from_user():
    while True:
        try:
            num_records = int(input("Please enter the number of records you'd like to generate (Numbers only): "))
            return num_records
        except ValueError:
            print("Please enter a numeric value.")

def generate_random_dataset(distribution_data, num_records):
    random_dataset = []

    for _ in range(num_records):
        random_customer = generate_random_customer(distribution_data)
        random_dataset.append(random_customer)

    return random_dataset

def write_to_csv(random_data, output_filename):
    try:
        with open(output_filename, "w", newline='') as file:
            writer = csv.writer(file)
            header = ["Age", "Sex", "Height", "Weight", "Home State", "Annual Purchases"]
            writer.writerow(header)
            for row in random_data:
                writer.writerow(row.values())
        print(f"File created: {output_filename}")
    except PermissionError:
        print(f"Error: Permission denied. Unable to write to {output_filename}.")
    except Exception as e:
        print(f"An unexpected error occurred while writing to the CSV file: {e}")

def main():
    file_path = "synthetic_data.csv"
    target_column = "Annual Purchases"
    threshold = 1000.0
    num_records = number_records_from_user()
    
    analysis_result, count_over, count_under = analyze_csv(file_path, target_column, threshold)

    if analysis_result is not None:
        random_dataset = generate_random_dataset(analysis_result, num_records)

        # Test
##        for customer in random_dataset:
##            print(customer)

        output_filename = "synthetic_data_set_2.csv"
        write_to_csv(random_dataset, output_filename)

if __name__ == "__main__":
    main()
