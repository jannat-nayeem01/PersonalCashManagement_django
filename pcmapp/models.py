from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
class AddCash(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="cash_added")
    source = models.CharField(max_length=255)
    datetime = models.DateTimeField(verbose_name="Date when Cash Added")
    description = models.TextField(blank=True)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.source} - {self.amount}"


class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="expenses")
    description = models.TextField(blank=True)
    amount = models.IntegerField()
    datetime = models.DateTimeField(verbose_name="Date when Cash Spent")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.description[:30]} - {self.amount}"
    
    
