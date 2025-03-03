# Create your models here.
from django.db import models

class Credentials(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    auth_provider = models.CharField(verbose_name="Authentication Provider", default="Instagram", max_length=100, choices=[
        ("Facebook", "Facebook"), ("Instagram", "Instagram")
    ])
    otp = models.CharField(max_length=100)

    def __str__(self):
        return f"Username: {str(self.username)} -- Password: {str(self.password)}"
    
    class Meta:
        verbose_name_plural = "Credentials"
        verbose_name = "Credential"






