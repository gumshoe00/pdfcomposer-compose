import unittest


from unittest.mock import patch
from io import StringIO


class TestPdfComposerCompose(unittest.TestCase):
    @patch('sys.stdin', StringIO('pdfcomposer --outputer compose --files ~/projects/pdf-composer/src/pdf-composer-infile/tests/mockdata/outfile.pdf ~/projects/pdf-composer/src/pdf-composer-infile/tests/mockdata/infile1.pdf'))
    @patch('sys.stdout', new_callable=StringIO)
    @patch('sys.stderr', new_callable=StringIO)
    def test_main(self, stderr, stdout):
        # Expect stderr
        err = ''

        # Expect stdout
        expected = ''

        # Check stdout and stderr
        self.assertEqual(stdout.getvalue(), expected)
        self.assertEqual(stderr.getvalue(), err)
