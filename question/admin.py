from django.contrib import admin
from question.models import question, answer

admin.site.register(question)
admin.site.register(answer)