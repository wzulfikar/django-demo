from django.contrib import admin
from .models import Question

# Register your models here.

# Make the poll app modifiable in the admin
admin.site.register(Question)

admin.site.site_header = 'Django Demo Admin Panel'