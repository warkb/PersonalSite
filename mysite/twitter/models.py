from django.db import models

class Statement(models.Model):
    author = models.CharField(max_length=100)
    textOfStatement = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return '%s: %s' % (self.author, self.textOfStatement)

