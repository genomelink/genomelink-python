import os
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
from requests_oauthlib import OAuth2Session
from genomelink import api_base
from genomelink.errors import raise_oauth_error


class OAuth(object):
    @staticmethod
    def authorize_url(client_id='', scope=[], callback_url=''):
        if not client_id:
            client_id = os.environ['GENOMELINK_CLIENT_ID']
        if not callback_url:
            callback_url = os.environ['GENOMELINK_CALLBACK_URL']

        path = '{}/oauth/authorize'.format(api_base)
        session = OAuth2Session(client_id, scope=scope, redirect_uri=callback_url)
        url, state = session.authorization_url(path)
        return url

    @staticmethod
    def token(client_id='', client_secret='', callback_url='', request_url=''):
        if not client_id:
            client_id = os.environ['GENOMELINK_CLIENT_ID']
        if not client_secret:
            client_secret = os.environ['GENOMELINK_CLIENT_SECRET']
        if not callback_url:
            callback_url = os.environ['GENOMELINK_CALLBACK_URL']

        query = urlparse.parse_qs(urlparse.urlparse(request_url).query)
        error = query.get('error')
        if error:
            error_code = error[0]
            raise_oauth_error(error_code)

        path = '{}/oauth/token'.format(api_base)
        session = OAuth2Session(client_id, redirect_uri=callback_url)
        token = session.fetch_token(path,
                                    client_secret=client_secret,
                                    authorization_response=request_url)
        return token
