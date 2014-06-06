from django.contrib import admin
from management.models import User, Country, Trip, Organization, Representative

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Trip)
admin.site.register(Organization)
admin.site.register(Representative)