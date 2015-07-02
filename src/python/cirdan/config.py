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

"""Config class definition."""

import configparser

from cirdan.cirdan_error import CirdanError

class Config(object):
    """
    Config(config_file) -> Config object
    """

    # Constructor
    #############

    def __init__(self, config_file):
        """
        Constructor method.
        Initialize the configuration from 'config_file' which must be must be an
        iterable yielding Unicode strings.
        """

        # Initialize configuration
        self.__config = configparser.ConfigParser()
        self.__config.read_file(config_file)

        # Validate the content of the configuratiob
        if not self.__config.has_section('Cirdan'):
            raise CirdanError("no section 'Cirdan' in configuration file")
        if not self.__config.has_option('Cirdan', 'user'):
            raise CirdanError('no user defined in configuration file')
        if not self.__config.has_option('Cirdan', 'path'):
            raise CirdanError('no path defined in configuration file')

    # Properties
    ############

    user = property(
            lambda self: self.__config['Cirdan']['user'],
            doc='Cirdan user'
            )

    path = property(
            lambda self: self.__config['Cirdan']['path'],
            doc='Cirdan path'
            )
