"""test0210 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^show/$', 'show.views.show'),
    url(r'^knowledge/$', 'show.views.knowledge'),
    url(r'^questions/$', 'question.views.questions'),
    url(r'^answers/$', 'question.views.answers'),
    url(r'^questions/(?P<question_id>\d+)/$', 'question.views.question_detail'),
    url(r'^answers/(?P<answer_id>\d+)/$', 'question.views.answer_detail'),
    url(r'^questions/create/$','question.views.question_create'),
    url(r'^board/$', 'web.views.board'),
    url(r'^post/$','web.views.post'),
    url(r'^diary/$','web.views.diary'),
    url(r'^diary/add/$','web.views.diary_add'),
    url(r'^diary/(?P<month>\d+)/$','web.views.diary_month'),
    url(r'^home/$', 'web.views.home'),
    url(r'^diary/word/(?P<month>\d+)/$','web.views.diary_word'),
    url(r'^money/(?P<month>\d+)$','web.views.money'),
    url(r'^money/add/$','web.views.money_add'),
    url(r'^money/excel/(?P<month>\d+)/$','web.views.money_excel'),
    url(r'^$', 'web.views.home'),
]
