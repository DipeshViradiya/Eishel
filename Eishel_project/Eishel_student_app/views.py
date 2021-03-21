from django.shortcuts import render, redirect
from Eishel_student_app.models import student_details, teacher_details

# Create your views here.

def index(request):
    if request.method == "POST":
        username  = request.POST.get('inputUsername')
        email  = request.POST.get('inputEmail')
        password  = request.POST.get('inputPassword')
        #dob  = request.POST.get('inputDate')
        clgname  = request.POST.get('inputCollegeName')

        student_details_obj = student_details(st_username=username, st_email=email, st_pass=password, st_clgname=clgname)
        student_details_obj.save()

        return redirect('/exam_login')

    return render(request, 'index.html')

def student_login(request):
    if request.method == "POST":
        email = str(request.POST.get('inputEmail'))
        password = str(request.POST.get('inputPassword'))

        test_obj = student_details.objects.filter(st_email = email)[0]
        test_pass = test_obj.st_pass
        if password==test_pass:
            return redirect('/exam_login')


    return render(request, 'student_login.html')

def teacher_signup(request):
    if request.method == "POST":
        username  = request.POST.get('inputUsername')
        email  = request.POST.get('inputEmail')
        password  = request.POST.get('inputPassword')
        clgname  = request.POST.get('inputCollegeName')

        teacher_details_obj = teacher_details(tc_username=username, tc_email=email, tc_pass=password, tc_clgname=clgname)
        teacher_details_obj.save()

        return redirect('/teacher_home')

    return render(request, 'teacher_signup.html')

def teacher_login(request):
    if request.method == "POST":
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')

        test = teacher_details.objects.filter(tc_email = email)[0]
        test_pass = test.tc_pass
        if password==test_pass:
            return redirect('/teacher_home')
        return redirect('/teacher_home')

    return render(request, 'teacher_login.html')

def teacher_home(request):
    return render(request, 'teacher_home.html')

def create_exam(request):
    return render(request, 'teacher_create_exam.html')

def exam_login(request):
    return render(request,  'exam_login.html')