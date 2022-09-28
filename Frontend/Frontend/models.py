from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Frontend(models.model):
    ammount=models.IntegerField(_MAX_LENGTH=100)
    account=models.IntegerField(_MAX_LENGTH=100)