import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from server import app  

class TestPurchasePlacesExceedTicketLimit(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_purchasePlaces_exceed_ticket_limit(self):
        response = self.client.post('/purchasePlaces', data={'competition': 'Fall Classic', 'club': 'Simply Lift', 'places': '13'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('welcome.html')
        # self.assertIn(b"Vous ne pouvez pas réserver plus de 12 billets pour une compétition spécifique.",response.data)  # Vérifiez que le message d'erreur est dans la réponse

if __name__ == '__main__':
    unittest.main()
