from django.contrib import admin
from Eishel_student_app.models import student_details,teacher_details,exam_details,ex_details,ans_stu,ans_key_details

# Register your models here.

admin.site.register(student_details)
admin.site.register(teacher_details)
admin.site.register(exam_details)
admin.site.register(ex_details)
admin.site.register(ans_stu)
admin.site.register(ans_key_details)