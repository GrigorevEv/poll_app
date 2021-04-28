from django.contrib import admin
from .models import Choice, Question, RightAnswerExplanation


class ChoiceInline(admin.TabularInline):
    '''
    Inline for question choices
    '''
    model = Choice
    extra = 2
    min_num = 2
    verbose_name = 'вариант'


class RightAnswerExplanationInline(admin.TabularInline):
    '''
    Inline for question right answer
    '''
    model = RightAnswerExplanation
    max_num = 1
    min_num = 1


class QuestionAdmin(admin.ModelAdmin):
    '''
    Customasing question panel in admin area
    '''
    fieldsets = [
        ('ТЕКСТ ВОПРОСА', {'fields':['question_text']}),
        ('ДАТА ПУБЛИКАЦИИ', {'fields':['pub_date']}),
        ]
    inlines = [ChoiceInline, RightAnswerExplanationInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
