import os
import csv
import shutil
from .models import UserData
from celery import shared_task
from time import sleep

# @shared_task
# def add(x,y):
#     sleep(10)
#     return x+y

@shared_task
def generate_and_upload_csv(*args):
    source_dir = "csv_files"
    destination_dir = "uploaded_files"

    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(destination_dir, exist_ok=True)

    for i in range(10):
        file_path = os.path.join(source_dir, f'file_{i}.csv')
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name']) 
            for j in range(1, 6):
                writer.writerow([j, f'User{i}{j}']) 
        print(f" Created: {file_path}")        
        sleep(1) 
    
    for file_name in os.listdir(source_dir):
        if file_name.endswith(".csv"):
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    UserData.objects.create(user_id=row[0], name=row[1])
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, file_name))
            print(f" Uploaded: {file_name}") 
            sleep(2)  

    return "CSV Generation & Upload Success"
