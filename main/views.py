from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        "name": "Jaysen Lestari",
        "student_id": "2406395335",
        "class_name": "PBP-C"
    }
    return render(request, "main.html", context)