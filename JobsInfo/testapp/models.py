from django.db import models

class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()


class BngJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
