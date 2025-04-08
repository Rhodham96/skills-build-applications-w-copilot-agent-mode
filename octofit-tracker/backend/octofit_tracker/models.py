from djongo import models
from bson import ObjectId

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=255)
    members = models.JSONField()

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=255)
    description = models.TextField()
