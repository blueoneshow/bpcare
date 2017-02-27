from django.contrib import admin
from web.models import Message
from web.models import Diary, Month
from web.models import Money, Test

admin.site.register(Diary)
admin.site.register(Month)
admin.site.register(Message)
admin.site.register(Money)
admin.site.register(Test)