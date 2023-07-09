from django.db import models
from django.utils import timezone

# Create your models here.
class Questionnaire(models.Model):
    question = models.CharField(verbose_name="Question", max_length=255)
    questioncategory = models.ForeignKey("questioncategory.QuestionCategory",on_delete=models.CASCADE,related_name="questions")
    age = models.IntegerField(default=0,verbose_name="Age in Month's" )
    whattodo = models.CharField(verbose_name="What to do or watch", max_length=255,default="What to do or watch",blank=True,null=True)
    tools = models.CharField(verbose_name="Tools", max_length=255,blank=True,null=True)
    created_date = models.DateField(verbose_name="Created date", auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Questionnaires'

    def __str__(self):
        return self.question


class QuestionAnswer(models.Model):
    visitdate = models.DateField(verbose_name="visit date", auto_now=True)
    question = models.ForeignKey(Questionnaire,on_delete=models.CASCADE,related_name="questions")
    patient = models.ForeignKey("patient.Patient",on_delete=models.CASCADE,related_name="patientQuestion")
    answer = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Question Answer'
        verbose_name_plural = 'Question Answers'

    def __str__(self):
        return self.question.question

class PatientComment(models.Model):
    patient = models.ForeignKey("patient.Patient",on_delete=models.CASCADE,related_name="patientComment", null=True, blank=True)
    commentCategory = models.ForeignKey("questioncategory.QuestionCategory",on_delete=models.CASCADE,related_name="commentCategory")
    comment = models.TextField()
