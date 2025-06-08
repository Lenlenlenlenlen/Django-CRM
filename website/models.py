from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	producer = models.CharField(max_length=100)
	voicebank_avatar = models.CharField(max_length=100)
	length = models.CharField(max_length=100)
	year_released = models.CharField(max_length=100)

	def __str__(self):
		return(f"{self.title} {self.producer}")