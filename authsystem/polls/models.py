from django.db import models
from django.conf import settings
# Create your models here.

class Survey(models.Model):
    # survey_id = models.BigAutoField(primary_key=True ,)
    title = models.CharField(max_length=100)
    qustion1= models.TextField(default="meeting time",editable=False)
    qustion2= models.TextField(default="meeting Date",editable=False)
    qustion3= models.TextField(default="meeting place",editable=False)
    qustion4= models.TextField(default="Attendence",editable=False)
    created_at=models.DateTimeField(auto_now =True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Choices(models.Model):
    survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    qustion = models.IntegerField()

class Answer(models.Model):
    voter_id =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    voteing_time = models.DateTimeField(auto_now=True)
    answer = models.ForeignKey(Choices, on_delete=models.CASCADE)



