from django.shortcuts import render, redirect
from Eishel_student_app.models import student_details, teacher_details, exam_details, ex_details, ans_stu, ans_key_details,temp_ans_data,temp_check_data,model_features,secondary_key_data


#####


import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer


#####

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
        

        ans_stu_obj = ans_stu(exam_id="ex_dbms",ans_by_stu=ansbystu)
        ans_stu_obj.save()

        return redirect('/after_exam')
    return render(request, 'student_exam.html')

def after_exam(request):
    return render(request, 'after_exam.html')

def enter_ans_key(request):
    if request.method == "POST":
        ansmain = request.POST.get('inputAnsMain')
        ansa = request.POST.get('inputAnsA')
        ansb = request.POST.get('inputAnsB')
        
        ans_key_details_obj = ans_key_details(examm_id="ex_dbms", ans_key_main=ansmain, ans_key_A=ansa, ans_key_B=ansb)
        ans_key_details_obj.save()

        return redirect('/teacher_home')
    return render(request, 'teacher_enter_answer_key.html')

def teacher_check(request):
    return render(request, 'teacher_check.html')










########## ########## Feature Generation ########## ########## ##################################################

stopwords = stopwords.words('english')
stemmer = PorterStemmer()

def remove_stopwords(temp):
    templi2 = []
    for word in temp:
        if (word not in stopwords and
            word not in string.punctuation):     
            templi2.append(word)
    return templi2

def stem_li(temp):
    templi3 = []
    for word in temp:
        stemmed = stemmer.stem(word)
        templi3.append(stemmed)
    return templi3
    
def process_text(tempstr):
    
    temp = re.sub(r'^RT[\s]+', '', tempstr)

    temp = re.sub(r'https?:\/\/.*[\r\n]*', '', temp)
    temp = re.sub(r'#', '', temp)
    
    templi = list(temp.split(" "))
    templi2 = remove_stopwords(templi)
    templi3 = stem_li(templi2)
    return templi2    






anskey = str(ans_key_details.objects.filter(examm_id = "ex_dbms")[0].ans_key_main)   #"This property states that a transaction must be treated as an atomic unit, that is, either all of its operations are executed or none. There must be no state in a database where a transaction is left partially completed. States should be defined either before the execution of the transaction or after the execution/abortion/failure of the transaction."
anskeyA = str(ans_key_details.objects.filter(examm_id = "ex_dbms")[0].ans_key_A)          #"transaction must be treated as an atomic unit"
anskeyB = str(ans_key_details.objects.filter(examm_id = "ex_dbms")[0].ans_key_B)          #"There must be no state in a database where a transaction is left partially completed"

secondary_knowledge = []

#anskeywordlist = list(anskey.split(" "))
anskeywordlist = process_text(anskey)
anskeysenlist = list(anskey.split("."))
#anskeyAlist = list(anskeyA.split(" "))
anskeyAlist = process_text(anskeyA)
anskeyAsenlist = list(anskeyA.split("."))
#anskeyBlist = list(anskeyB.split(" "))
anskeyBlist = process_text(anskeyB)
anskeyBsenlist = list(anskeyB.split("."))
anskeyCsenlist = []
for templist in anskeysenlist:
    if ((templist not in anskeyAsenlist)and(templist not in anskeyBsenlist)):
        anskeyCsenlist.append(templist)

m = len(anskeywordlist)
a = len(anskeyAlist)
b = len(anskeyBlist)

msen = len(anskeysenlist)
asen = len(anskeyAsenlist)
bsen = len(anskeyBsenlist)
csen = len(anskeyCsenlist)



