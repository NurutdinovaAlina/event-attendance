import datetime

from django.conf import settings
from django.db import models
from django.shortcuts import reverse

from localflavor.us.models import (
    PhoneNumberField,
    USZipCodeField,
    USStateField,
)


class Event(models.Model):
    id_event=models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    null=True)
    event_admin = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    event_date = models.DateField(default=datetime.date.today, blank=True)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    gps_loc = models.CharField(max_length=255)
    event_duration= models.CharField(max_length=255)
    date_published = models.DateField(default=datetime.date.today, blank=True)
    def __str__(self):
        return f'{self.name} ({self.event_date})'

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})


class EventParticipant(models.Model):
    id_event = models.ForeignKey(Event, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    login = models.CharField(max_length=255, blank=True)
    group = models.IntegerField()
    gps_loc = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name or ""} ({self.email or "[No Email Given]"})'
