# coding: utf-8

"""
    Provisioning endpoints - production line certificates.

    A producton line certificate is used to associate a specific installation of the Factory Tool with an mbed Cloud account.  The production line certificate is generated by the Factory Tool, and needs to be uploaded using these APIs. 

    OpenAPI spec version: 0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AListOfProductionLineCertificates_(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, object=None, total_count=None, after=None, limit=None, data=None, order=None):
        """
        AListOfProductionLineCertificates_ - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'object': 'str',
            'total_count': 'int',
            'after': 'str',
            'limit': 'int',
            'data': 'list[ProductionLineCertificate]',
            'order': 'str'
        }

        self.attribute_map = {
            'object': 'object',
            'total_count': 'total_count',
            'after': 'after',
            'limit': 'limit',
            'data': 'data',
            'order': 'order'
        }

        self._object = object
        self._total_count = total_count
        self._after = after
        self._limit = limit
        self._data = data
        self._order = order

    @property
    def object(self):
        """
        Gets the object of this AListOfProductionLineCertificates_.
        \"list\"

        :return: The object of this AListOfProductionLineCertificates_.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this AListOfProductionLineCertificates_.
        \"list\"

        :param object: The object of this AListOfProductionLineCertificates_.
        :type: str
        """

        self._object = object

    @property
    def total_count(self):
        """
        Gets the total_count of this AListOfProductionLineCertificates_.
        Currently not used.

        :return: The total_count of this AListOfProductionLineCertificates_.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this AListOfProductionLineCertificates_.
        Currently not used.

        :param total_count: The total_count of this AListOfProductionLineCertificates_.
        :type: int
        """

        self._total_count = total_count

    @property
    def after(self):
        """
        Gets the after of this AListOfProductionLineCertificates_.
        Currently not used.

        :return: The after of this AListOfProductionLineCertificates_.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this AListOfProductionLineCertificates_.
        Currently not used.

        :param after: The after of this AListOfProductionLineCertificates_.
        :type: str
        """

        self._after = after

    @property
    def limit(self):
        """
        Gets the limit of this AListOfProductionLineCertificates_.
        Currently not used.

        :return: The limit of this AListOfProductionLineCertificates_.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this AListOfProductionLineCertificates_.
        Currently not used.

        :param limit: The limit of this AListOfProductionLineCertificates_.
        :type: int
        """

        self._limit = limit

    @property
    def data(self):
        """
        Gets the data of this AListOfProductionLineCertificates_.
        Production line certificates.

        :return: The data of this AListOfProductionLineCertificates_.
        :rtype: list[ProductionLineCertificate]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this AListOfProductionLineCertificates_.
        Production line certificates.

        :param data: The data of this AListOfProductionLineCertificates_.
        :type: list[ProductionLineCertificate]
        """

        self._data = data

    @property
    def order(self):
        """
        Gets the order of this AListOfProductionLineCertificates_.
        Currently not used.

        :return: The order of this AListOfProductionLineCertificates_.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this AListOfProductionLineCertificates_.
        Currently not used.

        :param order: The order of this AListOfProductionLineCertificates_.
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
        if not isinstance(other, AListOfProductionLineCertificates_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
