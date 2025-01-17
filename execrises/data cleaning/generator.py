import pandas as pd
import random
import numpy as np

# Define a function to generate random emails, names, and departments
def generate_email(name):
    domains = ["email.com", "mail.net", "web.org", "fake.com"]
    return f"{name.lower().replace(' ', '_')}@{random.choice(domains)}"

def generate_name():
    first_names = ["John", "Jane", "Mike", "Sarah", "Chris", "Emily", "Alex", "Anna", "Sam", "Tom", "Jessica", "Laura", "Lisa", "Peter", "Robert", "Alice", "James", "Mary", "David"]
    last_names = ["Doe", "Smith", "Johnson", "O'Connell", "Brown", "Green", "Black", "White", "Miller", "Davis"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_department():
    return random.choice(["Sales", "Marketing", "IT", "HR", "Finance", "Operations", "Customer Support", "NULL"])

def generate_date():
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%B %d, %Y", "N/A"]
    try:
        return pd.Timestamp(random.randint(2015, 2025), random.randint(1, 12), random.randint(1, 28)).strftime(random.choice(formats))
    except:
        return "NULL"

# Generate random data for 1000 rows
data = []
for i in range(1000):
    name = generate_name() if random.random() > 0.05 else "NULL"  # 5% chance for NULL name
    email = generate_email(name) if "NULL" not in name and random.random() > 0.1 else "invalid_email"  # 10% invalid emails
    age = random.choice([random.randint(20, 60), "twenty", "NULL", "NA"])  # Some invalid age entries
    join_date = generate_date()
    salary = random.choice([random.randint(30000, 100000), "NULL", ""])  # Some missing or blank salaries
    department = generate_department()
    data.append([name, age, email, join_date, salary, department])

# Create DataFrame
columns = ["Name", "Age", "Email", "Join_Date", "Salary", "Department"]
df_messy = pd.DataFrame(data, columns=columns)

# Save to CSV
file_path = "large_messy_data.csv"
df_messy.to_csv(file_path, index=False)

file_path
