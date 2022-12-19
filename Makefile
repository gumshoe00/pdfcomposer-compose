NAME = pdfcomposer-compose

LIB = `python -c 'print("${NAME}".replace("-", "_"))' `

all:
	@echo "$(NAME)"
	@echo "$(LIB)"

install:
	@echo `pip install -e .`

build:
	@echo `python -m build`

topypi:
	@echo `twine check dist/*`
	@echo `twine upload dist/*`

cleanup:
	@if [ -d dist ]; then rm -r dist ;fi
	@if [ -d .idea ]; then rm -r .idea ;fi
	@if [ -d .DS_Store ]; then rm -r .DS_Store ;fi
	@if [ -d __pycache__ ]; then rm -r __pycache__ ;fi
	@if [ -d src/${NAME}/${LIB}.egg-info ]; then rm -r src/${NAME}/${LIB}.egg-info ;fi
	@if [ -d src/${NAME}/.DS_Store ]; then rm -r src/${NAME}/.DS_Store ;fi
	@if [ -d src/${NAME}/__pycache__ ]; then rm -r src/${NAME}/__pycache__ ;fi
	@if [ -d tests/__pycache__ ]; then rm -r tests/__pycache__ ;fi


.PHONEY: all cleanup
