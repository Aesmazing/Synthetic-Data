#Exam 2 part 1
#Aeslyn Broughton

import random
import csv
import os


def generate_random_name(used_names):
    first_names = [
        "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack",
        "John", "Kate", "Liam", "Olivia", "Mason", "Sophia", "Noah", "Ava", "Lucas", "Zoe",
        "Emma", "William", "James", "Oliver", "Ella", "Sophia", "Mia", "Charlotte", "Abigail",
        "Ethan", "Daniel", "Michael", "Benjamin", "Matthew", "Alexander", "Grace", "Lily", "Chloe",
        "Emily", "Evelyn", "Scarlett", "Lucy", "Sophie", "Ella", "Liam", "Noah", "Logan", "Jacob",
        "Elijah", "Carter", "Samuel", "Henry", "Sebastian", "David", "Michael", "Christopher",
        "Joseph", "Gabriel", "Daniel", "Anthony", "Isabella", "Sofia", "Aria", "Grace", "Lily",
        "Mia", "Zoe", "Camila", "Emily", "Madison", "Luna", "Ella", "Avery", "Scarlett", "Lucy",
        "Penelope", "Chloe", "Riley", "Evelyn", "Abigail", "Emma", "Charlotte", "Elijah", "Henry",
        "Leo", "James", "Benjamin", "Samuel", "David", "Matthew", "Joseph", "Daniel", "Nicholas",
        "Liam", "William", "Oliver", "Aiden", "Ethan", "Lucas", "Logan", "Alexander", "Gabriel",
        "Jackson", "Sebastian", "Ezekiel", "Daniel", "Eleanor", "Madeline", "Sophia", "Alice",
        "Ella", "Hannah", "Grace", "Lily", "Mia", "Avery", "Charlotte", "Penelope", "Riley",
    ]

    last_names = [
        "Smith", "Johnson", "Brown", "Davis", "Wilson", "Lee", "Wong", "Taylor", "Clark", "Martin",
        "Harris", "Miller", "Anderson", "Jones", "Moore", "Williams", "White", "Walker", "Thomas", "King",
        "Lewis", "Hill", "Young", "Scott", "Green", "Hall", "Adams", "Baker", "Evans", "Parker",
        "Garcia", "Martinez", "Rodriguez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Turner", "Robinson", "Perez",
        "Thomas", "White", "Anderson", "Jackson", "Harris", "Sanchez", "Ramirez", "Rivera", "Campbell", "Parker",
        "Bennett", "Wood", "Coleman", "Gray", "Mitchell", "Rogers", "Scott", "Stewart", "Bryant", "Russell",
        "Diaz", "Hayes", "Myers", "Ford", "Hamilton", "Graham", "Sullivan", "Wallace", "Powell", "Carter",
        "Reed", "Morgan", "Cooper", "Murphy", "Reed", "Ross", "Edwards", "Murray", "Spencer", "Watson",
        "Harrison", "Foster", "Morgan", "Simpson", "Dixon", "Neal", "Russell", "Willis", "Burns", "Howard",
        "Alexander", "Gardner", "Warren", "Carroll", "Hansen", "Black", "Weaver", "Sharp", "Wheeler", "Collins",
        "Price", "Morris", "Murphy", "Bennett", "Wood", "Coleman", "Gray", "Mitchell", "Rogers", "Scott", "Stewart",
        "Bryant", "Russell", "Diaz", "Hayes", "Myers", "Ford", "Hamilton", "Graham", "Sullivan", "Wallace", "Powell",
        "Carter", "Reed", "Morgan", "Cooper", "Murphy", "Reed", "Ross", "Edwards", "Murray", "Spencer", "Watson",
        "Harrison", "Foster", "Morgan", "Simpson", "Dixon", "Neal", "Russell", "Willis", "Burns", "Howard",
    ]

    while True:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = f"{last_name}, {first_name}"

        if full_name not in used_names:
            used_names.add(full_name)
            return full_name

def generate_customer_data(num_customers):
    
    customer_data = []
    for _ in range(num_customers):
        age = random.randint(18, 99)
        weight = round(random.uniform(90, 250), 2)
        height = round(random.uniform(55, 180), 2)
        sex = random.choice(['M', 'F'])
        home_state = random.choice(['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'])
        annual_purchases = round(random.uniform(-500, 5000), 2)

        customer_data.append({
            'Name': generate_random_name(set()),
            'Age': age,
            'Sex': sex,
            'Height': height,
            'Weight': weight,
            'Home State': home_state,
            'Annual Purchases': annual_purchases
        })

    return customer_data

def write_to_csv(customer_data, filename):
   try:
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            header = ["Name", "Age", "Sex", "Height", "Weight", "Home State", "Annual Purchases"]
            writer.writerow(header)
            for row in customer_data:
                writer.writerow(row.values())
   except PermissionError as e:
       print(f"Error writing to file: {e}")
      

def main():
    try:
        if os.path.exists("synthetic_data.csv"):
            os.remove("synthetic_data.csv")
            print ("Original File has been deleted")
        num_customers = random.randint(50,50000 )
        customer_data = generate_customer_data(num_customers)
        write_to_csv(customer_data, "synthetic_data.csv")
        print("File created: synthetic_data.csv")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
