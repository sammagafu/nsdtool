from django.db import models

class QuestionCategory(models.Model):
    category = models.CharField(verbose_name="Question Category", max_length=50)
    age = models.IntegerField(default=0,verbose_name="Age in Month's" )
    created_date = models.DateField(verbose_name="Created date", auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Questionnaires'

    def __str__(self):
        return self.question