def feature_generation_train(ansstu):
    # returns features as F1 F2 F3 F4 F5 F6 F7 F8 F9
    
    #ansstulist = list(ansstu.split(" "))
    ansstulist = process_text(ansstu)
    ansstusenlist = list(ansstu.split("."))

    stm = len(ansstulist)
    stmsen = len(ansstusenlist)
    
    countA = 0
    countB = 0
    countC = 0
    countD = 0

    countsenA = 0
    countsenB = 0
    countsenC = 0
    countsenD = 0

    ansstuA = []
    ansstuB = []
    ansstuC = []
    ansstuD = []

    occumlist = [0]*msen
    occualist = [0]*asen
    occublist = [0]*bsen
    occuclist = [0]*csen

    for word in ansstulist:
        if word in anskeyAlist:
            countA += 1
            ansstuA.append(word)
        if word in anskeyBlist:
            countB += 1
            ansstuB.append(word)
        if ((word in anskeywordlist)and((word not in anskeyAlist)and(word not in anskeyBlist))):
            countC += 1
            ansstuC.append(word)
        if word not in anskeywordlist:
            countD += 1
            ansstuD.append(word)
            if word not in secondary_knowledge:
                secondary_knowledge.append(str(word))
    

    # FEATURES
    F1 = countA / a
    F2 = countB / b 
    F3 = countC / (m-a-b)
    F4 = countD / stm
    div_3 = countD / 3
    if countD >= (stm * 0.5):
        F1 = (countA + div_3) / a
        F2 = (countB + div_3) / b
        F3 = (countC + div_3) / (m-a-b)

    for listA in anskeyAsenlist:
        for word in ansstulist:
            if word in listA:
                occualist[countsenA] += 1
        countsenA += 1
     
    for listB in anskeyBsenlist:
        for word in ansstulist:
            if word in listB:
                occublist[countsenB] += 1
        countsenB += 1


    for listC in anskeyCsenlist:
        for word in ansstulist:
            if word in listC:
                occuclist[countsenC] += 1
        countsenC += 1

    
    countoccua = 0
    for occuanum in occualist:
        temp = anskeyAsenlist[countoccua]
        lentemp = len(temp)
        if occualist[countoccua] != 0:
            occualist[countoccua] /= lentemp
        countoccua += 1
    #print(occualist)
        
    countoccub = 0
    for occubnum in occublist:
        temp = anskeyBsenlist[countoccub]
        lentemp = len(temp)
        if occublist[countoccub] != 0:
            occublist[countoccub] /= lentemp
        countoccub += 1
    #print(occublist)
        
    countoccuc = 0
    for occucnum in occuclist:
        temp = anskeyCsenlist[countoccuc]
        lentemp = len(temp)
        if occuclist[countoccuc] != 0:
            occuclist[countoccuc] /= lentemp
        countoccuc += 1
    #print(occuclist)

    f5 = 0
    for num in range(0,(len(occualist)-1)):
        if occualist[num] >= 0.3:
            f5 += 1
    f6 = 0
    for num in range(0,(len(occublist)-1)):
        if occublist[num] >= 0.3:
            f6 += 1
    f7 = 0
    for num in range(0,(len(occuclist)-1)):
        if occuclist[num] >= 0.3:
            f7 += 1

    #FEATURES
    F5 = f5 / asen
    F6 = f6 / bsen
    F7 = f7 / csen
    F8 = stm / m
    F9 = stmsen / msen

    feature_string = str(F1)+" "+str(F2)+" "+str(F3)+" "+str(F4)+" "+str(F5)+" "+str(F6)+" "+str(F7)+" "+str(F8)+" "+str(F9)
    return feature_string



def feature_generation_iter(a,b):
    for iter_data in range(a,b+1):
        temp_ansstu = str(temp_ans_data.objects.filter(stu_id = int(iter_data))[0].stu_ans)
        temp_feature = feature_generation_train(temp_ansstu)
        temp_prediction = int(temp_check_data.objects.filter(stu_id = int(iter_data))[0].given_m)
        temp_model_features_obj = model_features(stu_id = int(iter_data),feature_str = temp_feature, prediction_int = temp_prediction)
        temp_model_features_obj.save()

def store_secondary_data(se_list):
    secondary_str = ""
    for every_word in se_list:
        secondary_str = secondary_str+" "+every_word
    templist = process_text(secondary_str)
    temp_str = ""
    for every_word in templist:
        temp_str = temp_str+" "+every_word
    secondary_key_data_obj = secondary_key_data(ex_id = "ex_dbms", secondary_key = temp_str)
    secondary_key_data_obj.save()

