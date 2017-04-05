# coding: utf-8

"""
    Deployment Service API

    This is the API Documentation for the mbed deployment service which is part of the update service.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WriteUpdateCampaignPage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, limit=None, after=None, data=None, order=None):
        """
        WriteUpdateCampaignPage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'limit': 'int',
            'after': 'str',
            'data': 'list[UpdateCampaign]',
            'order': 'str'
        }

        self.attribute_map = {
            'limit': 'limit',
            'after': 'after',
            'data': 'data',
            'order': 'order'
        }

        self._limit = limit
        self._after = after
        self._data = data
        self._order = order

    @property
    def limit(self):
        """
        Gets the limit of this WriteUpdateCampaignPage.

        :return: The limit of this WriteUpdateCampaignPage.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this WriteUpdateCampaignPage.

        :param limit: The limit of this WriteUpdateCampaignPage.
        :type: int
        """

        self._limit = limit

    @property
    def after(self):
        """
        Gets the after of this WriteUpdateCampaignPage.

        :return: The after of this WriteUpdateCampaignPage.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this WriteUpdateCampaignPage.

        :param after: The after of this WriteUpdateCampaignPage.
        :type: str
        """

        self._after = after

    @property
    def data(self):
        """
        Gets the data of this WriteUpdateCampaignPage.

        :return: The data of this WriteUpdateCampaignPage.
        :rtype: list[UpdateCampaign]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this WriteUpdateCampaignPage.

        :param data: The data of this WriteUpdateCampaignPage.
        :type: list[UpdateCampaign]
        """

        self._data = data

    @property
    def order(self):
        """
        Gets the order of this WriteUpdateCampaignPage.

        :return: The order of this WriteUpdateCampaignPage.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this WriteUpdateCampaignPage.

        :param order: The order of this WriteUpdateCampaignPage.
        :type: str
        """

        self._order = order

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
        if not isinstance(other, WriteUpdateCampaignPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
