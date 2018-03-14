import os
import unittest
try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock
try:
    from urllib.parse import urlparse, parse_qs
except ImportError:
    from urlparse import urlparse, parse_qs
import genomelink


class OAuthTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(OAuthTestCase, cls).setUpClass()
        os.environ['GENOMELINK_CLIENT_ID'] = 'GENOMELINK_CLIENT_ID'
        os.environ['GENOMELINK_CLIENT_SECRET'] = 'GENOMELINK_CLIENT_SECRET'
        os.environ['GENOMELINK_CALLBACK_URL'] = 'https://localhost:5000/callback'

    @classmethod
    def tearDownClass(cls):
        super(OAuthTestCase, cls).tearDownClass()

    def test_authorize_url(self):
        authorize_url = genomelink.OAuth.authorize_url(scope=['report:eye-color report:beard-thickness report:morning-person'])
        url = urlparse(authorize_url)
        query = parse_qs(url.query)

        self.assertEqual(url.scheme, 'https')
        self.assertEqual(url.netloc, 'genomelink.io')
        self.assertEqual(url.path, '/oauth/authorize')
        self.assertEqual(query['response_type'], ['code'])
        self.assertEqual(query['client_id'], [os.environ['GENOMELINK_CLIENT_ID']])
        self.assertEqual(query['redirect_uri'], [os.environ['GENOMELINK_CALLBACK_URL']])
        self.assertEqual(query['scope'], ['report:eye-color report:beard-thickness report:morning-person'])
        self.assertTrue(query.get('state'))

    @patch('requests.Session.post')
    def test_token(self, mock_post):
        mock_post.return_value = Mock(text='''
        {
          "access_token":"MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
          "token_type":"bearer",
          "expires_in":3600,
          "refresh_token":"IwOGYzYTlmM2YxOTQ5MGE3YmNmMDFkNTVk",
          "scope":"report:eye-color report:beard-thickness report:morning-person",
          "state":"12345678"
        }
        ''')

        token = genomelink.OAuth.token(request_url='https://localhost:5000/callback?code=xxx')
        self.assertEqual(token['access_token'], 'MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3')
