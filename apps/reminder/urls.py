from django.urls import path
from apps.reminder.Views.reminder_view import ReminderViewSet

app_name = 'reminders'
urlpatterns = [
    path('create', ReminderViewSet.create, name='create')
]