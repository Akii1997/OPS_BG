from django.contrib import admin
from .models import Questions, StandardAnswer, FormQuestions
# Register your models here.

admin.site.register(Questions)
admin.site.register(StandardAnswer)
admin.site.register(FormQuestions)
