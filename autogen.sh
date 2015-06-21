#!/bin/sh
#
# Cirdan: create and manage LXC unprivileged containers
#
# Copyright (C) Xavier Gendre 2015
#
# This file is part of Cirdan.
#
# Cirdan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cirdan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cirdan. If not, see <http://www.gnu.org/licenses/>.

set -x

test -d autom4te.cache && rm -rf autom4te.cache

aclocal || exit 1
autoconf || exit 1
automake --add-missing --copy || exit 1