def feature_generation_test(ansstu):
    # returns features as F1 F2 F3 F4 F5 F6 F7 F8 F9
    
    #ansstulist = list(ansstu.split(" "))
    secondary_str = str(secondary_key_data.objects.filter(ex_id = "ex_dbms")[0].secondary_key)
    se_list = list(secondary_str.split(" "))

    ansstulist = process_text(ansstu)
    ansstusenlist = list(ansstu.split("."))

    stm = len(ansstulist)
    stmsen = len(ansstusenlist)
    
    countA = 0
    countB = 0
    countC = 0
    countD = 0

    countsenA = 0
    countsenB = 0
    countsenC = 0
    countsenD = 0

    ansstuA = []
    ansstuB = []
    ansstuC = []
    ansstuD = []

    occumlist = [0]*msen
    occualist = [0]*asen
    occublist = [0]*bsen
    occuclist = [0]*csen

    for word in ansstulist:
        if word in anskeyAlist:
            countA += 1
            ansstuA.append(word)
        if word in anskeyBlist:
            countB += 1
            ansstuB.append(word)
        if ((word in anskeywordlist)and((word not in anskeyAlist)and(word not in anskeyBlist))):
            countC += 1
            ansstuC.append(word)
        if word not in anskeywordlist:
            countD += 1
            ansstuD.append(word)

    
    

    # FEATURES
    F1 = countA / a
    F2 = countB / b 
    F3 = countC / (m-a-b)
    F4 = countD / stm

    
    cred = 0
    for every_word in ansstuD:
        if every_word in se_list:
            cred += 1
        F1 = (countA + cred) / a
        F2 = (countB + cred) / b
        F3 = (countC + cred) / (m-a-b)

    for listA in anskeyAsenlist:
        for word in ansstulist:
            if word in listA:
                occualist[countsenA] += 1
        countsenA += 1
     
    for listB in anskeyBsenlist:
        for word in ansstulist:
            if word in listB:
                occublist[countsenB] += 1
        countsenB += 1


    for listC in anskeyCsenlist:
        for word in ansstulist:
            if word in listC:
                occuclist[countsenC] += 1
        countsenC += 1

    
    countoccua = 0
    for occuanum in occualist:
        temp = anskeyAsenlist[countoccua]
        lentemp = len(temp)
        if occualist[countoccua] != 0:
            occualist[countoccua] /= lentemp
        countoccua += 1
    #print(occualist)
        
    countoccub = 0
    for occubnum in occublist:
        temp = anskeyBsenlist[countoccub]
        lentemp = len(temp)
        if occublist[countoccub] != 0:
            occublist[countoccub] /= lentemp
        countoccub += 1
    #print(occublist)
        
    countoccuc = 0
    for occucnum in occuclist:
        temp = anskeyCsenlist[countoccuc]
        lentemp = len(temp)
        if occuclist[countoccuc] != 0:
            occuclist[countoccuc] /= lentemp
        countoccuc += 1
    #print(occuclist)

    f5 = 0
    for num in range(0,(len(occualist)-1)):
        if occualist[num] >= 0.3:
            f5 += 1
    f6 = 0
    for num in range(0,(len(occublist)-1)):
        if occublist[num] >= 0.3:
            f6 += 1
    f7 = 0
    for num in range(0,(len(occuclist)-1)):
        if occuclist[num] >= 0.3:
            f7 += 1

    #FEATURES
    F5 = f5 / asen
    F6 = f6 / bsen
    F7 = f7 / csen
    F8 = stm / m
    F9 = stmsen / msen

    feature_string = str(F1)+" "+str(F2)+" "+str(F3)+" "+str(F4)+" "+str(F5)+" "+str(F6)+" "+str(F7)+" "+str(F8)+" "+str(F9)
    return feature_string


def feature_generation_iter_test(a,b):
    for iter_data in range(a,b+1):
        temp_ansstu = str(temp_ans_data.objects.filter(stu_id = int(iter_data))[0].stu_ans)
        temp_feature = feature_generation_test(temp_ansstu)
        temp_prediction = int(temp_check_data.objects.filter(stu_id = int(iter_data))[0].given_m)
        temp_model_features_obj = model_features(stu_id = int(iter_data),feature_str = temp_feature, prediction_int = temp_prediction)
        temp_model_features_obj.save()

#file_f = open(r"C:\Users\as\Desktop\Eishel\FEATURES\features.txt", "a") 
def feature_to_csv(a,b):
    for i in range(a,b+1):
        model_features_obj = model_features.objects.filter(stu_id = i)[0]
        temp_f = str(model_features_obj.feature_str)
        temp_p = str(model_features_obj.prediction_int)
        temp_f_str = temp_f.replace(" ",",")
        
        final_str = str(temp_f_str) + "," + str(temp_p) + ",\n"
        file_f.write(final_str)
        

#feature_generation_iter(81,100)
#store_secondary_data(secondary_knowledge)

#feature_to_csv(81,100)
#file_f.close()