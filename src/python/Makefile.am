all:
	$(PYTHON) setup.py build

clean:
	rm -rf build

install:
	$(PYTHON) setup.py install --prefix=$(prefix) --no-compile

uninstall:
	rm -f $(bindir)/cirdan
	test -d "$(CIRDAN_PKGPYTHON_PATH)" && rm -rf "$(CIRDAN_PKGPYTHON_PATH)"

EXTRA_DIST = \
  cirdan/entry_points.py \
  cirdan/id_map.py \
  cirdan/lond.py
