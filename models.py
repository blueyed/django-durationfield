from django.db import models

from durationfield.db.models.fields.duration import DurationField

class ModelWithDuration(models.Model):
	runtime = DurationField()

