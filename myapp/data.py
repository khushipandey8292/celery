import csv
import os

def create_csv_files():
    os.makedirs("csv_files", exist_ok=True)

    for i in range(1, 11):
        file_path = f"csv_files/file_{i}.csv"
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age"]) 
            
            for j in range(1, 101):  
                writer.writerow([j, f"User_{j}", (j % 50) + 18])
        
        print(f"{file_path} created!")

if __name__ == "__main__":
    create_csv_files()
