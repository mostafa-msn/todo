from django.test import RequestFactory, TestCase
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User, AnonymousUser
from account.models import UserProfile
from task.models import Task, Project
from task.views import ProjectListAPI


class ProjectTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()
        # create data
        self.developer = User.objects.create_user(
            username="developer", email=None, password="password",
            first_name="mostafa", last_name="soltani",
        )
        self.manager = User.objects.create_user(
            username="project_manager", email=None, password='password',
            first_name="mike", last_name="soltani",
        )
        UserProfile.objects.create(user=self.developer, role=1)
        UserProfile.objects.create(user=self.manager, role=2)
        Project.objects.create(user=self.manager, title="project_1", description="project description")

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/project/list')
        # Use this syntax for class-based views.
        force_authenticate(request, user=self.manager)
        response = ProjectListAPI.as_view()(request)
        self.assertEqual(response.status_code, 200)


