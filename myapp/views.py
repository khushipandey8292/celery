from django.shortcuts import render
from django.http import JsonResponse
from myapp.tasks import generate_and_upload_csv
# from myceleryproject.celery import sub
# from myapp.tasks import add

# def index(request):
#     print("Results: ")
#     result1=sub.delay(10,20)
#     print("Results 1:", result1)
#     result2=add.delay(10,20)
#     print("Results 2:", result2)
#     return render(request,"home.html")

# def about(request):
#     return render(request,'about.html')

# def contact(request):
#     return render(request,'contact.html')

def start_csv_process(request):
    task = generate_and_upload_csv.delay()
    return JsonResponse({"message": "CSV Generation & Upload Started!" })


