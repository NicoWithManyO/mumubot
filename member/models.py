from django.db import models

# Create your models here.
class Member(models.Model):
    discord_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, blank=True)
    discriminator = models.IntegerField(blank=True)
    
    guild = models.CharField(max_length=128, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}#{self.discriminator}"