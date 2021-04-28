import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    '''
    Model of questions that are on the main page of the site
    '''
    question_text = models.CharField('', max_length=200)
    pub_date = models.DateTimeField('')

    class Meta():
        verbose_name = 'вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Опубликовано недавно?'


class Choice(models.Model):
    '''
    Question answer model
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Варианты', max_length=200)
    votes = models.IntegerField('Кол-во голосов', default=0)

    class Meta():
        verbose_name_plural = 'Варианты ответов'

    def __str__(self):
        return self.choice_text
    

class RightAnswerExplanation(models.Model):
    '''
    Explanation of the correct answer
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_explanation = models.TextField('')

    class Meta():
        verbose_name = 'Пояснение к правильному ответу'

    def __str__(self):
        return self.answer_explanation

