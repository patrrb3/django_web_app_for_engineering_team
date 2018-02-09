from django.contrib import admin
from appTwo.models import Site, Document, UserProfileInfo

# Register your models here.
admin.site.register(Site)
admin.site.register(Document)
admin.site.register(UserProfileInfo)
