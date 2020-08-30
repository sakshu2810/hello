from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError

def validate_image(image):
    file_size = image.file.size
    
    
    limit_mb = 2
    if file_size>limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB " % limit)



class User(AbstractUser):
    pass
    
    

class Company(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    c_name = models.CharField(max_length=300)
    owner_name = models.CharField(max_length=300)
    type = models.CharField(max_length=300 )
   

    def __str__(self):
        return self.c_name



class Problems(models.Model):
  
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    #user_name = models.CharField(max_length=30)                                          
    c_name = models.ForeignKey("Company", on_delete=models.CASCADE)
    problems= models.TextField(max_length=400)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    image = models.FileField(upload_to='images/',validators=[validate_image,FileExtensionValidator(allowed_extensions=['jpeg','jpg','pdf'])], blank=True, null=True, editable=True)
    video_url = models.URLField(max_length=300)
    


    def __str__(self):
        return self.problems
 
    #'user','c_name','problems','from_date','to_date','image','video_url'
   
class Student(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    #user_name = models.CharField(max_length=50)
    student_name = models.CharField(max_length=300)
    branch = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=10)
    #education = models.CharField(max_lenght=300)
    #state = models.CharField(max_lenght=300)
    #address = models.CharField(max_length= 300)

    def __str__(self):
        return self.student_name
   #'user','student_name','branch','mobile_no'
  

class Solution(models.Model):
    #user_name = models.CharField(max_length=50)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    date = models.DateTimeField()
    solution_name = models.CharField(max_length=100)
    progress = models.TextField(max_length=500,null =True)
    progress_details= models.TextField(max_length=500,null =True)
    image = models.FileField(upload_to='images/',validators=[validate_image,FileExtensionValidator(allowed_extensions=['jpeg','jpg','pdf'])], blank=True, null=True, editable=True)
    video_url = models.URLField(max_length=300)
    
    
    #'user','date','solution_name','progress','progress_details','image','video_url'