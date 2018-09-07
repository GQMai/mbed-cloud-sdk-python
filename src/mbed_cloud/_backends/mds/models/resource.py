# coding: utf-8

"""
    Connect API

    Pelion Device Management Connect API allows web applications to communicate with devices. You can subscribe to device resources and read/write values to them. Device Management Connect allows connectivity to devices by queueing requests and caching resource values.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Resource(object):
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
        'obs': 'bool',
        'rt': 'str',
        'type': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'obs': 'obs',
        'rt': 'rt',
        'type': 'type',
        'uri': 'uri'
    }

    def __init__(self, obs=None, rt=None, type=None, uri=None):
        """
        Resource - a model defined in Swagger
        """

        self._obs = obs
        self._rt = rt
        self._type = type
        self._uri = uri
        self.discriminator = None

    @property
    def obs(self):
        """
        Gets the obs of this Resource.
        Observable determines whether you can subscribe to changes for this resource. It can have values \"true\" or \"false\". 

        :return: The obs of this Resource.
        :rtype: bool
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """
        Sets the obs of this Resource.
        Observable determines whether you can subscribe to changes for this resource. It can have values \"true\" or \"false\". 

        :param obs: The obs of this Resource.
        :type: bool
        """

        self._obs = obs

    @property
    def rt(self):
        """
        Gets the rt of this Resource.
        Application specific resource type that describes this resource. [It is created by the client side application](/docs/current/connecting/resource-setup-in-mbed-cloud-client.html). Not meant to be a human-readable name for the resource. Multiple resource types may be included, they are separated by a space.

        :return: The rt of this Resource.
        :rtype: str
        """
        return self._rt

    @rt.setter
    def rt(self, rt):
        """
        Sets the rt of this Resource.
        Application specific resource type that describes this resource. [It is created by the client side application](/docs/current/connecting/resource-setup-in-mbed-cloud-client.html). Not meant to be a human-readable name for the resource. Multiple resource types may be included, they are separated by a space.

        :param rt: The rt of this Resource.
        :type: str
        """

        self._rt = rt

    @property
    def type(self):
        """
        Gets the type of this Resource.
        The content type of the resource. <br/><br/><b>Important</b><br/> You are encouraged to use the resource types listed in the [LwM2M specification](http://technical.openmobilealliance.org/Technical/technical-information/omna/lightweight-m2m-lwm2m-object-registry). 

        :return: The type of this Resource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Resource.
        The content type of the resource. <br/><br/><b>Important</b><br/> You are encouraged to use the resource types listed in the [LwM2M specification](http://technical.openmobilealliance.org/Technical/technical-information/omna/lightweight-m2m-lwm2m-object-registry). 

        :param type: The type of this Resource.
        :type: str
        """

        self._type = type

    @property
    def uri(self):
        """
        Gets the uri of this Resource.
        The URL of the resource.

        :return: The uri of this Resource.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Resource.
        The URL of the resource.

        :param uri: The uri of this Resource.
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")

        self._uri = uri

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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
