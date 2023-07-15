from django.test import TestCase
from django.test import TestCase, RequestFactory
from django.urls import reverse
from backend.views import top_players_view 

class BackendTest(TestCase):
    fixtures = ['backend/fixtures']

    def setUp(self):
        self.factory = RequestFactory()

    def test_top_players_view(self):
        url = reverse('top-player-details')
        request = self.factory.get(url)
        response = top_players_view(request)
        self.assertEqual(response.status_code, 200)
