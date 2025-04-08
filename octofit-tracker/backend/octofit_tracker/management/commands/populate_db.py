from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(id=ObjectId(), email='user1@example.com', name='User One', password='password1'),
            User(id=ObjectId(), email='user2@example.com', name='User Two', password='password2'),
            User(id=ObjectId(), email='user3@example.com', name='User Three', password='password3'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team = Team(id=ObjectId(), name='Team Alpha', members=[user.id for user in users])
        team.save()

        # Create activities
        activities = [
            Activity(id=ObjectId(), user=users[0], type='Running', duration=60, date='2025-04-01'),
            Activity(id=ObjectId(), user=users[1], type='Cycling', duration=90, date='2025-04-02'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(id=ObjectId(), team=team, points=100),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(id=ObjectId(), name='Morning Run', description='A quick morning run'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
