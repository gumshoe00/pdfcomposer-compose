import pathlib
import unittest


from unittest.mock import patch
from io import StringIO

from pdfcomposer_compose import main

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

    def test_compose(self):
        _dir = pathlib.Path(__file__).parent.joinpath('mockdata')
        _outfile = pathlib.Path(str(_dir.joinpath('output.pdf')))
        if _outfile.exists():
            _outfile.unlink()

        main(*[str(_dir.joinpath('output.pdf')), str(_dir.joinpath('infile1.pdf')), str(_dir.joinpath('infile1.pdf'))])

        actual = pathlib.Path(str(_dir.joinpath('output.pdf'))).exists()
        expected = True

        self.assertEqual(actual, expected)
