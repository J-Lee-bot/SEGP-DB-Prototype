from django.db import models
	
class House(models.Model):
	HouseName = models.CharField(max_length=30)
	HousePoints = models.IntegerField(default=0)
	
class Students(models.Model):
	StudentID = models.IntegerField
	StudentName = models.CharField(max_length=30)
	HouseName = models.ForeignKey('House', on_delete=models.CASCADE)
