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

"""Lond class definition."""

import lxc
import os.path
import re

class Lond(object):
    """
    Lond(name, lxc_path) -> Lond object
    """

    # Constructor
    #############

    def __init__(self, name, lxc_path):
        """
        Constructor method.
        The name of the lond is treated as an ASCII string and has to match the
        pattern '^[a-zA-Z]\w*$'. Argument 'lxc_path' refers to the directory
        where LXC containers are stored.
        """

        # Name of the lond
        if re.match('^[a-zA-Z]\w*$', str(name), re.ASCII):
            self.__name = str(name)
        else:
            raise ValueError(
                    "name '{}' does not match '^[a-zA-Z]\w*$'".format(name)
                    )

        if not os.path.isdir(lxc_path):
            raise ValueError("path '{}' does not exist".format(lxc_path))

        # LXC container
        self.__lxc_container = lxc.Container(self.__name, str(lxc_path))

    # Properties
    ############

    name = property(
            lambda self: self.__name,
            doc="Read only attribute 'name'"
            )
