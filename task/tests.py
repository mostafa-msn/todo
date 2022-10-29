from django.test import TestCase
from task.models import Task, Project

class ProjectTestCase(TestCase):
    def setUp(self):
        Project.objects.create(name="lion", sound="roar")
        Project.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
