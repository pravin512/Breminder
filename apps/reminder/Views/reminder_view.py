from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions,authentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from apps.reminder.models.Reminder_models import Reminder
from apps.reminder.serializers import ReminderSerializer
from datetime import datetime, timedelta, time

class ReminderViewSet(viewsets.ViewSet):
    
    queryset = Reminder.objects.all().order_by('created_at')
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())

        queryset = self.request.user.reminder_set.filter(event_date__lte=today_end, event_date__gte=today_start)
        serializer = ReminderSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ReminderSerializer(data=request.POST)
        if serializer.is_valid():
            Reminder.objects.create(title=serializer.data['title'], quote=serializer.data['quote'], event_date=serializer.data['event_date'], user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = self.request.user.reminder_set.filter(id=pk)
        serializer = ReminderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = ReminderSerializer(data=request.POST)
        if serializer.is_valid():
            Reminder.objects.filter(id=pk).update(title=serializer.data['title'], quote=serializer.data['quote'], event_date=serializer.data['event_date'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        Reminder.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_200_OK)