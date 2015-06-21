# Process this file with autoconf to produce a configure script.

# Cirdan version
m4_define([cirdan_version_major], 0)
m4_define([cirdan_version_minor], 2)
m4_define([cirdan_version_micro], 0)
m4_define([cirdan_version_beta], [unstable])

m4_define([cirdan_version_base], [cirdan_version_major.cirdan_version_minor.cirdan_version_micro])
m4_define([cirdan_version], [ifelse(cirdan_version_beta, [], [cirdan_version_base], [cirdan_version_base-cirdan_version_beta])])

AC_INIT([cirdan], [cirdan_version], [gendre.reivax@gmail.com])

# Create output variables
AC_SUBST([CIRDAN_VERSION], [cirdan_version])
AC_SUBST([CIRDAN_VERSION_BASE], [cirdan_version_base])
AC_SUBST([CIRDAN_VERSION_BETA], [cirdan_version_beta])
AC_SUBST([CIRDAN_VERSION_MAJOR], [cirdan_version_major])
AC_SUBST([CIRDAN_VERSION_MINOR], [cirdan_version_minor])
AC_SUBST([CIRDAN_VERSION_MICRO], [cirdan_version_micro])

AC_CONFIG_SRCDIR([configure.ac])
AM_INIT_AUTOMAKE

# Check for some standard binaries
AC_PROG_GREP
AC_PROG_SED

# Check for Python3 interpreter
AM_PATH_PYTHON([3.2], [], [AC_MSG_ERROR([cannot find python3 >= 3.2])])

# Makefiles
AC_CONFIG_FILES([
  Makefile
  src/Makefile
  src/python/Makefile
])

# Files requiring some variable expansion
AC_CONFIG_FILES([
  src/python/setup.py
  src/python/cirdan/__init__.py
])

AC_OUTPUT
