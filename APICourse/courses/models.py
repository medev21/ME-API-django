from django.db import models

# Create your models here.

class Course(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 100, blank = True, default = "")
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name = 'courses')

    class Meta:
        ordering = ('created',)
