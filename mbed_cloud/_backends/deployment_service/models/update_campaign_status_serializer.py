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


class UpdateCampaignStatusSerializer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, direct_devices=None, connector_devices=None, description=None, state=None, updating_user_id=None, created_at=None, total_devices=None, campaigndevicemetadata_set=None, campaign_id=None, deployed_devices=None, updated_at=None, when=None, finished=None, root_manifest_url=None, updating_api_key=None, updating_account_id=None, device_filter=None, name=None):
        """
        UpdateCampaignStatusSerializer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'direct_devices': 'int',
            'connector_devices': 'int',
            'description': 'str',
            'state': 'str',
            'updating_user_id': 'str',
            'created_at': 'datetime',
            'total_devices': 'int',
            'campaigndevicemetadata_set': 'list[CampaignDeviceMetadataSerializer]',
            'campaign_id': 'str',
            'deployed_devices': 'int',
            'updated_at': 'datetime',
            'when': 'datetime',
            'finished': 'datetime',
            'root_manifest_url': 'str',
            'updating_api_key': 'str',
            'updating_account_id': 'str',
            'device_filter': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'direct_devices': 'direct_devices',
            'connector_devices': 'connector_devices',
            'description': 'description',
            'state': 'state',
            'updating_user_id': 'updating_user_id',
            'created_at': 'created_at',
            'total_devices': 'total_devices',
            'campaigndevicemetadata_set': 'campaigndevicemetadata_set',
            'campaign_id': 'campaign_id',
            'deployed_devices': 'deployed_devices',
            'updated_at': 'updated_at',
            'when': 'when',
            'finished': 'finished',
            'root_manifest_url': 'root_manifest_url',
            'updating_api_key': 'updating_api_key',
            'updating_account_id': 'updating_account_id',
            'device_filter': 'device_filter',
            'name': 'name'
        }

        self._direct_devices = direct_devices
        self._connector_devices = connector_devices
        self._description = description
        self._state = state
        self._updating_user_id = updating_user_id
        self._created_at = created_at
        self._total_devices = total_devices
        self._campaigndevicemetadata_set = campaigndevicemetadata_set
        self._campaign_id = campaign_id
        self._deployed_devices = deployed_devices
        self._updated_at = updated_at
        self._when = when
        self._finished = finished
        self._root_manifest_url = root_manifest_url
        self._updating_api_key = updating_api_key
        self._updating_account_id = updating_account_id
        self._device_filter = device_filter
        self._name = name

    @property
    def direct_devices(self):
        """
        Gets the direct_devices of this UpdateCampaignStatusSerializer.

        :return: The direct_devices of this UpdateCampaignStatusSerializer.
        :rtype: int
        """
        return self._direct_devices

    @direct_devices.setter
    def direct_devices(self, direct_devices):
        """
        Sets the direct_devices of this UpdateCampaignStatusSerializer.

        :param direct_devices: The direct_devices of this UpdateCampaignStatusSerializer.
        :type: int
        """
        if direct_devices is None:
            raise ValueError("Invalid value for `direct_devices`, must not be `None`")

        self._direct_devices = direct_devices

    @property
    def connector_devices(self):
        """
        Gets the connector_devices of this UpdateCampaignStatusSerializer.

        :return: The connector_devices of this UpdateCampaignStatusSerializer.
        :rtype: int
        """
        return self._connector_devices

    @connector_devices.setter
    def connector_devices(self, connector_devices):
        """
        Sets the connector_devices of this UpdateCampaignStatusSerializer.

        :param connector_devices: The connector_devices of this UpdateCampaignStatusSerializer.
        :type: int
        """
        if connector_devices is None:
            raise ValueError("Invalid value for `connector_devices`, must not be `None`")

        self._connector_devices = connector_devices

    @property
    def description(self):
        """
        Gets the description of this UpdateCampaignStatusSerializer.
        An optional description of the campaign

        :return: The description of this UpdateCampaignStatusSerializer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateCampaignStatusSerializer.
        An optional description of the campaign

        :param description: The description of this UpdateCampaignStatusSerializer.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def state(self):
        """
        Gets the state of this UpdateCampaignStatusSerializer.
        The state of the campaign

        :return: The state of this UpdateCampaignStatusSerializer.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this UpdateCampaignStatusSerializer.
        The state of the campaign

        :param state: The state of this UpdateCampaignStatusSerializer.
        :type: str
        """
        allowed_values = ["draft", "scheduled", "devicefetch", "devicecopy", "devicecopycomplete", "publishing", "deploying", "deployed", "manifestremoved", "expired"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def updating_user_id(self):
        """
        Gets the updating_user_id of this UpdateCampaignStatusSerializer.
        The updating IAM user ID

        :return: The updating_user_id of this UpdateCampaignStatusSerializer.
        :rtype: str
        """
        return self._updating_user_id

    @updating_user_id.setter
    def updating_user_id(self, updating_user_id):
        """
        Sets the updating_user_id of this UpdateCampaignStatusSerializer.
        The updating IAM user ID

        :param updating_user_id: The updating_user_id of this UpdateCampaignStatusSerializer.
        :type: str
        """
        if updating_user_id is None:
            raise ValueError("Invalid value for `updating_user_id`, must not be `None`")

        self._updating_user_id = updating_user_id

    @property
    def created_at(self):
        """
        Gets the created_at of this UpdateCampaignStatusSerializer.
        The time the object was created

        :return: The created_at of this UpdateCampaignStatusSerializer.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this UpdateCampaignStatusSerializer.
        The time the object was created

        :param created_at: The created_at of this UpdateCampaignStatusSerializer.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def total_devices(self):
        """
        Gets the total_devices of this UpdateCampaignStatusSerializer.

        :return: The total_devices of this UpdateCampaignStatusSerializer.
        :rtype: int
        """
        return self._total_devices

    @total_devices.setter
    def total_devices(self, total_devices):
        """
        Sets the total_devices of this UpdateCampaignStatusSerializer.

        :param total_devices: The total_devices of this UpdateCampaignStatusSerializer.
        :type: int
        """
        if total_devices is None:
            raise ValueError("Invalid value for `total_devices`, must not be `None`")

        self._total_devices = total_devices

    @property
    def campaigndevicemetadata_set(self):
        """
        Gets the campaigndevicemetadata_set of this UpdateCampaignStatusSerializer.

        :return: The campaigndevicemetadata_set of this UpdateCampaignStatusSerializer.
        :rtype: list[CampaignDeviceMetadataSerializer]
        """
        return self._campaigndevicemetadata_set

    @campaigndevicemetadata_set.setter
    def campaigndevicemetadata_set(self, campaigndevicemetadata_set):
        """
        Sets the campaigndevicemetadata_set of this UpdateCampaignStatusSerializer.

        :param campaigndevicemetadata_set: The campaigndevicemetadata_set of this UpdateCampaignStatusSerializer.
        :type: list[CampaignDeviceMetadataSerializer]
        """
        if campaigndevicemetadata_set is None:
            raise ValueError("Invalid value for `campaigndevicemetadata_set`, must not be `None`")

        self._campaigndevicemetadata_set = campaigndevicemetadata_set

    @property
    def campaign_id(self):
        """
        Gets the campaign_id of this UpdateCampaignStatusSerializer.
        DEPRECATED: The ID of the campaign

        :return: The campaign_id of this UpdateCampaignStatusSerializer.
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """
        Sets the campaign_id of this UpdateCampaignStatusSerializer.
        DEPRECATED: The ID of the campaign

        :param campaign_id: The campaign_id of this UpdateCampaignStatusSerializer.
        :type: str
        """
        if campaign_id is None:
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")

        self._campaign_id = campaign_id

    @property
    def deployed_devices(self):
        """
        Gets the deployed_devices of this UpdateCampaignStatusSerializer.

        :return: The deployed_devices of this UpdateCampaignStatusSerializer.
        :rtype: int
        """
        return self._deployed_devices

    @deployed_devices.setter
    def deployed_devices(self, deployed_devices):
        """
        Sets the deployed_devices of this UpdateCampaignStatusSerializer.

        :param deployed_devices: The deployed_devices of this UpdateCampaignStatusSerializer.
        :type: int
        """
        if deployed_devices is None:
            raise ValueError("Invalid value for `deployed_devices`, must not be `None`")

        self._deployed_devices = deployed_devices

    @property
    def updated_at(self):
        """
        Gets the updated_at of this UpdateCampaignStatusSerializer.
        The time the object was updated

        :return: The updated_at of this UpdateCampaignStatusSerializer.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this UpdateCampaignStatusSerializer.
        The time the object was updated

        :param updated_at: The updated_at of this UpdateCampaignStatusSerializer.
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    @property
    def when(self):
        """
        Gets the when of this UpdateCampaignStatusSerializer.
        The timestamp at which campaign is scheduled to start

        :return: The when of this UpdateCampaignStatusSerializer.
        :rtype: datetime
        """
        return self._when

    @when.setter
    def when(self, when):
        """
        Sets the when of this UpdateCampaignStatusSerializer.
        The timestamp at which campaign is scheduled to start

        :param when: The when of this UpdateCampaignStatusSerializer.
        :type: datetime
        """

        self._when = when

    @property
    def finished(self):
        """
        Gets the finished of this UpdateCampaignStatusSerializer.
        The timestamp when the update campaign finished

        :return: The finished of this UpdateCampaignStatusSerializer.
        :rtype: datetime
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """
        Sets the finished of this UpdateCampaignStatusSerializer.
        The timestamp when the update campaign finished

        :param finished: The finished of this UpdateCampaignStatusSerializer.
        :type: datetime
        """

        self._finished = finished

    @property
    def root_manifest_url(self):
        """
        Gets the root_manifest_url of this UpdateCampaignStatusSerializer.

        :return: The root_manifest_url of this UpdateCampaignStatusSerializer.
        :rtype: str
        """
        return self._root_manifest_url

    @root_manifest_url.setter
    def root_manifest_url(self, root_manifest_url):
        """
        Sets the root_manifest_url of this UpdateCampaignStatusSerializer.

        :param root_manifest_url: The root_manifest_url of this UpdateCampaignStatusSerializer.
        :type: str
        """
        if root_manifest_url is None:
            raise ValueError("Invalid value for `root_manifest_url`, must not be `None`")

        self._root_manifest_url = root_manifest_url

    @property
    def updating_api_key(self):
        """
        Gets the updating_api_key of this UpdateCampaignStatusSerializer.
        The gateway client API key

        :return: The updating_api_key of this UpdateCampaignStatusSerializer.
        :rtype: str
        """
        return self._updating_api_key

    @updating_api_key.setter
    def updating_api_key(self, updating_api_key):
        """
        Sets the updating_api_key of this UpdateCampaignStatusSerializer.
        The gateway client API key

        :param updating_api_key: The updating_api_key of this UpdateCampaignStatusSerializer.
        :type: str
        """
        if updating_api_key is None:
            raise ValueError("Invalid value for `updating_api_key`, must not be `None`")

        self._updating_api_key = updating_api_key

    @property
    def updating_account_id(self):
        """
        Gets the updating_account_id of this UpdateCampaignStatusSerializer.
        The updating account ID

        :return: The updating_account_id of this UpdateCampaignStatusSerializer.
        :rtype: str
        """
        return self._updating_account_id

    @updating_account_id.setter
    def updating_account_id(self, updating_account_id):
        """
        Sets the updating_account_id of this UpdateCampaignStatusSerializer.
        The updating account ID

        :param updating_account_id: The updating_account_id of this UpdateCampaignStatusSerializer.
        :type: str
        """
        if updating_account_id is None:
            raise ValueError("Invalid value for `updating_account_id`, must not be `None`")

        self._updating_account_id = updating_account_id

    @property
    def device_filter(self):
        """
        Gets the device_filter of this UpdateCampaignStatusSerializer.
        The filter for the devices the campaign will target

        :return: The device_filter of this UpdateCampaignStatusSerializer.
        :rtype: str
        """
        return self._device_filter

    @device_filter.setter
    def device_filter(self, device_filter):
        """
        Sets the device_filter of this UpdateCampaignStatusSerializer.
        The filter for the devices the campaign will target

        :param device_filter: The device_filter of this UpdateCampaignStatusSerializer.
        :type: str
        """
        if device_filter is None:
            raise ValueError("Invalid value for `device_filter`, must not be `None`")

        self._device_filter = device_filter

    @property
    def name(self):
        """
        Gets the name of this UpdateCampaignStatusSerializer.
        A name for this campaign

        :return: The name of this UpdateCampaignStatusSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateCampaignStatusSerializer.
        A name for this campaign

        :param name: The name of this UpdateCampaignStatusSerializer.
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
        if not isinstance(other, UpdateCampaignStatusSerializer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
