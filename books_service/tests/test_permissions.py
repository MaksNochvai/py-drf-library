from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.views import APIView
from books_service.permissions import IsAdminOrIfAuthenticatedReadOnly


class TestIsAdminOrIfAuthenticatedReadOnly:
    def setup(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='user', password='password')
        self.staff_user = User.objects.create_user(username='staff', password='password', is_staff=True)

    def test_authenticated_read_only(self):
        request = self.factory.get('/')
        force_authenticate(request, user=self.user)
        permission = IsAdminOrIfAuthenticatedReadOnly()
        assert permission.has_permission(request, APIView())

    def test_authenticated_staff(self):
        request = self.factory.post('/')
        force_authenticate(request, user=self.staff_user)
        permission = IsAdminOrIfAuthenticatedReadOnly()
        assert permission.has_permission(request, APIView())

    def test_anonymous_read_only(self):
        request = self.factory.get('/')
        permission = IsAdminOrIfAuthenticatedReadOnly()
        assert permission.has_permission(request, APIView())

    def test_anonymous_write(self):
        request = self.factory.post('/')
        permission = IsAdminOrIfAuthenticatedReadOnly()
        assert not permission.has_permission(request, APIView())

    def test_authenticated_write(self):
        request = self.factory.post('/')
        force_authenticate(request, user=self.user)
        permission = IsAdminOrIfAuthenticatedReadOnly()
        assert not permission.has_permission(request, APIView())
