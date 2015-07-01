all:
	$(PYTHON) setup.py build

clean:
	rm -rf build

install:
	$(PYTHON) setup.py install --prefix=$(prefix) --no-compile

uninstall:
	rm -f $(bindir)/cirdan
	test -d "$(CIRDAN_PKGPYTHON_PATH)" && rm -rf "$(CIRDAN_PKGPYTHON_PATH)"

noinst_DATA = \
  setup.py \
  cirdan/__init__.py

CLEANFILES = $(noinst_DATA)
EXTRA_DIST = \
  setup.py.in \
  cirdan/__init__.py.in \
  cirdan/entry_points.py \
  cirdan/lond.py

do_substitution = $(SED) -e 's%[@]CIRDAN_VERSION[@]%$(CIRDAN_VERSION)%g'

setup.py: setup.py.in Makefile
	$(do_substitution) < "$<" > "$@"

cirdan/__init__.py: cirdan/__init__.py.in Makefile
	$(do_substitution) < "$<" > "$@"
