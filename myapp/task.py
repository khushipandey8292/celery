from celery import shared_task
import csv
import time
import os

@shared_task
def upload_csv(file_path):
    print(f"Processing {file_path} ...")
    time.sleep(2)  # Simulating delay

    if not os.path.exists(file_path):
        return f"Error: {file_path} not found"

    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        record_count = sum(1 for _ in reader)
        
        for row in reader:
            print(f" Uploading Row: {row}")  # Har row ko terminal me print karenge
            time.sleep(0.5)
    print(f"Uploaded {file_path}, {record_count} records processed.")
    return f"Uploaded {file_path} successfully!"
