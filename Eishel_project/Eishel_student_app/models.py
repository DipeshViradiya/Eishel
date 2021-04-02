from django.db import models

# Create your models here.
class student_details(models.Model):
    st_username  = models.CharField(max_length=25)
    st_email  = models.CharField(max_length=25, primary_key=True)
    st_pass  = models.CharField(max_length=25)
    #st_dob  = models.DateField()
    st_clgname  = models.CharField(max_length=25)

class teacher_details(models.Model):
    tc_username  = models.CharField(max_length=25)
    tc_email  = models.CharField(max_length=25, primary_key=True)
    tc_pass  = models.CharField(max_length=25)
    tc_clgname  = models.CharField(max_length=25)

class exam_details(models.Model):
    ex_sub = models.CharField(max_length=25)
    ex_name = models.CharField(max_length=25)
    ex_date = models.DateField()
    ex_time = models.TimeField()
    ex_stu = models.IntegerField()
    ex_marks = models.IntegerField()
    ex_noq = models.IntegerField()
    ex_id = models.CharField(max_length=25, primary_key=True)
    ex_pass = models.CharField(max_length=25)

class ex_details(models.Model):
    exm_id = models.CharField(max_length=25, default="ex_dbms", primary_key=True)
    ex_q = models.CharField(max_length=100)
    ex_q_marks = models.IntegerField()

class ans_stu(models.Model):
    exam_id = models.CharField(max_length=25, primary_key=True)
    ex_q_no = models.IntegerField(default=1)
    ans_by_stu = models.TextField()

class ans_key_details(models.Model):
    examm_id = models.CharField(max_length=25, primary_key=True)
    ex_q_no = models.IntegerField(default=1)
    ans_key_main = models.TextField()
    ans_key_A = models.TextField()
    ans_key_B = models.TextField()

class temp_ans_data(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    stu_ans = models.TextField()

class temp_check_data(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    given_m = models.IntegerField(default=1)

class model_features(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    feature_str = models.CharField(max_length=200)
    prediction_int = models.IntegerField(default=1)

class secondary_key_data(models.Model):
    ex_id = models.CharField(max_length=25, primary_key=True)
    secondary_key = models.TextField()
