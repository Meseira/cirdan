EXTRA_DIST = \
  cirdan.conf

if DISTRO_DEBIAN
install-exec-hook:
	echo "1" > /proc/sys/kernel/unprivileged_userns_clone

sysctldir = $(libdir)/sysctl.d
sysctl_DATA = cirdan.conf
endif
