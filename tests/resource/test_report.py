import unittest
import genomelink


class ReportTestCase(unittest.TestCase):
    def test_token(self):
        report = genomelink.Report.fetch(name='eye-color', population='european', token='GENOMELINKTEST001')
        self.assertEqual(report.phenotype['url_name'], 'eye-color')
        self.assertEqual(report.population, 'european')
        self.assertEqual(report.summary['text'], 'Tend to not have brown eyes')
