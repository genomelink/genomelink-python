from requests_oauthlib import OAuth2Session
from genomelink import api_base


class Report(object):
    @staticmethod
    def fetch(name, population, token=''):
        path = '{}/v1/reports/{name}/?population={population}'.format(api_base, name=name, population=population)

        if type(token) == str:
            token = {'token_type': 'Bearer', 'access_token': token}

        session = OAuth2Session(token=token)
        response = session.get(path).json()
        return Report(response)

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
