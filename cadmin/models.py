from django.db import models


class Visitor(models.Model):
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField(default=0)
    first_visit_date = models.DateTimeField(auto_now_add=True)
    recent_visit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_address
