SUBDIRS = conf m4 src

EXTRA_DIST = autogen.sh

install-exec-hook:
	useradd --comment Cirdan --home-dir $(localstatedir)/lib/cirdan --system --shell /bin/bash cirdan
	mkdir $(localstatedir)/lib/cirdan
	chown cirdan:cirdan $(localstatedir)/lib/cirdan

uninstall-hook:
	userdel --remove cirdan
