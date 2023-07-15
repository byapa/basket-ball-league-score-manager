from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from backend.views import top_players_view
from django.core.management import call_command
import os
import json


class BackendTest(TestCase):
    def setUp(self):
        self.client = Client()
        fixture_dir = "backend/fixtures"
        fixtures = [
            os.path.join(fixture_dir, file_name)
            for file_name in os.listdir(fixture_dir)
            if file_name.endswith(".json")
        ]
        call_command("loaddata", *fixtures)

    def test_top_players_view(self):

        response = self.client.get('/api/teams/1/top-players')
        self.assertEqual(response.status_code, 200)

        max_numb_of_players_per_team  = 10
        data = response.json()
        self.assertLess(len(data), max_numb_of_players_per_team/2)
