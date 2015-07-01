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

"""IdMap class definition and utilities."""

class IdRangeMap(object):
    """
    IdRangeMap(first, count[, target]) -> IdRangeMap object
    """

    # Constructor
    #############

    def __init__(self, first, count, target=None):
        """
        Constructor method.
        Map a range of 'count' consecutive ids starting at 'first' to a range
        of 'count' consecutive ids starting at 'target'. Arguments 'first' and
        'target' are non negative integers and 'count' is a positive integer.
        If 'target' is unspecified or 'None', the range is stored but not
        mapped.
        """

        if not isinstance(first, int):
            raise TypeError(
                    "{}() argument 'first' must be an integer, "
                    "not {}".format(
                        self.__class__.__name__,
                        first.__class__.__name__
                        )
                    )

        if first < 0:
            raise ValueError(
                    "{}() argument 'first' must be a non negative integer: "
                    "{}".format(self.__class__.__name__, first)
                    )

        if not isinstance(count, int):
            raise TypeError(
                    "{}() argument 'count' must be an integer, "
                    "not {}".format(
                        self.__class__.__name__,
                        count.__class__.__name__
                        )
                    )

        if count < 1:
            raise ValueError(
                    "{}() argument 'count' must be a positive integer: "
                    "{}".format(self.__class__.__name__, count)
                    )

        if not (target is None or isinstance(target, int)):
            raise TypeError(
                    "{}() argument 'target' must be None or an integer, "
                    "not {}".format(
                        self.__class__.__name__,
                        target.__class__.__name__
                        )
                    )

        if isinstance(target, int) and target < 0:
            raise ValueError(
                    "{}() argument 'target' must be a non negative integer: "
                    "{}".format(self.__class__.__name__, target)
                    )

        # First id to map
        self.__first = first

        # Number of ids to map
        self.__count = count

        # First target id
        self.__target = target

    # Special methods
    #################

    def __contains__(self, item):
        """Return True if item is an id in the range, False otherwise."""

        if isinstance(item, int):
            return self.__first <= item and item < self.__first + self.__count
        else:
            return False

    def __getitem__(self, key):
        """
        Return self[key].
        Returned value is the id corresponding to id 'key' or None if 'key' is
        in the range but not mapped. If 'key' is not in the range, an exception
        'KeyError' is raised.
        """

        if not isinstance(key, int):
            raise TypeError(
                    "key must be an integer, not {}".format(
                        key.__class__.__name__
                        )
                    )

        if self.__first <= key and key < self.__first + self.__count:
            if not self.__target is None:
                return self.__target + key - self.__first
            else:
                return None
        else:
            raise KeyError("{} is out of range".format(key))

    def __len__(self):
        """Return len(self)."""

        return self.__count

class IdMap(object):
    """
    IdMap() -> IdMap object
    """

    # Constructor
    #############

    def __init__(self):
        """"Constructor method."""

        # Pool of id ranges
        self.__id_pool = []

    # Special methods
    #################

    def __contains__(self, item):
        """Return True if item is an id in the map, False otherwise."""

        for id_range in self.__id_pool:
            if item in id_range:
                return True
        return False

    def __getitem__(self, key):
        """
        Return self[key].
        Returned value is the id corresponding to id 'key' or None if 'key' is
        in the pool but not mapped. If 'key' is not in the map, an exception
        'KeyError' is raised.
        """

        if not isinstance(key, int):
            raise TypeError(
                    "key must be an integer, not {}".format(
                        key.__class__.__name__
                        )
                    )

        # Browse the id ranges
        for id_range in self.__id_pool:
            if key in id_range:
                return id_range[key]

        # At this point, key is not found in the id ranges
        raise KeyError("{} is not in the map".format(key))

    def __len__(self):
        """Return len(self)."""

        id_number = 0
        for id_range in self.__id_pool:
            id_number += len(id_range)

        return id_number

    # Public methods
    ################

    def append_id_range(self, first, count, target=None):
        """
        Append a range of 'count' ids starting at 'first' to the pool. This
        range is mapped to a range of 'count' ids starting at 'target'. The
        arguments 'first' and 'target' must be non negative integers and
        'count' must be a positive integer.
        """

        self.__id_pool.append(IdRangeMap(first, count, target))
