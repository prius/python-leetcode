# coding: utf-8

"""
    Simple Inventory API

    This is a simple API  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: pv.safronov@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Interpretation(object):
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
        'interpret_id': 'str',
        'test_case': 'str'
    }

    attribute_map = {
        'interpret_id': 'interpret_id',
        'test_case': 'test_case'
    }

    def __init__(self, interpret_id=None, test_case=None):  # noqa: E501
        """Interpretation - a model defined in Swagger"""  # noqa: E501
        self._interpret_id = None
        self._test_case = None
        self.discriminator = None
        self.interpret_id = interpret_id
        self.test_case = test_case

    @property
    def interpret_id(self):
        """Gets the interpret_id of this Interpretation.  # noqa: E501


        :return: The interpret_id of this Interpretation.  # noqa: E501
        :rtype: str
        """
        return self._interpret_id

    @interpret_id.setter
    def interpret_id(self, interpret_id):
        """Sets the interpret_id of this Interpretation.


        :param interpret_id: The interpret_id of this Interpretation.  # noqa: E501
        :type: str
        """
        if interpret_id is None:
            raise ValueError("Invalid value for `interpret_id`, must not be `None`")  # noqa: E501

        self._interpret_id = interpret_id

    @property
    def test_case(self):
        """Gets the test_case of this Interpretation.  # noqa: E501


        :return: The test_case of this Interpretation.  # noqa: E501
        :rtype: str
        """
        return self._test_case

    @test_case.setter
    def test_case(self, test_case):
        """Sets the test_case of this Interpretation.


        :param test_case: The test_case of this Interpretation.  # noqa: E501
        :type: str
        """
        if test_case is None:
            raise ValueError("Invalid value for `test_case`, must not be `None`")  # noqa: E501

        self._test_case = test_case

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
        if issubclass(Interpretation, dict):
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
        if not isinstance(other, Interpretation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
