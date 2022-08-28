from django.db import models
from django.utils.text import slugify

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=24)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    owner = models.ForeignKey('member.Member', blank=True, related_name="owner", null=True, on_delete=models.SET_NULL)
    engaged_members = models.ManyToManyField('member.Member', blank=True)
    
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    max_participants = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}")
        if self.start_date:
            self.duration = self.end_date - self.start_date
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.id}. {self.name}"