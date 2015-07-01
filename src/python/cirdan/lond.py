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
import tempfile

from cirdan.cirdan_error import CirdanError

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

        # Subordinate user id range
        self.__user_id_first = None
        self.__user_id_count = None

        # Subordinate group id range
        self.__group_id_first = None
        self.__group_id_count = None

    # Public methods
    ################

    def create(self):
        """
        Create the lond or raise an exception if it has already been created.
        """

        if self.__lxc_container.defined:
            raise CirdanError("'{}' already exists".format(self.__name))

        if self.__user_id_first is None or self.__user_id_count is None:
            raise CirdanError("no subordinate user id range")

        if self.__group_id_first is None or self.__group_id_count is None:
            raise CirdanError("no subordinate group id range")

        # Set the configuration for LXC container
        with tempfile.NamedTemporaryFile() as f:
            f.write('lxc.network.type = empty\n'.encode())
            f.write('lxc.id_map = u 0 {} {}\n'.format(
                self.__user_id_first,
                self.__user_id_count).encode()
                )
            f.write('lxc.id_map = g 0 {} {}\n'.format(
                self.__group_id_first,
                self.__group_id_count).encode()
                )
            f.seek(0)

            if not self.__lxc_container.load_config(f.name):
                raise CirdanError('cannot load configuration')

        # Create LXC container
        self.__lxc_container.create('download')

    def set_group_id_range(self, first, count):
        """
        Give a range of 'count' subordinate group ids starting at id 'first' to
        the lond. The ownership of the subordinate ids is not checked, thus be
        sure to use a range that belongs to an appropriate group. While the lond
        remains uncreated, the range is stored but not mapped. If the lond has
        already been created, setting an new range is useless.
        """

        if not isinstance(first, int):
            raise TypeError("'first' must be an integer, not {}".format(
                        first.__class__.__name__
                        )
                    )

        if first < 0:
            raise ValueError(
                    "'first' must be a non negative integer: {}".format(first)
                    )

        if not isinstance(count, int):
            raise TypeError("'count' must be an integer, not {}".format(
                        count.__class__.__name__
                        )
                    )

        if count < 1:
            raise ValueError(
                    "'count' must be a positive integer: {}".format(count)
                    )

        self.__group_id_first = first
        self.__group_id_count = count

    def set_user_id_range(self, first, count):
        """
        Give a range of 'count' subordinate user ids starting at id 'first' to
        the lond. The ownership of the subordinate ids is not checked, thus be
        sure to use a range that belongs to an appropriate user. While the lond
        remains uncreated, the range is stored but not mapped. If the lond has
        already been created, setting an new range is useless.
        """

        if not isinstance(first, int):
            raise TypeError("'first' must be an integer, not {}".format(
                        first.__class__.__name__
                        )
                    )

        if first < 0:
            raise ValueError(
                    "'first' must be a non negative integer: {}".format(first)
                    )

        if not isinstance(count, int):
            raise TypeError("'count' must be an integer, not {}".format(
                        count.__class__.__name__
                        )
                    )

        if count < 1:
            raise ValueError(
                    "'count' must be a positive integer: {}".format(count)
                    )

        self.__user_id_first = first
        self.__user_id_count = count

    # Properties
    ############

    name = property(
            lambda self: self.__name,
            doc="Read only attribute 'name'"
            )
