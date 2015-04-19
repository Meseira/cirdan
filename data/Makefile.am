if ENABLE_BASH_COMPLETION
bashcompletiondir = $(BASH_COMPLETION_DIR)
dist_bashcompletion_DATA = cirdan
CLEANFILES = $(dist_bashcompletion_DATA)
EXTRA_DIST = cirdan.in

do_subst = sed -e 's%[@]PACKAGE[@]%$(PACKAGE)%g' \
	-e 's%[@]localstatedir[@]%$(localstatedir)%g'

cirdan: cirdan.in Makefile
	$(do_subst) < $(srcdir)/cirdan.in > cirdan
endif
