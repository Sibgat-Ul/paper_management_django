from django.db import models

# Create your models here.


class Thesis(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    supervisor = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ThesisDetails(models.Model):
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.description
