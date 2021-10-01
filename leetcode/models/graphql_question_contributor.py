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

class GraphqlQuestionContributor(object):
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
        'username': 'str',
        'profile_url': 'str',
        'avatar_url': 'str',
        'typename': 'str'
    }

    attribute_map = {
        'username': 'username',
        'profile_url': 'profileUrl',
        'avatar_url': 'avatarUrl',
        'typename': '__typename'
    }

    def __init__(self, username=None, profile_url=None, avatar_url=None, typename=None):  # noqa: E501
        """GraphqlQuestionContributor - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._profile_url = None
        self._avatar_url = None
        self._typename = None
        self.discriminator = None
        self.username = username
        self.profile_url = profile_url
        self.avatar_url = avatar_url
        if typename is not None:
            self.typename = typename

    @property
    def username(self):
        """Gets the username of this GraphqlQuestionContributor.  # noqa: E501


        :return: The username of this GraphqlQuestionContributor.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GraphqlQuestionContributor.


        :param username: The username of this GraphqlQuestionContributor.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def profile_url(self):
        """Gets the profile_url of this GraphqlQuestionContributor.  # noqa: E501


        :return: The profile_url of this GraphqlQuestionContributor.  # noqa: E501
        :rtype: str
        """
        return self._profile_url

    @profile_url.setter
    def profile_url(self, profile_url):
        """Sets the profile_url of this GraphqlQuestionContributor.


        :param profile_url: The profile_url of this GraphqlQuestionContributor.  # noqa: E501
        :type: str
        """
        if profile_url is None:
            raise ValueError("Invalid value for `profile_url`, must not be `None`")  # noqa: E501

        self._profile_url = profile_url

    @property
    def avatar_url(self):
        """Gets the avatar_url of this GraphqlQuestionContributor.  # noqa: E501


        :return: The avatar_url of this GraphqlQuestionContributor.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this GraphqlQuestionContributor.


        :param avatar_url: The avatar_url of this GraphqlQuestionContributor.  # noqa: E501
        :type: str
        """
        if avatar_url is None:
            raise ValueError("Invalid value for `avatar_url`, must not be `None`")  # noqa: E501

        self._avatar_url = avatar_url

    @property
    def typename(self):
        """Gets the typename of this GraphqlQuestionContributor.  # noqa: E501


        :return: The typename of this GraphqlQuestionContributor.  # noqa: E501
        :rtype: str
        """
        return self._typename

    @typename.setter
    def typename(self, typename):
        """Sets the typename of this GraphqlQuestionContributor.


        :param typename: The typename of this GraphqlQuestionContributor.  # noqa: E501
        :type: str
        """

        self._typename = typename

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GraphqlQuestionContributor, dict):
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
        if not isinstance(other, GraphqlQuestionContributor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
