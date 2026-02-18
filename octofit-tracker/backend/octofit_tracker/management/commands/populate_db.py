from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel', superpower='Powered Armor'),
            User(email='captain@marvel.com', name='Captain America', team='Marvel', superpower='Super Soldier'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel', superpower='Spider Sense'),
            User(email='batman@dc.com', name='Batman', team='DC', superpower='Detective Skills'),
            User(email='superman@dc.com', name='Superman', team='DC', superpower='Super Strength'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', superpower='Amazonian Warrior'),
        ]
        for user in users:
            user.save()

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Upper body workout', difficulty='Easy'),
            Workout(name='Running', description='Cardio workout', difficulty='Medium'),
            Workout(name='Deadlift', description='Strength workout', difficulty='Hard'),
        ]
        for workout in workouts:
            workout.save()

        # Create activities
        Activity.objects.create(user=users[0], activity_type='Pushups', duration=30, date='2026-02-18')
        Activity.objects.create(user=users[3], activity_type='Running', duration=45, date='2026-02-18')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
