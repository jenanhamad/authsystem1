from django.contrib import admin
from .models import Survey,Choices,Answer

# Register your models here.
admin.site.register(Survey)
admin.site.register(Choices)
admin.site.register(Answer)


