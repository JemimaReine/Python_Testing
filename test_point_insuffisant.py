import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from server import app  # Remplacez 'your_flask_app' par le nom de votre fichier d'application Flask

class TestPurchasePlacesInsufficientPoints(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_purchasePlaces_insufficient_points(self):
        response = self.client.post('/purchasePlaces', data={'competition': 'Fall Classic', 'club': 'Simply Lift', 'places': '13'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('welcome.html')

if __name__ == '_main_':
    unittest.main()