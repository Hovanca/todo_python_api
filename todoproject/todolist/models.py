from django.db import models

# Create your models here.
#cela magia kde sa vytvara to do ako bude vyzerat tie stlpce

class Todo(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
    status = models.BooleanField(default = False)

    def __str__(self):
        return self.title
