bin_SCRIPTS = cirdan

CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = cirdan.in

cirdan: cirdan.in Makefile
	$(SED) \
		-e 's%[@]PYTHON[@]%$(PYTHON)%g' \
		< "$<" > "$@"
