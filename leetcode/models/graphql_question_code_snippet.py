# coding: utf-8

"""
    Leetcode API

    Leetcode API implementation.  # noqa: E501

    OpenAPI spec version: 1.0.1-1
    Contact: pv.safronov@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
from __future__ import annotations

import pprint
import re  # noqa: F401

import six


class GraphqlQuestionCodeSnippet(object):
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
        "lang": "str",
        "lang_slug": "str",
        "code": "str",
        "typename": "str",
    }

    attribute_map = {
        "lang": "lang",
        "lang_slug": "langSlug",
        "code": "code",
        "typename": "__typename",
    }

    def __init__(
        self, lang=None, lang_slug=None, code=None, typename=None
    ) -> None:  # noqa: E501
        """GraphqlQuestionCodeSnippet - a model defined in Swagger"""  # noqa: E501
        self._lang = None
        self._lang_slug = None
        self._code = None
        self._typename = None
        self.discriminator = None
        self.lang = lang
        self.lang_slug = lang_slug
        self.code = code
        if typename is not None:
            self.typename = typename

    @property
    def lang(self):
        """Gets the lang of this GraphqlQuestionCodeSnippet.  # noqa: E501


        :return: The lang of this GraphqlQuestionCodeSnippet.  # noqa: E501
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this GraphqlQuestionCodeSnippet.


        :param lang: The lang of this GraphqlQuestionCodeSnippet.  # noqa: E501
        :type: str
        """
        if lang is None:
            raise ValueError(
                "Invalid value for `lang`, must not be `None`"
            )  # noqa: E501

        self._lang = lang

    @property
    def lang_slug(self):
        """Gets the lang_slug of this GraphqlQuestionCodeSnippet.  # noqa: E501


        :return: The lang_slug of this GraphqlQuestionCodeSnippet.  # noqa: E501
        :rtype: str
        """
        return self._lang_slug

    @lang_slug.setter
    def lang_slug(self, lang_slug):
        """Sets the lang_slug of this GraphqlQuestionCodeSnippet.


        :param lang_slug: The lang_slug of this GraphqlQuestionCodeSnippet.  # noqa: E501
        :type: str
        """
        if lang_slug is None:
            raise ValueError(
                "Invalid value for `lang_slug`, must not be `None`"
            )  # noqa: E501

        self._lang_slug = lang_slug

    @property
    def code(self):
        """Gets the code of this GraphqlQuestionCodeSnippet.  # noqa: E501


        :return: The code of this GraphqlQuestionCodeSnippet.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GraphqlQuestionCodeSnippet.


        :param code: The code of this GraphqlQuestionCodeSnippet.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError(
                "Invalid value for `code`, must not be `None`"
            )  # noqa: E501

        self._code = code

    @property
    def typename(self):
        """Gets the typename of this GraphqlQuestionCodeSnippet.  # noqa: E501


        :return: The typename of this GraphqlQuestionCodeSnippet.  # noqa: E501
        :rtype: str
        """
        return self._typename

    @typename.setter
    def typename(self, typename):
        """Sets the typename of this GraphqlQuestionCodeSnippet.


        :param typename: The typename of this GraphqlQuestionCodeSnippet.  # noqa: E501
        :type: str
        """

        self._typename = typename

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
        if issubclass(GraphqlQuestionCodeSnippet, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: GraphqlQuestionCodeSnippet) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GraphqlQuestionCodeSnippet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
