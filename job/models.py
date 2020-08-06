from django.db import models

# Create your models here.
JOB_TYPE = (
    ("full time","full time"),
    ("part time","part time"),
)
class job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    publish_at = models.DateTimeField(auto_now=True)
    salary = models.IntegerField(default=0)
    exper = models.IntegerField(default=1)
    Vacancy = models.IntegerField(default=1)


    def __str__(self):
        return self.title
    