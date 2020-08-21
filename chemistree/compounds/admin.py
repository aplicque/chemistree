from django.contrib import admin
from .models import Molecule, Element

# Register your models here.
admin.site.register(Molecule)
admin.site.register(Element)