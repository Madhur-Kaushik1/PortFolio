from django.contrib import admin
from .models import frontend_skills, lang, framework, database, dsa, deploy
admin.site.register(frontend_skills)
admin.site.register(lang)
admin.site.register(framework)
admin.site.register(database)
admin.site.register(dsa)
admin.site.register(deploy)