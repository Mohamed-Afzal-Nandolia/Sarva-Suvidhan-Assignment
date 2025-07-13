from django.db import models

class User(models.Model):
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.phone

class KYCForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    aadhar_number = models.CharField(max_length=12)

    aadhar_front = models.FileField(upload_to='kyc_docs/')
    aadhar_back = models.FileField(upload_to='kyc_docs/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"KYCForm - {self.name}"
