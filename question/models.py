from django.db import models
#from django import forms

class question(models.Model):
    subject = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.subject

class answer(models.Model):
    question = models.ForeignKey(question)
    content = models.TextField()

    def __unicode__(self):
        return self.content