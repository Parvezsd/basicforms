from django.contrib import admin # type: ignore
from app.models import *
# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)