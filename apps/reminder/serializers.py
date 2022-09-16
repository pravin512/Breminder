from rest_framework import serializers
from apps.reminder.models.Reminder_models import Reminder

class ReminderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'title', 'quote', 'event_date']