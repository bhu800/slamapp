from django.db import models

# Create your models here.
class tableThree(models.Model):
    senior = models.ForeignKey('dashboard.senior_users', related_name='entries',on_delete=models.CASCADE)
    junior = models.CharField(max_length=264)
    ans1 = models.TextField(max_length=1000)
    ans2 = models.TextField(max_length=1000)
    ans3 = models.TextField(max_length=1000)
    ans4 = models.TextField(max_length=1000)
    ans5 = models.TextField(max_length=1000)
    ans6 = models.TextField(max_length=1000)
    ans7 = models.TextField(max_length=1000)
    ans8 = models.TextField(max_length=1000)
    ans9 = models.TextField(max_length=1000)
    ans10 = models.TextField(max_length=1000)
    ans11 = models.TextField(max_length=1000)
    ans12 = models.TextField(max_length=1000)
    ans13 = models.TextField(max_length=1000)
    ans14 = models.TextField(max_length=1000)
    ans15 = models.TextField(max_length=1000)

class senior_users(models.Model):
    email = models.CharField(max_length=200, default="b16000@students.iitmandi.ac.in")
    name = models.CharField(max_length=264, default="Cool Senior")
    tag_line = models.CharField(max_length=264, default="I am Cool...")
    nick_name = models.CharField(max_length=264, default="stud")
    story_name = models.CharField(max_length=264, default="phuk")
    avatar = models.ImageField(upload_to="static/dashboard/img/Avatars/sideways", default="static/dashboard/img/Avatars/sideways/background_removed.png")
    avatar_standing = models.ImageField(upload_to="static/dashboard/img/Avatars/standing", default="static/dashboard/img/Avatars/standing/background_removed.png")