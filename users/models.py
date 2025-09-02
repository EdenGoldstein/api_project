from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user",
    )
    # membership_date = models.DateField(
    #     auto_now_add=True
    # )  # only the date it was created, not update instance

    def __str__(self):
        return self.user