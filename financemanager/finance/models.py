from django.db import models

# Create your models here.
class BaseContent(models.Model):
    """
        Captures BaseContent as created On and modified On and active field.
        common field accessed for the following classes.
    """
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class ContactUs(BaseContent):
    dealerName = models.CharField(max_length = 255, null=True, blank=True)
    websiteURL = models.CharField(max_length = 255, null=True, blank=True)
    numOfCars  = models.CharField(max_length = 255, null=True, blank=True)
    companyName = models.CharField(max_length = 255, null=True, blank=True)
    contactName= models.CharField(max_length = 255, null=True, blank=True)
    contactPhNum= models.CharField(max_length = 255, null=True, blank=True)
    contactEmail= models.CharField(max_length = 255, null=True, blank=True)
    dealerDMS = models.CharField(max_length = 255, null=True, blank=True)
    dealerCRM= models.CharField(max_length = 255, null=True, blank=True)