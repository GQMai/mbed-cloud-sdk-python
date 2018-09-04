# coding: utf-8

"""
    billing REST API documentation

    This document contains the public REST API definitions of the mbed-billing service.

    OpenAPI spec version: 1.4.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BadRequestErrorResponseField(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'message': 'str',
        'name': 'str'
    }

    attribute_map = {
        'message': 'message',
        'name': 'name'
    }

    def __init__(self, message=None, name=None):
        """
        BadRequestErrorResponseField - a model defined in Swagger
        """

        self._message = message
        self._name = name
        self.discriminator = None

    @property
    def message(self):
        """
        Gets the message of this BadRequestErrorResponseField.
        A human readable message with detailed validation error.

        :return: The message of this BadRequestErrorResponseField.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this BadRequestErrorResponseField.
        A human readable message with detailed validation error.

        :param message: The message of this BadRequestErrorResponseField.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def name(self):
        """
        Gets the name of this BadRequestErrorResponseField.
        Name of the field that failed the validation. If name is set to \"body\" then the validation failed on request body.

        :return: The name of this BadRequestErrorResponseField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BadRequestErrorResponseField.
        Name of the field that failed the validation. If name is set to \"body\" then the validation failed on request body.

        :param name: The name of this BadRequestErrorResponseField.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, BadRequestErrorResponseField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
