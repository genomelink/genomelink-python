# GENOME LINK Python SDK

Python client library to quickly get started with the GENOME LINK API

## Installation

To install, use `pip`:

```bash
pip install --upgrade genomelink
```

## Examples

```
>>> import genomelink
>>> report = genomelink.Report.fetch(name='eye-color', population='european', token='GENOMELINKTEST')
>>> report.summary['text']
Tend to not have brown eyes, slightly
```

* [Flask web app](https://github.com/AWAKENS-dev/api-oauth-example-flask)
* Django web app - coming soon

## Dependencies

* [requests](http://docs.python-requests.org/en/latest/)
* requests_oauthlib
