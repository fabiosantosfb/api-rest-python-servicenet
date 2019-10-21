from django.contrib import admin
from django.apps import apps
from django.contrib.auth.models import User, Group

app = apps.get_app_config('projeto')


admin.site.unregister(User)
admin.site.unregister(Group)

for model_name, model in app.models.items():
    admin.site.register(model)
