from django.db import models
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
def validate_question_text(value):
	if len(value)<5:
		raise ValidationError("Plz input maximum 5 charecter :")
	else:
		return value	

class Question(models.Model):
	question_text = models.CharField(max_length=200,validators=[validate_question_text])
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now
		return now-datetime.timedelta(days=1) <= self.pub_date <= now
		#return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question , on_delete=models.CASCADE)
	choice_text =models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

print("i ama modified again this file ")