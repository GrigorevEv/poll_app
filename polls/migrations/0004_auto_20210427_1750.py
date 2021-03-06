# Generated by Django 3.2 on 2021-04-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rightanswerexplanation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name_plural': 'Варианты ответов'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='rightanswerexplanation',
            options={'verbose_name': 'Пояснение к правильному ответу'},
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200, verbose_name='Варианты'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='Кол-во голосов'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='rightanswerexplanation',
            name='answer_explanation',
            field=models.TextField(verbose_name=''),
        ),
    ]
