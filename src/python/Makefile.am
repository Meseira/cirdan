if DISTRO_DEBIAN
  SETUP_OPTS=--install-layout=deb
else
  SETUP_OPTS=
endif

all:
	$(PYTHON) setup.py build

clean:
	rm -rf build

install:
	$(PYTHON) setup.py install --prefix=$(prefix) --no-compile $(SETUP_OPTS)

uninstall:
	rm -f $(bindir)/cirdan

EXTRA_DIST = \
  cirdan/entry_points.py
