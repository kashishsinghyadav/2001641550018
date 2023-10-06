from django.contrib import admin
from Registerusre.models import RegisterUser

class Register(admin.ModelAdmin):
    list_display=('companyname','ownername','rollno','owneremail','accesscode')
admin.site.register(RegisterUser,Register)

# Register your models here.
