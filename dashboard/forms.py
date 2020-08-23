from django import forms
from django.core import validators

class fillSlambook(forms.Form):
    # Your Questions Goes inside labels
    ans1 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 1 goes here")
    ans2 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 2 goes here")
    ans3 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 3 goes here")
    ans4 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 4 goes here")
    ans5 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 5 goes here")
    ans6 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 6 goes here")
    ans7 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 7 goes here")
    ans8 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 8 goes here")
    ans9 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 9 goes here")
    ans10 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 10 goes here")
    ans11 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 11 goes here")
    ans12 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 12 goes here")
    ans13 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 13 goes here")
    ans14 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 14 goes here")
    ans15 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 15 goes here")
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])