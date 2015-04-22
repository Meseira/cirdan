AC_INIT([cirdan], [0.1.3], [gendre.reivax@gmail.com])

AC_CONFIG_MACRO_DIRS([m4])

AM_INIT_AUTOMAKE

AC_PROG_GREP
AC_PROG_SED

AX_LXC_VERSION([1.0.7], [], [AC_MSG_ERROR([cirdan needs at least LXC 1.0.7])])

AC_ARG_WITH([bash-completion],
            [AS_HELP_STRING([--with-bash-completion],
                            [install the bash auto-completion script @<:@default=yes@:>@])],
            [], [with_bash_completion=yes])
AS_IF([test "x$with_bash_completion" = "xyes"], [
        PKG_CHECK_MODULES([BASH_COMPLETION],
                          [bash-completion >= 2.0],
                          [BASH_COMPLETION_DIR="`pkg-config --variable=completionsdir bash-completion`"],
                          [AC_MSG_ERROR([can not find bash-completion module])])
      ], [
        BASH_COMPLETION_DIR="$with_bash_completion"
      ])
AC_SUBST([BASH_COMPLETION_DIR])
AM_CONDITIONAL([ENABLE_BASH_COMPLETION],[test "x$with_bash_completion_dir" != "xno"])

AC_CONFIG_FILES([
  Makefile
  conf/Makefile
  data/Makefile
  m4/Makefile
  src/Makefile
])

AC_OUTPUT
