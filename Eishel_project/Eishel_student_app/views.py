from django.shortcuts import render, redirect
from Eishel_student_app.models import student_details, teacher_details, exam_details, ex_details, ans_stu

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
    if request.method == "POST":
        sub = request.POST.get('inputSubject')
        name = request.POST.get('inputExamname')
        date = request.POST.get('inputExamdate')
        time = request.POST.get('inputExamtime')
        stu = request.POST.get('inputNostu')
        marks = request.POST.get('inputTotalmarks')
        questions = request.POST.get('inputNoq')
        exid = request.POST.get('inputExid')
        password = request.POST.get('inputExpass')

        exam_details_obj = exam_details(ex_sub=sub, ex_name=name, ex_date=date, ex_time=time, ex_stu=stu, ex_marks=marks, ex_noq=questions, ex_id=exid, ex_pass=password)
        exam_details_obj.save()

        return redirect('/generate_questions')

    return render(request, 'teacher_create_exam.html')

def generate_questions(request):
    if request.method == "POST":
        exq = request.POST.get('inputExQ')
        exm = request.POST.get('inputExM')

        ex_details_obj = ex_details(ex_q=exq, ex_q_marks=exm)
        ex_details_obj.save()

        return redirect('/teacher_home')

    return render(request, 'teacher_generate_questions.html')

def exam_login(request):
    if request.method == "POST":
        exid = request.POST.get('inputExID')
        expass = request.POST.get('inputExPass')

        test_obj = exam_details.objects.filter(ex_id = exid)[0]
        testpass = test_obj.ex_pass
        if expass==testpass:
            return redirect('/student_exam')
        
    return render(request,  'exam_login.html')

def student_exam(request):
    if request.method == "POST":
        ansbystu = request.POST.get('inputAnsStu')

        ans_stu_obj = ans_stu(ans_by_stu=ansbystu)
        ans_stu_obj.save()

        return redirect('/after_exam')
    return render(request, 'student_exam.html')

def after_exam(request):
    return render(request, 'after_exam.html')