from django.contrib.auth.models import User
from django.db import models
from to_do_app import settings

# create to_do_list model
class to_do_list(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'to_do_list'
