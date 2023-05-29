import random
import string

ALLOWED_DEPARTMENTS = ["Marketing", "Accounting", "FinOps"]

def generate_ec2_names(num_instances, department_name):
    ec2_names = []
    
    for _ in range(num_instances):
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        ec2_name = f"{department_name}-{random_chars}"
        ec2_names.append(ec2_name)
    
    return ec2_names

def main():
    num_instances = int(input("Enter the number of EC2 instances you want names for: "))
    department_name = input("Enter the name of your department: ")
    
    department_name = department_name.lower().capitalize()
    
    if department_name in ALLOWED_DEPARTMENTS:
        ec2_names = generate_ec2_names(num_instances, department_name)
        
        print("\nGenerated EC2 names:")
        for name in ec2_names:
            print(name)
    else:
        print("You should not use this Name Generator. Please choose from the following departments:")
        print(", ".join(ALLOWED_DEPARTMENTS))

if __name__ == "__main__":
    main()
