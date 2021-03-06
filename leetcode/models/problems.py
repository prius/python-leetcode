# coding: utf-8

"""
    Leetcode API

    Leetcode API implementation.  # noqa: E501

    OpenAPI spec version: 1.0.1-1
    Contact: pv.safronov@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Problems(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "user_name": "str",
        "num_solved": "int",
        "num_total": "int",
        "ac_easy": "int",
        "ac_medium": "int",
        "ac_hard": "int",
        "stat_status_pairs": "list[StatStatusPair]",
        "frequency_high": "int",
        "frequency_mid": "int",
        "category_slug": "str",
    }

    attribute_map = {
        "user_name": "user_name",
        "num_solved": "num_solved",
        "num_total": "num_total",
        "ac_easy": "ac_easy",
        "ac_medium": "ac_medium",
        "ac_hard": "ac_hard",
        "stat_status_pairs": "stat_status_pairs",
        "frequency_high": "frequency_high",
        "frequency_mid": "frequency_mid",
        "category_slug": "category_slug",
    }

    def __init__(
        self,
        user_name=None,
        num_solved=None,
        num_total=None,
        ac_easy=None,
        ac_medium=None,
        ac_hard=None,
        stat_status_pairs=None,
        frequency_high=None,
        frequency_mid=None,
        category_slug=None,
    ):  # noqa: E501
        """Problems - a model defined in Swagger"""  # noqa: E501
        self._user_name = None
        self._num_solved = None
        self._num_total = None
        self._ac_easy = None
        self._ac_medium = None
        self._ac_hard = None
        self._stat_status_pairs = None
        self._frequency_high = None
        self._frequency_mid = None
        self._category_slug = None
        self.discriminator = None
        self.user_name = user_name
        self.num_solved = num_solved
        self.num_total = num_total
        self.ac_easy = ac_easy
        self.ac_medium = ac_medium
        self.ac_hard = ac_hard
        self.stat_status_pairs = stat_status_pairs
        self.frequency_high = frequency_high
        self.frequency_mid = frequency_mid
        self.category_slug = category_slug

    @property
    def user_name(self):
        """Gets the user_name of this Problems.  # noqa: E501


        :return: The user_name of this Problems.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this Problems.


        :param user_name: The user_name of this Problems.  # noqa: E501
        :type: str
        """
        if user_name is None:
            raise ValueError(
                "Invalid value for `user_name`, must not be `None`"
            )  # noqa: E501

        self._user_name = user_name

    @property
    def num_solved(self):
        """Gets the num_solved of this Problems.  # noqa: E501


        :return: The num_solved of this Problems.  # noqa: E501
        :rtype: int
        """
        return self._num_solved

    @num_solved.setter
    def num_solved(self, num_solved):
        """Sets the num_solved of this Problems.


        :param num_solved: The num_solved of this Problems.  # noqa: E501
        :type: int
        """
        if num_solved is None:
            raise ValueError(
                "Invalid value for `num_solved`, must not be `None`"
            )  # noqa: E501

        self._num_solved = num_solved

    @property
    def num_total(self):
        """Gets the num_total of this Problems.  # noqa: E501


        :return: The num_total of this Problems.  # noqa: E501
        :rtype: int
        """
        return self._num_total

    @num_total.setter
    def num_total(self, num_total):
        """Sets the num_total of this Problems.


        :param num_total: The num_total of this Problems.  # noqa: E501
        :type: int
        """
        if num_total is None:
            raise ValueError(
                "Invalid value for `num_total`, must not be `None`"
            )  # noqa: E501

        self._num_total = num_total

    @property
    def ac_easy(self):
        """Gets the ac_easy of this Problems.  # noqa: E501


        :return: The ac_easy of this Problems.  # noqa: E501
        :rtype: int
        """
        return self._ac_easy

    @ac_easy.setter
    def ac_easy(self, ac_easy):
        """Sets the ac_easy of this Problems.


        :param ac_easy: The ac_easy of this Problems.  # noqa: E501
        :type: int
        """
        if ac_easy is None:
            raise ValueError(
                "Invalid value for `ac_easy`, must not be `None`"
            )  # noqa: E501

        self._ac_easy = ac_easy

    @property
    def ac_medium(self):
        """Gets the ac_medium of this Problems.  # noqa: E501


        :return: The ac_medium of this Problems.  # noqa: E501
        :rtype: int
        """
        return self._ac_medium

    @ac_medium.setter
    def ac_medium(self, ac_medium):
        """Sets the ac_medium of this Problems.


        :param ac_medium: The ac_medium of this Problems.  # noqa: E501
        :type: int
        """
        if ac_medium is None:
            raise ValueError(
                "Invalid value for `ac_medium`, must not be `None`"
            )  # noqa: E501

        self._ac_medium = ac_medium

    @property
    def ac_hard(self):
        """Gets the ac_hard of this Problems.  # noqa: E501


        :return: The ac_hard of this Problems.  # noqa: E501
        :rtype: int
        """
        return self._ac_hard

    @ac_hard.setter
    def ac_hard(self, ac_hard):
        """Sets the ac_hard of this Problems.


        :param ac_hard: The ac_hard of this Problems.  # noqa: E501
        :type: int
        """
        if ac_hard is None:
            raise ValueError(
                "Invalid value for `ac_hard`, must not be `None`"
            )  # noqa: E501

        self._ac_hard = ac_hard

    @property
    def stat_status_pairs(self):
        """Gets the stat_status_pairs of this Problems.  # noqa: E501


        :return: The stat_status_pairs of this Problems.  # noqa: E501
        :rtype: list[StatStatusPair]
        """
        return self._stat_status_pairs

    @stat_status_pairs.setter
    def stat_status_pairs(self, stat_status_pairs):
        """Sets the stat_status_pairs of this Problems.


        :param stat_status_pairs: The stat_status_pairs of this Problems.  # noqa: E501
        :type: list[StatStatusPair]
        """
        if stat_status_pairs is None:
            raise ValueError(
                "Invalid value for `stat_status_pairs`, must not be `None`"
            )  # noqa: E501

        self._stat_status_pairs = stat_status_pairs

    @property
    def frequency_high(self):
        """Gets the frequency_high of this Problems.  # noqa: E501


        :return: The frequency_high of this Problems.  # noqa: E501
        :rtype: int
        """
        return self._frequency_high

    @frequency_high.setter
    def frequency_high(self, frequency_high):
        """Sets the frequency_high of this Problems.


        :param frequency_high: The frequency_high of this Problems.  # noqa: E501
        :type: int
        """
        if frequency_high is None:
            raise ValueError(
                "Invalid value for `frequency_high`, must not be `None`"
            )  # noqa: E501

        self._frequency_high = frequency_high

    @property
    def frequency_mid(self):
        """Gets the frequency_mid of this Problems.  # noqa: E501


        :return: The frequency_mid of this Problems.  # noqa: E501
        :rtype: int
        """
        return self._frequency_mid

    @frequency_mid.setter
    def frequency_mid(self, frequency_mid):
        """Sets the frequency_mid of this Problems.


        :param frequency_mid: The frequency_mid of this Problems.  # noqa: E501
        :type: int
        """
        if frequency_mid is None:
            raise ValueError(
                "Invalid value for `frequency_mid`, must not be `None`"
            )  # noqa: E501

        self._frequency_mid = frequency_mid

    @property
    def category_slug(self):
        """Gets the category_slug of this Problems.  # noqa: E501


        :return: The category_slug of this Problems.  # noqa: E501
        :rtype: str
        """
        return self._category_slug

    @category_slug.setter
    def category_slug(self, category_slug):
        """Sets the category_slug of this Problems.


        :param category_slug: The category_slug of this Problems.  # noqa: E501
        :type: str
        """
        if category_slug is None:
            raise ValueError(
                "Invalid value for `category_slug`, must not be `None`"
            )  # noqa: E501

        self._category_slug = category_slug

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(Problems, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Problems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
