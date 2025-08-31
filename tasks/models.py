from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    """
    This is model for the tasks created by users
    @Fields: status_choices - a list of choices of status of task
            user - creator of the task
            title - title of the task
            description - brief description of the task
            status - status of the task
            created_at - time when it was created
    """
    STATUS_CHOICES = [
        ('PENDING', 'pending'),
        ('IN_PROGRESS', 'in progress'),
        ('COMPLETED', 'completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return (
            f"""
            Title: {self.title}\n
            Description: {self.description}\n
            Created at: {self.created_at}\n
            Status: {self.status}
            """
        )
