from django.db import models

class UserData(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.name}"

