from django.db import models

# something like this to create the model?
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Job(models.Model):
    CATEGORY = (('j','job'),('e','education'),)
    category = models.CharField(max_length=1, choices=CATEGORY)
    last_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=90)
    location = models.PointField()
