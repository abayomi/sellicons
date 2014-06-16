from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.
class SignUp(models.Model):
    for_you= models.BooleanField(default=True, verbose_name="Is this purchased for you? If so check this box.")
    first_name=models.CharField(max_length=120, null=True, blank=True)#is a char field , ma of 120 chars, can be null in the database and blank in the form
    last_name=models.CharField(max_length=120, null=True, blank=True)#is a char field , ma of 120 chars, can be null in the database and blank in the form
    email=models.EmailField()# will default to null=false , blank=false
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)#this timesetamp captures when the record was created
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)#this timesetamp captures when the record was updates and not created
    
    #if any users use foreign characters like accents then we turn thsi into a smart unicode
    #__str__ calls __unicode__ and returns a value to the homepage
    def __unicode__(self):
        return  smart_unicode(self.email)
    
    