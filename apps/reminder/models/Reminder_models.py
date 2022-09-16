from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Reminder(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'InActive'),
    ]
    id = models.AutoField(db_column='id', primary_key=True)
    user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE)
    title = models.CharField(db_column='title', max_length=254, validators=[MinLengthValidator(3)])
    quote = models.TextField(db_column='quote', blank=True, null=True)
    image = models.ImageField(db_column='reminder_thumbnail', upload_to='uploads/', max_length=500, blank=True, null=True)
    event_date = models.DateField(db_column='event_date')
    created_at = models.DateTimeField(db_column='created_at', auto_now_add=True, editable=False)
    expire_at = models.DateTimeField(db_column='expire_at', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, db_column='updated_at')
    status = models.PositiveSmallIntegerField(db_column='status', choices=STATUS_CHOICES, default=1)

    class Meta:
        managed = True
        db_table = 'reminder'

    def __str__(self):
        return self.title