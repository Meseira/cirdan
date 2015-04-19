# SYNOPSIS
#
#   AX_LXC_VERSION([VERSION], [ACTION-IF-TRUE], [ACTION-IF-FALSE])
#
# DESCRIPTION
#
#   Makes sure that LXC supports the version indicated. If true the shell
#   commands in ACTION-IF-TRUE are executed. If not the shell commands in
#   ACTION-IF-FALSE are run. Note if lxc-info application can not be found,
#   the macro will fail. The $LXC_VERSION variable will be valorized with the
#   detected version.
#
#   Example:
#
#     AX_LXC_VERSION([1.0.7], [ ... ], [ ... ])
#
# LICENSE
#
#   Copyright (c) 2015 Xavier Gendre <gendre.reivax@gmail.com>
#
#   Copying and distribution of this file, with or without modification, are
#   permitted in any medium without royalty provided the copyright notice
#   and this notice are preserved. This file is offered as-is, without any
#   warranty.

# serial 1

AC_DEFUN([AX_LXC_VERSION], [
  AC_REQUIRE([AC_PROG_SED])
  AC_REQUIRE([AX_PROG_LXC_INFO])

  AS_IF([test "x$LXC_INFO" != "xno"], [
    ax_lxc_version="$1"

    AC_MSG_CHECKING([for LXC version])
    changequote(<<,>>)
    lxc_version=`$LXC_INFO --version | $SED -e 's/^.* \([0-9]*\.[0-9]*\.[0-9]*\) .*/\1/'`
    changequote([,])
    AC_MSG_RESULT($lxc_version)

    AC_SUBST([LXC_VERSION], [$lxc_version])

    AX_COMPARE_VERSION([$ax_lxc_version], [le], [$lxc_version],[
      :
      $2
    ],[
      :
      $3
    ])
  ], [
    AC_MSG_WARN([can not get the LXC version])
    $3
  ])
])
