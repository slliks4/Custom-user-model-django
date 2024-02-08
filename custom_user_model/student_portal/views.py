from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def Student_portal(request):
    return render(request, 'student_portal.html')
