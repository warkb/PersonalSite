# Generated by Django 2.2 on 2019-04-23 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mySuperTrelloApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'Карточка', 'verbose_name_plural': 'Карточки'},
        ),
        migrations.AlterModelOptions(
            name='desc',
            options={'verbose_name': 'Доска', 'verbose_name_plural': 'Доски'},
        ),
        migrations.AlterField(
            model_name='card',
            name='data',
            field=models.DateTimeField(auto_now_add=True, help_text='Время создания'),
        ),
        migrations.AlterField(
            model_name='card',
            name='desc',
            field=models.ForeignKey(help_text='Родительская доска', on_delete=django.db.models.deletion.CASCADE, to='mySuperTrelloApp.Desc'),
        ),
        migrations.AlterField(
            model_name='card',
            name='position',
            field=models.PositiveIntegerField(help_text='Позиция на доске'),
        ),
        migrations.AlterField(
            model_name='card',
            name='text',
            field=models.TextField(help_text='Позиция на доске'),
        ),
        migrations.AlterField(
            model_name='desc',
            name='name',
            field=models.CharField(help_text='Имя доски', max_length=200),
        ),
    ]
