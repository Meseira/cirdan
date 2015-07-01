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
AC_SUBST([CIRDAN_USER], [cirdan])
AC_SUBST([CIRDAN_GROUP], [cirdan])

AC_SUBST([CIRDAN_VERSION], [cirdan_version])
AC_SUBST([CIRDAN_VERSION_BASE], [cirdan_version_base])
AC_SUBST([CIRDAN_VERSION_BETA], [cirdan_version_beta])
AC_SUBST([CIRDAN_VERSION_MAJOR], [cirdan_version_major])
AC_SUBST([CIRDAN_VERSION_MINOR], [cirdan_version_minor])
AC_SUBST([CIRDAN_VERSION_MICRO], [cirdan_version_micro])

AC_CONFIG_MACRO_DIRS([m4])
AC_CONFIG_SRCDIR([configure.ac])
AM_INIT_AUTOMAKE

# Check for some standard binaries
AC_PROG_GREP
AC_PROG_SED

# Check for Python3 interpreter and modules
AM_PATH_PYTHON([3.2], [], [AC_MSG_ERROR([cannot find python3 >= 3.2])])
AX_PYTHON_MODULE([lxc], [yes], [python3])
AX_PYTHON_MODULE([setuptools], [yes], [python3])

# Check for lsb_release
AC_CHECK_PROG([have_lsb_release], [lsb_release], [yes], [no])
if test "x$have_lsb_release" != "xyes"; then
  AC_MSG_ERROR([cannot find lsb_release])
fi

# Detect the distribution to deal with distro specific options
AC_MSG_CHECKING([host distribution])
distro=`lsb_release -is | tr '[[:upper:]]' '[[:lower:]]'`
AC_MSG_RESULT([$distro])
case $distro in
  debian)
    ;;
  *)
    AC_MSG_ERROR([your host distribution is not yet supported])
    ;;
esac
AM_CONDITIONAL([DISTRO_DEBIAN], [test "x$distro" = "xdebian"])

# Python package 'cirdan' path
AM_COND_IF([DISTRO_DEBIAN],
  [pythondir_base=`echo $pythondir | sed s/site-packages/dist-packages/`],
  [pythondir_base=`echo $pythondir`]
)
egg_name=`echo $CIRDAN_VERSION | tr - _`-py`echo $PYTHON_VERSION`.egg
cirdan_pkgpython_path=$pythondir_base/cirdan-$egg_name
AC_SUBST([CIRDAN_PKGPYTHON_PATH], [$cirdan_pkgpython_path])

# Makefiles
AC_CONFIG_FILES([
  Makefile
  conf/Makefile
  conf/sysctl/Makefile
  m4/Makefile
  src/Makefile
  src/python/Makefile
  src/scripts/Makefile
])

AC_OUTPUT
