from django.db import models


class Thesis(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False, default='User has not provided any title')
    supervisor = models.CharField(max_length=200, null=False, default='User has not provided any supervisor')
    category = models.CharField(max_length=300, null=False, default='User has not provided any category')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'supervisor'], name='unique_order')
        ]

    def get_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'supervisor': self.supervisor,
        }

    def __str__(self):
        return f"\
            'id': {self.id},\
            'title': {self.title},\
            'category': {self.category},\
            'supervisor': {self.supervisor},\
        "

class ThesisDescription(models.Model):
    id = models.OneToOneField(Thesis, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField(null=False, default='User has not provided any description')

    def __str__(self):
        return {
            'id': self.id,
            'description': self.description
        }
