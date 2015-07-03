noinst_DATA = \
  setup.py \
  cirdan/__init__.py

CLEANFILES = $(noinst_DATA)
EXTRA_DIST = \
  setup.py.in \
  cirdan/__init__.py.in \
  cirdan/cirdan_error.py \
  cirdan/config.py \
  cirdan/lond.py

all:
	$(PYTHON) setup.py build

clean:
	rm -rf build

install:
	$(PYTHON) setup.py install --prefix=$(prefix) --no-compile

uninstall:
	test -d "$(CIRDAN_PKGPYTHON_PATH)" && rm -rf "$(CIRDAN_PKGPYTHON_PATH)"

do_substitution = $(SED) -e 's%[@]CIRDAN_VERSION[@]%$(CIRDAN_VERSION)%g'

setup.py: setup.py.in Makefile
	$(do_substitution) < "$<" > "$@"

cirdan/__init__.py: cirdan/__init__.py.in Makefile
	$(do_substitution) < "$<" > "$@"
