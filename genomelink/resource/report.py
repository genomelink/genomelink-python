import os
import requests
from requests_oauthlib import OAuth2Session
from genomelink import api_base
from genomelink.errors import GenomeLinkError


class Report(object):
    @staticmethod
    def fetch(name, population, token='', client_secret=''):
        if type(token) == str:
            token = {'token_type': 'Bearer', 'access_token': token}

        if token['access_token'].startswith('T_'):
            if not client_secret:
                client_secret = os.environ.get('GENOMELINK_CLIENT_SECRET')
                if not client_secret:
                    raise GenomeLinkError('GENOMELINK_CLIENT_SECRET is not provided.')

            path = '{}/v1/enterprise/reports/{name}/?population={population}'.format(api_base, name=name, population=population)
            response = requests.post(path,
                                     headers={'Authorization': 'Bearer {}'.format(client_secret)},
                                     data={'token': token['access_token']})
            if response.status_code != requests.codes.ok:
                raise GenomeLinkError('Invalid request.')

            record = [Report(report) for report in response.json()['reports']]

        else:
            path = '{}/v1/reports/{name}/?population={population}'.format(api_base, name=name, population=population)
            session = OAuth2Session(token=token)
            response = session.get(path)
            record = Report(response.json())

        return record

    def __init__(self, data):
        self._data = data

    @property
    def phenotype(self):
        return self._data['phenotype']

    @property
    def population(self):
        return self._data['population']

    @property
    def scores(self):
        return self._data['scores']

    @property
    def summary(self):
        return self._data['summary']
