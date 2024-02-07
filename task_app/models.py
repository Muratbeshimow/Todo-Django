from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('Personal', 'Personal'),
    ('Work', 'Work'),
    ('Shop', 'Shop'),
    ('Sport', 'Sport'),
    ('Cleaning', 'Cleaning'),
    ('Other', 'Other'),
]


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
