all:
	$(PYTHON) setup.py build

install:
	$(PYTHON) setup.py install --prefix=$(prefix) --no-compile

uninstall:
	echo "TEST: "$(PYTHON)
	echo "TEST: "$(PYTHON_VERSION)
	echo "TEST: "$(PYTHON_PREFIX)
	echo "TEST: "$(PYTHON_EXEC_PREFIX)
	echo "TEST: "$(PYTHON_PLATFORM)
	echo "TEST: "$(pythondir)
	echo "TEST: "$(pkgpythondir)
	echo "TEST: "$(pyexecdir)
	echo "TEST: "$(pkgpyexecdir)

EXTRA_DIST = \
  cirdan/entry_points.py
