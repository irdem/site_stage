from django.contrib import admin

# Register your models here.
from .models import Image
from .models import Utilisateurs
from .models import Test
from .models import Aliment
from .models import Preference

admin.site.register(Image)
admin.site.register(Utilisateurs)
admin.site.register(Test)
admin.site.register(Aliment)
admin.site.register(Preference)