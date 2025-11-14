from django.core.management.base import BaseCommand
from octofit_tracker.models.user import User
from octofit_tracker.models.team import Team
from octofit_tracker.models.activity import Activity
from octofit_tracker.models.leaderboard import Leaderboard
from octofit_tracker.models.workout import Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team='Marvel'),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='Marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='DC'),
            User.objects.create(email='superman@dc.com', name='Superman', team='DC'),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]

        # Activities
        run = Activity.objects.create(name='Running', description='Run outdoors', points=10)
        swim = Activity.objects.create(name='Swimming', description='Swim in pool', points=15)
        cycle = Activity.objects.create(name='Cycling', description='Cycle in park', points=12)

        # Workouts
        Workout.objects.create(user=users[0].email, activity=run.name, duration=30, date='2025-11-01')
        Workout.objects.create(user=users[1].email, activity=swim.name, duration=45, date='2025-11-02')
        Workout.objects.create(user=users[3].email, activity=cycle.name, duration=60, date='2025-11-03')

        # Leaderboard
        Leaderboard.objects.create(user=users[0].email, team=users[0].team, points=100)
        Leaderboard.objects.create(user=users[3].email, team=users[3].team, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
