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

import re

class Lond(object):
    """
    Lond(name) -> Lond object
    """

    # Constructor
    #############

    def __init__(self, name):
        """
        Constructor method.
        The name of the lond is treated as an ASCII string and has to match the
        pattern '^[a-zA-Z]\w*$'.
        """

        # Name of the lond
        if re.match('^[a-zA-Z]\w*$', str(name), re.ASCII):
            self.__name = str(name)
        else:
            raise ValueError(
                    "name '{}' does not match '^[a-zA-Z]\w*$'".format(
                        str(name)
                        )
                    )

    # Properties
    ############

    name = property(
            lambda self: self.__name,
            doc="Read only attribute 'name'"
            )
