sbin_SCRIPTS = cirdan
CLEANFILES = $(sbin_SCRIPTS)
EXTRA_DIST = cirdan.in

do_subst = sed -e 's%[@]PACKAGE[@]%$(PACKAGE)%g' \
	-e 's%[@]VERSION[@]%$(VERSION)%g' \
	-e 's%[@]localstatedir[@]%$(localstatedir)%g' \
	-e 's%[@]sysconfdir[@]%$(sysconfdir)%g'

cirdan: cirdan.in Makefile
	$(do_subst) < $(srcdir)/cirdan.in > cirdan
	chmod +x cirdan
