from django.db import models
from account.models import CustomUser

# Create your models here.


class Voter(models.Model):
    CONSTITUENCY_CHOICES = [
        ("Shangri-la-Town", "Shangri-la-Town"),
        ("Northern-Kunlun-Mountain", "Northern-Kunlun-Mountain"),
        ("Western-Shangri-la", "Western-Shangri-la"),
        ("Naboo-Vallery", "Naboo-Vallery"),
        ("New-Felucia", "New-Felucia"),
    ]
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, unique=True)  # Used for OTP
    otp = models.CharField(max_length=10, null=True)
    verified = models.BooleanField(default=False)
    voted = models.BooleanField(default=False)
    otp_sent = models.IntegerField(default=0)  # Control how many OTPs are sent
    constituency = models.CharField(
        max_length=50, choices=CONSTITUENCY_CHOICES, default="Shangri-la-Town"
    )
    uvc = models.CharField(max_length=8, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.admin.last_name} {self.admin.first_name} - {self.constituency}"


class Position(models.Model):
    name = models.CharField(max_length=50, unique=True)
    max_vote = models.IntegerField()
    priority = models.IntegerField()

    def __str__(self):
        return self.name


class Candidate(models.Model):
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="candidates", default="candidates/profile1.jpg")
    bio = models.TextField(blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Votes(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
