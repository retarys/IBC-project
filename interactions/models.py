from xml.etree.ElementTree import Comment
from django.db import models

class Snippet(models.Model):
    EVENT = 'Event'
    MEETING = 'Meeting'
    interaction_type_choices = [
        (EVENT,'Event'),
        (MEETING,'Meeting')
    ]
    interaction_type = models.CharField(
        max_length=100,
        choices=interaction_type_choices,
        default=EVENT
        )
    date = models.DateField(auto_now=False, auto_now_add=False)
    default_time = '12:00:00'
    time = models.TimeField(auto_now=False, auto_now_add=False, default=default_time)
    comment = models.TextField()
    def __str__(self):
        return self.interaction_type