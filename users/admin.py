from django.contrib import admin
from .models import CustomUser
from .models import Gasto, calendario

admin.site.register(Gasto)
admin.site.register(calendario)
admin.site.register(CustomUser)