from django.db import models

# Create your models here.
class Questionnaire(models.Model):
    question = models.CharField(verbose_name="Question", max_length=50)
    questioncategory = models.ForeignKey("questioncategory.QuestionCategory",on_delete=models.CASCADE,related_name="question_cat")
    created_date = models.DateField(verbose_name="Created date", auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Questionnaires'

    def __str__(self):
        return self.question


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Questionnaire,on_delete=models.CASCADE)
    patient = models.ForeignKey("patient.Patient",on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Question Answer'
        verbose_name_plural = 'Question Answers'

    def __str__(self):
        return self.question.question
