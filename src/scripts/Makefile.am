sbin_SCRIPTS = cirdan

CLEANFILES = $(sbin_SCRIPTS)
EXTRA_DIST = cirdan.in

cirdan: cirdan.in Makefile
	$(SED) \
		-e 's%[@]PYTHON[@]%$(PYTHON)%g' \
		< "$<" > "$@"
