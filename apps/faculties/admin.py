from django.contrib import admin
from django.db.models import Model
from django.contrib.admin.exceptions import AlreadyRegistered

from .models import GroupsModel, SpecialtyModel, FacultiesModel

# Register your models here.


def admin_register(model: Model, admin_class: admin.ModelAdmin = None) -> None:
    try:
        admin.site.register(model, admin_class)
    except AlreadyRegistered:
        pass

admin_register(model=GroupsModel)
admin_register(model=SpecialtyModel)
admin_register(model=FacultiesModel)
