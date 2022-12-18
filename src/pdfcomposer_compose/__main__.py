import pathlib

from builtins import str, print

from pdfrw import PdfReader, PdfWriter, IndirectPdfDict


def main(*files, **info):
    """Composes one PDF from the given pdf files, in the given sequence,
    then writes it to the given outfile path.

    Example:
    >>> main(*['outfile.pdf', 'infile1.pdf', 'infile2.pdf'],
    ...         **{'title': 'My PDF', 'author': 'Joe', 'subject': 'About my PDF', 'creator': 'Joe'})


    :param files:
        - outfile = files[0]
            The full path and name of the output pdf file.
            If the name does not end with `.pdf`, it will be added.
        - infiles = files[1:]
            List the full path of each file,
            in the same sequence it will be added to the composed PDF.

    :return: None

    """

    files = [_fl for _fl in files]

    if not len(files) > 0:
        print('The PDF was **not** created because no outfile was given.')
        return ''

    outfile = pathlib.Path(files.pop(0))

    if not len(files) > 0:
        print('The PDF was **not** created because no PDF files were given.')
        return ''

    sani_outfile_stem = ''.join([_char for _char in outfile.stem if _char.isalnum()])
    sani_outfile_name = outfile.name.replace(outfile.stem, sani_outfile_stem)
    if not sani_outfile_name.endswith('.pdf'):
        sani_outfile_name = f"{sani_outfile_name}.pdf"

    outfile = outfile.parent.joinpath(sani_outfile_name)
    writer = PdfWriter()
    for file in files:
        _pdf = PdfReader(file)
        writer.addpages(_pdf.pages)

    writer.trailer.Info = IndirectPdfDict(
        Title=info.get('title', pathlib.Path(outfile).stem),
        Author=info.get('author', pathlib.Path('~').expanduser().name),
        Subject=info.get('subject', pathlib.Path(outfile).stem),
        Creator=info.get('creator', pathlib.Path('~').expanduser().name),
    )
    writer.write(outfile)


