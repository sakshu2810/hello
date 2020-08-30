from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.




#from .models import User,Company,Problems,Student,Solution




#from .models import Company,Problems,Student,Solution
# admin.site.register(City)
# admin.site.register(Company)
# admin.site.register(Subject1)




class CompanyAdmin(admin.ModelAdmin):

    list_per_page = 5

    list_display  = ['user','c_name','owner_name','type']
    search_fields = ['user','c_name','owner_name']




class ProblemsAdmin(admin.ModelAdmin):


    #list_per_page = 5

    list_display  = ['user','c_name','problems','from_date','to_date','image','video_url']
    search_fields = ['user','c_name']




class StudentAdmin(admin.ModelAdmin):


    list_per_page = 6

    list_display  = ['user','student_name','branch','mobile_no']
    search_fields = ['user','student_name']
   






class SolutionAdmin(admin.ModelAdmin):

    list_per_page = 6

    list_display  = ['user','date','solution_name','progress','progress_details','image','video_url']
    search_fields = ['user']






admin.site.register(User,UserAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Problems,ProblemsAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Solution,SolutionAdmin)












# Register your models here.


# Register your models here.
