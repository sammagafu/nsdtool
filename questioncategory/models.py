from django.db import models

class QuestionCategory(models.Model):
    category = models.CharField(verbose_name="Question Category", max_length=180)
    created_date = models.DateField(verbose_name="Created date", auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Questionnaires'

    def __str__(self):
        return self.category