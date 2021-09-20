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

class GraphqlQueryVariables(object):
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
        'title_slug': 'str'
    }

    attribute_map = {
        'title_slug': 'titleSlug'
    }

    def __init__(self, title_slug=None):  # noqa: E501
        """GraphqlQueryVariables - a model defined in Swagger"""  # noqa: E501
        self._title_slug = None
        self.discriminator = None
        self.title_slug = title_slug

    @property
    def title_slug(self):
        """Gets the title_slug of this GraphqlQueryVariables.  # noqa: E501


        :return: The title_slug of this GraphqlQueryVariables.  # noqa: E501
        :rtype: str
        """
        return self._title_slug

    @title_slug.setter
    def title_slug(self, title_slug):
        """Sets the title_slug of this GraphqlQueryVariables.


        :param title_slug: The title_slug of this GraphqlQueryVariables.  # noqa: E501
        :type: str
        """
        if title_slug is None:
            raise ValueError("Invalid value for `title_slug`, must not be `None`")  # noqa: E501

        self._title_slug = title_slug

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
        if issubclass(GraphqlQueryVariables, dict):
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
        if not isinstance(other, GraphqlQueryVariables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
