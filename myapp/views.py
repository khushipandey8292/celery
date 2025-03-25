from django.shortcuts import render
# from myceleryproject.celery import sub

# def index(request):
#     print("Results: ")
#     result1=sub.delay(10,20)
#     print("Results 1:", result1)
#     return render(request,"home.html")

# def about(request):
#     return render(request,'about.html')

# def contact(request):
#     return render(request,'contact.html')

from django.http import JsonResponse
from .task import upload_csv
import os

def upload_all_csv(request):
    folder_path = "csv_files"
    if not os.path.exists(folder_path):
        return JsonResponse({"error": "CSV folder not found"}, status=400)

    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".csv")]
    
    for file in files:
        upload_csv.delay(file)
    
    return JsonResponse({"message": "CSV upload started!"})
