SUBDIRS = sysctl

cirdanconf_DATA = cirdan
cirdanconfdir = $(sysconfdir)

CLEANFILES = $(cirdanconf_DATA)
EXTRA_DIST = cirdan.in

cirdan: cirdan.in Makefile
	$(SED) \
		-e 's%[@]localstatedir[@]%$(localstatedir)%g' \
		-e 's%[@]CIRDAN_USER[@]%$(CIRDAN_USER)%g' \
		< "$<" > "$@"
