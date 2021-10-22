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


class Stat(object):
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
        "question_id": "int",
        "question__article__live": "bool",
        "question__article__slug": "str",
        "question__article__has_video_solution": "bool",
        "question__title": "str",
        "question__title_slug": "str",
        "question__hide": "bool",
        "total_acs": "int",
        "total_submitted": "int",
        "frontend_question_id": "int",
        "is_new_question": "bool",
    }

    attribute_map = {
        "question_id": "question_id",
        "question__article__live": "question__article__live",
        "question__article__slug": "question__article__slug",
        "question__article__has_video_solution": "question__article__has_video_solution",
        "question__title": "question__title",
        "question__title_slug": "question__title_slug",
        "question__hide": "question__hide",
        "total_acs": "total_acs",
        "total_submitted": "total_submitted",
        "frontend_question_id": "frontend_question_id",
        "is_new_question": "is_new_question",
    }

    def __init__(
        self,
        question_id=None,
        question__article__live=None,
        question__article__slug=None,
        question__article__has_video_solution=None,
        question__title=None,
        question__title_slug=None,
        question__hide=None,
        total_acs=None,
        total_submitted=None,
        frontend_question_id=None,
        is_new_question=None,
    ):  # noqa: E501
        """Stat - a model defined in Swagger"""  # noqa: E501
        self._question_id = None
        self._question__article__live = None
        self._question__article__slug = None
        self._question__article__has_video_solution = None
        self._question__title = None
        self._question__title_slug = None
        self._question__hide = None
        self._total_acs = None
        self._total_submitted = None
        self._frontend_question_id = None
        self._is_new_question = None
        self.discriminator = None
        self.question_id = question_id
        if question__article__live is not None:
            self.question__article__live = question__article__live
        if question__article__slug is not None:
            self.question__article__slug = question__article__slug
        if question__article__has_video_solution is not None:
            self.question__article__has_video_solution = (
                question__article__has_video_solution
            )
        self.question__title = question__title
        self.question__title_slug = question__title_slug
        self.question__hide = question__hide
        self.total_acs = total_acs
        self.total_submitted = total_submitted
        self.frontend_question_id = frontend_question_id
        self.is_new_question = is_new_question

    @property
    def question_id(self):
        """Gets the question_id of this Stat.  # noqa: E501


        :return: The question_id of this Stat.  # noqa: E501
        :rtype: int
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        """Sets the question_id of this Stat.


        :param question_id: The question_id of this Stat.  # noqa: E501
        :type: int
        """
        if question_id is None:
            raise ValueError(
                "Invalid value for `question_id`, must not be `None`"
            )  # noqa: E501

        self._question_id = question_id

    @property
    def question__article__live(self):
        """Gets the question__article__live of this Stat.  # noqa: E501


        :return: The question__article__live of this Stat.  # noqa: E501
        :rtype: bool
        """
        return self._question__article__live

    @question__article__live.setter
    def question__article__live(self, question__article__live):
        """Sets the question__article__live of this Stat.


        :param question__article__live: The question__article__live of this Stat.  # noqa: E501
        :type: bool
        """

        self._question__article__live = question__article__live

    @property
    def question__article__slug(self):
        """Gets the question__article__slug of this Stat.  # noqa: E501


        :return: The question__article__slug of this Stat.  # noqa: E501
        :rtype: str
        """
        return self._question__article__slug

    @question__article__slug.setter
    def question__article__slug(self, question__article__slug):
        """Sets the question__article__slug of this Stat.


        :param question__article__slug: The question__article__slug of this Stat.  # noqa: E501
        :type: str
        """

        self._question__article__slug = question__article__slug

    @property
    def question__article__has_video_solution(self):
        """Gets the question__article__has_video_solution of this Stat.  # noqa: E501


        :return: The question__article__has_video_solution of this Stat.  # noqa: E501
        :rtype: bool
        """
        return self._question__article__has_video_solution

    @question__article__has_video_solution.setter
    def question__article__has_video_solution(
        self, question__article__has_video_solution
    ):
        """Sets the question__article__has_video_solution of this Stat.


        :param question__article__has_video_solution: The question__article__has_video_solution of this Stat.  # noqa: E501
        :type: bool
        """

        self._question__article__has_video_solution = (
            question__article__has_video_solution
        )

    @property
    def question__title(self):
        """Gets the question__title of this Stat.  # noqa: E501


        :return: The question__title of this Stat.  # noqa: E501
        :rtype: str
        """
        return self._question__title

    @question__title.setter
    def question__title(self, question__title):
        """Sets the question__title of this Stat.


        :param question__title: The question__title of this Stat.  # noqa: E501
        :type: str
        """
        if question__title is None:
            raise ValueError(
                "Invalid value for `question__title`, must not be `None`"
            )  # noqa: E501

        self._question__title = question__title

    @property
    def question__title_slug(self):
        """Gets the question__title_slug of this Stat.  # noqa: E501


        :return: The question__title_slug of this Stat.  # noqa: E501
        :rtype: str
        """
        return self._question__title_slug

    @question__title_slug.setter
    def question__title_slug(self, question__title_slug):
        """Sets the question__title_slug of this Stat.


        :param question__title_slug: The question__title_slug of this Stat.  # noqa: E501
        :type: str
        """
        if question__title_slug is None:
            raise ValueError(
                "Invalid value for `question__title_slug`, must not be `None`"
            )  # noqa: E501

        self._question__title_slug = question__title_slug

    @property
    def question__hide(self):
        """Gets the question__hide of this Stat.  # noqa: E501


        :return: The question__hide of this Stat.  # noqa: E501
        :rtype: bool
        """
        return self._question__hide

    @question__hide.setter
    def question__hide(self, question__hide):
        """Sets the question__hide of this Stat.


        :param question__hide: The question__hide of this Stat.  # noqa: E501
        :type: bool
        """
        if question__hide is None:
            raise ValueError(
                "Invalid value for `question__hide`, must not be `None`"
            )  # noqa: E501

        self._question__hide = question__hide

    @property
    def total_acs(self):
        """Gets the total_acs of this Stat.  # noqa: E501


        :return: The total_acs of this Stat.  # noqa: E501
        :rtype: int
        """
        return self._total_acs

    @total_acs.setter
    def total_acs(self, total_acs):
        """Sets the total_acs of this Stat.


        :param total_acs: The total_acs of this Stat.  # noqa: E501
        :type: int
        """
        if total_acs is None:
            raise ValueError(
                "Invalid value for `total_acs`, must not be `None`"
            )  # noqa: E501

        self._total_acs = total_acs

    @property
    def total_submitted(self):
        """Gets the total_submitted of this Stat.  # noqa: E501


        :return: The total_submitted of this Stat.  # noqa: E501
        :rtype: int
        """
        return self._total_submitted

    @total_submitted.setter
    def total_submitted(self, total_submitted):
        """Sets the total_submitted of this Stat.


        :param total_submitted: The total_submitted of this Stat.  # noqa: E501
        :type: int
        """
        if total_submitted is None:
            raise ValueError(
                "Invalid value for `total_submitted`, must not be `None`"
            )  # noqa: E501

        self._total_submitted = total_submitted

    @property
    def frontend_question_id(self):
        """Gets the frontend_question_id of this Stat.  # noqa: E501


        :return: The frontend_question_id of this Stat.  # noqa: E501
        :rtype: int
        """
        return self._frontend_question_id

    @frontend_question_id.setter
    def frontend_question_id(self, frontend_question_id):
        """Sets the frontend_question_id of this Stat.


        :param frontend_question_id: The frontend_question_id of this Stat.  # noqa: E501
        :type: int
        """
        if frontend_question_id is None:
            raise ValueError(
                "Invalid value for `frontend_question_id`, must not be `None`"
            )  # noqa: E501

        self._frontend_question_id = frontend_question_id

    @property
    def is_new_question(self):
        """Gets the is_new_question of this Stat.  # noqa: E501


        :return: The is_new_question of this Stat.  # noqa: E501
        :rtype: bool
        """
        return self._is_new_question

    @is_new_question.setter
    def is_new_question(self, is_new_question):
        """Sets the is_new_question of this Stat.


        :param is_new_question: The is_new_question of this Stat.  # noqa: E501
        :type: bool
        """
        if is_new_question is None:
            raise ValueError(
                "Invalid value for `is_new_question`, must not be `None`"
            )  # noqa: E501

        self._is_new_question = is_new_question

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
        if issubclass(Stat, dict):
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
        if not isinstance(other, Stat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
