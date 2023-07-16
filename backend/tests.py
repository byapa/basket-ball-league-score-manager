import os

from django.core.management import call_command
from django.test import Client, TestCase


def _seed_data_from_fixtures():
    fixture_dir = "backend/fixtures"
    fixtures = [
        os.path.join(fixture_dir, file_name)
        for file_name in os.listdir(fixture_dir)
        if file_name.endswith(".json")
    ]
    call_command("loaddata", *fixtures)


class BackendTest(TestCase):
    def setUp(self):
        self.client = Client()
        _seed_data_from_fixtures()

    def test_top_players_view(self):
        top_players_response = self.client.get("/api/teams/1/top-players")
        self.assertEqual(top_players_response.status_code, 200)
        top_players = top_players_response.json()
        ninetieth_percentile_score = self._find_ninetieth_percentile_score_of_team_1()
        self.assertTrue(all(player['average_score'] >= ninetieth_percentile_score for player in top_players))

    def _find_ninetieth_percentile_score_of_team_1(self):
        team1_response = self.client.get("/api/teams/1/")
        self.assertEqual(team1_response.status_code, 200)

        team1_players = team1_response.json()['players']

        self.assertEqual(len(team1_players), 10)
        avg_scores = list(
            map(lambda player: player['average_score'], team1_players)
        )
        avg_scores.sort()
        ninetieth_percentile_score = avg_scores[8]
        return ninetieth_percentile_score
