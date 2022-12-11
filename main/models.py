from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Cards')
    members =  models.TextField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_date = models.DateField(auto_now_add=True)
     