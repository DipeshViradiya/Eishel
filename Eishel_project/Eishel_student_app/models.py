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

class exam_details(models,Model):
    ex_sub  = models.CharField(max_length=25)
    ex_name  = models.CharField(max_length=25)
    ex_date  = models.CharField(max_length=)
    ex_time  = models.CharField(max_length=)
    ex_nost  = models.CharField(max_length=)
    ex_noq  = models.CharField(max_length=)
    ex_id  = models.CharField(max_length=)
    ex_pass  = models.CharField(max_length=)
