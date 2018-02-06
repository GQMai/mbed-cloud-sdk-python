# coding: utf-8

"""
    Account Management API

    API for managing accounts, users, creating API keys, uploading trusted certificates

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FeaturePolicy(object):
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
        'action': 'str',
        'resource': 'str',
        'feature': 'str',
        'allow': 'bool',
        'inherited': 'bool'
    }

    attribute_map = {
        'action': 'action',
        'resource': 'resource',
        'feature': 'feature',
        'allow': 'allow',
        'inherited': 'inherited'
    }

    def __init__(self, action=None, resource=None, feature=None, allow=None, inherited=None):
        """
        FeaturePolicy - a model defined in Swagger
        """

        self._action = action
        self._resource = resource
        self._feature = feature
        self._allow = allow
        self._inherited = inherited
        self.discriminator = None

    @property
    def action(self):
        """
        Gets the action of this FeaturePolicy.
        Comma separated list of actions, empty string represents all actions.

        :return: The action of this FeaturePolicy.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this FeaturePolicy.
        Comma separated list of actions, empty string represents all actions.

        :param action: The action of this FeaturePolicy.
        :type: str
        """

        self._action = action

    @property
    def resource(self):
        """
        Gets the resource of this FeaturePolicy.
        Resource that is protected by this policy.

        :return: The resource of this FeaturePolicy.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this FeaturePolicy.
        Resource that is protected by this policy.

        :param resource: The resource of this FeaturePolicy.
        :type: str
        """

        self._resource = resource

    @property
    def feature(self):
        """
        Gets the feature of this FeaturePolicy.
        Feature name corresponding to this policy.

        :return: The feature of this FeaturePolicy.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """
        Sets the feature of this FeaturePolicy.
        Feature name corresponding to this policy.

        :param feature: The feature of this FeaturePolicy.
        :type: str
        """

        self._feature = feature

    @property
    def allow(self):
        """
        Gets the allow of this FeaturePolicy.
        True or false controlling whether an action is allowed or not.

        :return: The allow of this FeaturePolicy.
        :rtype: bool
        """
        return self._allow

    @allow.setter
    def allow(self, allow):
        """
        Sets the allow of this FeaturePolicy.
        True or false controlling whether an action is allowed or not.

        :param allow: The allow of this FeaturePolicy.
        :type: bool
        """

        self._allow = allow

    @property
    def inherited(self):
        """
        Gets the inherited of this FeaturePolicy.
        Flag indicating whether this feature is inherited or overwritten specifically.

        :return: The inherited of this FeaturePolicy.
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """
        Sets the inherited of this FeaturePolicy.
        Flag indicating whether this feature is inherited or overwritten specifically.

        :param inherited: The inherited of this FeaturePolicy.
        :type: bool
        """

        self._inherited = inherited

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
        if not isinstance(other, FeaturePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
