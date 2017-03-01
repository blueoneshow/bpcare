# -*- coding: UTF-8 -*-
from django import forms
from web.models import Diary, Money

#留言板格式
class MessageForm(forms.Form):
        user = forms.CharField(max_length=50, required=True)
        subject = forms.CharField(max_length=100, required=True)
      
#日誌表單
class DiaryForm(forms.ModelForm):
        class Meta:
                model = Diary
                fields = ['memo']
          
# 帳本表單
class MoneyForm(forms.ModelForm):
        RELEVANCE_CHOICES = (
                (1, "早上起床後"),
                (2, "晚上睡覺前"),
                (3, "其他時機"),
        )
        kind = forms.ChoiceField(choices = RELEVANCE_CHOICES, required=True)

        class Meta:
                model = Money
                fields = ['kind', 'item', 'price']

        def __init__(self, *args, **kwargs):
                super(MoneyForm, self).__init__(*args, **kwargs)                
                self.fields['kind'].label = "測量時機"
                self.fields['item'].label = "收縮壓"
                self.fields['price'].label = "舒張壓"