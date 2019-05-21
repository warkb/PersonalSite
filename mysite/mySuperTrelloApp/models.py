from django.db import models

class Desc(models.Model):
    name = models.CharField(max_length=200, help_text='Имя доски')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'
        app_label = 'mySuperTrelloApp'

class Card(models.Model):
    text = models.TextField(help_text='Позиция на доске')
    date = models.DateTimeField(auto_now_add=True, help_text='Время создания')
    desc = models.ForeignKey(Desc, on_delete=models.CASCADE, help_text='Родительская доска')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
        app_label = 'mySuperTrelloApp'
