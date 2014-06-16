from django.contrib import admin

# Register your models here.
from .models import SignUp#tesging the signup class. this is a realtive import denoted by the dot, it goes into the same folder
class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model=SignUp
        
admin.site.register(SignUp,SignUpAdmin)