# coding: utf-8

"""
    Device Directory API

    This is the API Documentation for the Mbed device directory update service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceDataPostRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, bootstrap_expiration_date=None, bootstrapped_timestamp=None, connector_expiration_date=None, mechanism=None, device_class=None, endpoint_name=None, auto_update=None, host_gateway=None, device_execution_mode=None, custom_attributes=None, state=None, serial_number=None, firmware_checksum=None, vendor_id=None, description=None, deployed_state=None, object=None, endpoint_type=None, deployment=None, mechanism_url=None, trust_level=None, name=None, device_key=None, manifest=None, ca_id=None):
        """
        DeviceDataPostRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'bootstrap_expiration_date': 'datetime',
            'bootstrapped_timestamp': 'datetime',
            'connector_expiration_date': 'datetime',
            'mechanism': 'str',
            'device_class': 'str',
            'endpoint_name': 'str',
            'auto_update': 'bool',
            'host_gateway': 'str',
            'device_execution_mode': 'int',
            'custom_attributes': 'dict(str, str)',
            'state': 'str',
            'serial_number': 'str',
            'firmware_checksum': 'str',
            'vendor_id': 'str',
            'description': 'str',
            'deployed_state': 'str',
            'object': 'str',
            'endpoint_type': 'str',
            'deployment': 'str',
            'mechanism_url': 'str',
            'trust_level': 'int',
            'name': 'str',
            'device_key': 'str',
            'manifest': 'str',
            'ca_id': 'str'
        }

        self.attribute_map = {
            'bootstrap_expiration_date': 'bootstrap_expiration_date',
            'bootstrapped_timestamp': 'bootstrapped_timestamp',
            'connector_expiration_date': 'connector_expiration_date',
            'mechanism': 'mechanism',
            'device_class': 'device_class',
            'endpoint_name': 'endpoint_name',
            'auto_update': 'auto_update',
            'host_gateway': 'host_gateway',
            'device_execution_mode': 'device_execution_mode',
            'custom_attributes': 'custom_attributes',
            'state': 'state',
            'serial_number': 'serial_number',
            'firmware_checksum': 'firmware_checksum',
            'vendor_id': 'vendor_id',
            'description': 'description',
            'deployed_state': 'deployed_state',
            'object': 'object',
            'endpoint_type': 'endpoint_type',
            'deployment': 'deployment',
            'mechanism_url': 'mechanism_url',
            'trust_level': 'trust_level',
            'name': 'name',
            'device_key': 'device_key',
            'manifest': 'manifest',
            'ca_id': 'ca_id'
        }

        self._bootstrap_expiration_date = bootstrap_expiration_date
        self._bootstrapped_timestamp = bootstrapped_timestamp
        self._connector_expiration_date = connector_expiration_date
        self._mechanism = mechanism
        self._device_class = device_class
        self._endpoint_name = endpoint_name
        self._auto_update = auto_update
        self._host_gateway = host_gateway
        self._device_execution_mode = device_execution_mode
        self._custom_attributes = custom_attributes
        self._state = state
        self._serial_number = serial_number
        self._firmware_checksum = firmware_checksum
        self._vendor_id = vendor_id
        self._description = description
        self._deployed_state = deployed_state
        self._object = object
        self._endpoint_type = endpoint_type
        self._deployment = deployment
        self._mechanism_url = mechanism_url
        self._trust_level = trust_level
        self._name = name
        self._device_key = device_key
        self._manifest = manifest
        self._ca_id = ca_id

    @property
    def bootstrap_expiration_date(self):
        """
        Gets the bootstrap_expiration_date of this DeviceDataPostRequest.
        The expiration date of the certificate used to connect to bootstrap server.

        :return: The bootstrap_expiration_date of this DeviceDataPostRequest.
        :rtype: datetime
        """
        return self._bootstrap_expiration_date

    @bootstrap_expiration_date.setter
    def bootstrap_expiration_date(self, bootstrap_expiration_date):
        """
        Sets the bootstrap_expiration_date of this DeviceDataPostRequest.
        The expiration date of the certificate used to connect to bootstrap server.

        :param bootstrap_expiration_date: The bootstrap_expiration_date of this DeviceDataPostRequest.
        :type: datetime
        """

        self._bootstrap_expiration_date = bootstrap_expiration_date

    @property
    def bootstrapped_timestamp(self):
        """
        Gets the bootstrapped_timestamp of this DeviceDataPostRequest.
        The timestamp of the device's most recent bootstrap process..

        :return: The bootstrapped_timestamp of this DeviceDataPostRequest.
        :rtype: datetime
        """
        return self._bootstrapped_timestamp

    @bootstrapped_timestamp.setter
    def bootstrapped_timestamp(self, bootstrapped_timestamp):
        """
        Sets the bootstrapped_timestamp of this DeviceDataPostRequest.
        The timestamp of the device's most recent bootstrap process..

        :param bootstrapped_timestamp: The bootstrapped_timestamp of this DeviceDataPostRequest.
        :type: datetime
        """

        self._bootstrapped_timestamp = bootstrapped_timestamp

    @property
    def connector_expiration_date(self):
        """
        Gets the connector_expiration_date of this DeviceDataPostRequest.
        The expiration date of the certificate used to connect to the LWM2M server.

        :return: The connector_expiration_date of this DeviceDataPostRequest.
        :rtype: datetime
        """
        return self._connector_expiration_date

    @connector_expiration_date.setter
    def connector_expiration_date(self, connector_expiration_date):
        """
        Sets the connector_expiration_date of this DeviceDataPostRequest.
        The expiration date of the certificate used to connect to the LWM2M server.

        :param connector_expiration_date: The connector_expiration_date of this DeviceDataPostRequest.
        :type: datetime
        """

        self._connector_expiration_date = connector_expiration_date

    @property
    def mechanism(self):
        """
        Gets the mechanism of this DeviceDataPostRequest.
        The ID of the channel used to communicate with the device.

        :return: The mechanism of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """
        Sets the mechanism of this DeviceDataPostRequest.
        The ID of the channel used to communicate with the device.

        :param mechanism: The mechanism of this DeviceDataPostRequest.
        :type: str
        """
        allowed_values = ["connector", "direct"]
        if mechanism not in allowed_values:
            raise ValueError(
                "Invalid value for `mechanism` ({0}), must be one of {1}"
                .format(mechanism, allowed_values)
            )

        self._mechanism = mechanism

    @property
    def device_class(self):
        """
        Gets the device_class of this DeviceDataPostRequest.
        An ID representing the model and hardware revision of the device.

        :return: The device_class of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._device_class

    @device_class.setter
    def device_class(self, device_class):
        """
        Sets the device_class of this DeviceDataPostRequest.
        An ID representing the model and hardware revision of the device.

        :param device_class: The device_class of this DeviceDataPostRequest.
        :type: str
        """
        if device_class is not None and len(device_class) > 500:
            raise ValueError("Invalid value for `device_class`, length must be less than or equal to `500`")

        self._device_class = device_class

    @property
    def endpoint_name(self):
        """
        Gets the endpoint_name of this DeviceDataPostRequest.
        The endpoint name given to the device.

        :return: The endpoint_name of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """
        Sets the endpoint_name of this DeviceDataPostRequest.
        The endpoint name given to the device.

        :param endpoint_name: The endpoint_name of this DeviceDataPostRequest.
        :type: str
        """
        if endpoint_name is not None and len(endpoint_name) > 64:
            raise ValueError("Invalid value for `endpoint_name`, length must be less than or equal to `64`")

        self._endpoint_name = endpoint_name

    @property
    def auto_update(self):
        """
        Gets the auto_update of this DeviceDataPostRequest.
        DEPRECATED: Mark this device for automatic firmware update.

        :return: The auto_update of this DeviceDataPostRequest.
        :rtype: bool
        """
        return self._auto_update

    @auto_update.setter
    def auto_update(self, auto_update):
        """
        Sets the auto_update of this DeviceDataPostRequest.
        DEPRECATED: Mark this device for automatic firmware update.

        :param auto_update: The auto_update of this DeviceDataPostRequest.
        :type: bool
        """

        self._auto_update = auto_update

    @property
    def host_gateway(self):
        """
        Gets the host_gateway of this DeviceDataPostRequest.
        The `endpoint_name` of the host gateway, if appropriate.

        :return: The host_gateway of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._host_gateway

    @host_gateway.setter
    def host_gateway(self, host_gateway):
        """
        Sets the host_gateway of this DeviceDataPostRequest.
        The `endpoint_name` of the host gateway, if appropriate.

        :param host_gateway: The host_gateway of this DeviceDataPostRequest.
        :type: str
        """

        self._host_gateway = host_gateway

    @property
    def device_execution_mode(self):
        """
        Gets the device_execution_mode of this DeviceDataPostRequest.
        The execution mode from the certificate of the device. Permitted values:   - 0 - unspecified execution mode (default)   - 1 - development devices   - 5 - production devices

        :return: The device_execution_mode of this DeviceDataPostRequest.
        :rtype: int
        """
        return self._device_execution_mode

    @device_execution_mode.setter
    def device_execution_mode(self, device_execution_mode):
        """
        Sets the device_execution_mode of this DeviceDataPostRequest.
        The execution mode from the certificate of the device. Permitted values:   - 0 - unspecified execution mode (default)   - 1 - development devices   - 5 - production devices

        :param device_execution_mode: The device_execution_mode of this DeviceDataPostRequest.
        :type: int
        """

        self._device_execution_mode = device_execution_mode

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this DeviceDataPostRequest.
        Up to five custom key-value attributes.

        :return: The custom_attributes of this DeviceDataPostRequest.
        :rtype: dict(str, str)
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this DeviceDataPostRequest.
        Up to five custom key-value attributes.

        :param custom_attributes: The custom_attributes of this DeviceDataPostRequest.
        :type: dict(str, str)
        """

        self._custom_attributes = custom_attributes

    @property
    def state(self):
        """
        Gets the state of this DeviceDataPostRequest.
        The current state of the device.

        :return: The state of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DeviceDataPostRequest.
        The current state of the device.

        :param state: The state of this DeviceDataPostRequest.
        :type: str
        """
        allowed_values = ["unenrolled", "cloud_enrolling", "bootstrapped", "registered", "deregistered"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def serial_number(self):
        """
        Gets the serial_number of this DeviceDataPostRequest.
        The serial number of the device.

        :return: The serial_number of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this DeviceDataPostRequest.
        The serial number of the device.

        :param serial_number: The serial_number of this DeviceDataPostRequest.
        :type: str
        """
        if serial_number is not None and len(serial_number) > 64:
            raise ValueError("Invalid value for `serial_number`, length must be less than or equal to `64`")

        self._serial_number = serial_number

    @property
    def firmware_checksum(self):
        """
        Gets the firmware_checksum of this DeviceDataPostRequest.
        The SHA256 checksum of the current firmware image.

        :return: The firmware_checksum of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._firmware_checksum

    @firmware_checksum.setter
    def firmware_checksum(self, firmware_checksum):
        """
        Sets the firmware_checksum of this DeviceDataPostRequest.
        The SHA256 checksum of the current firmware image.

        :param firmware_checksum: The firmware_checksum of this DeviceDataPostRequest.
        :type: str
        """
        if firmware_checksum is not None and len(firmware_checksum) > 64:
            raise ValueError("Invalid value for `firmware_checksum`, length must be less than or equal to `64`")

        self._firmware_checksum = firmware_checksum

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this DeviceDataPostRequest.
        The device vendor ID.

        :return: The vendor_id of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this DeviceDataPostRequest.
        The device vendor ID.

        :param vendor_id: The vendor_id of this DeviceDataPostRequest.
        :type: str
        """
        if vendor_id is not None and len(vendor_id) > 255:
            raise ValueError("Invalid value for `vendor_id`, length must be less than or equal to `255`")

        self._vendor_id = vendor_id

    @property
    def description(self):
        """
        Gets the description of this DeviceDataPostRequest.
        The description of the device.

        :return: The description of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceDataPostRequest.
        The description of the device.

        :param description: The description of this DeviceDataPostRequest.
        :type: str
        """

        self._description = description

    @property
    def deployed_state(self):
        """
        Gets the deployed_state of this DeviceDataPostRequest.
        DEPRECATED: The state of the device's deployment.

        :return: The deployed_state of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._deployed_state

    @deployed_state.setter
    def deployed_state(self, deployed_state):
        """
        Sets the deployed_state of this DeviceDataPostRequest.
        DEPRECATED: The state of the device's deployment.

        :param deployed_state: The deployed_state of this DeviceDataPostRequest.
        :type: str
        """
        allowed_values = ["development", "production"]
        if deployed_state not in allowed_values:
            raise ValueError(
                "Invalid value for `deployed_state` ({0}), must be one of {1}"
                .format(deployed_state, allowed_values)
            )

        self._deployed_state = deployed_state

    @property
    def object(self):
        """
        Gets the object of this DeviceDataPostRequest.
        The API resource entity.

        :return: The object of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this DeviceDataPostRequest.
        The API resource entity.

        :param object: The object of this DeviceDataPostRequest.
        :type: str
        """

        self._object = object

    @property
    def endpoint_type(self):
        """
        Gets the endpoint_type of this DeviceDataPostRequest.
        The endpoint type of the device. For example, the device is a gateway.

        :return: The endpoint_type of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """
        Sets the endpoint_type of this DeviceDataPostRequest.
        The endpoint type of the device. For example, the device is a gateway.

        :param endpoint_type: The endpoint_type of this DeviceDataPostRequest.
        :type: str
        """
        if endpoint_type is not None and len(endpoint_type) > 64:
            raise ValueError("Invalid value for `endpoint_type`, length must be less than or equal to `64`")

        self._endpoint_type = endpoint_type

    @property
    def deployment(self):
        """
        Gets the deployment of this DeviceDataPostRequest.
        DEPRECATED: The last deployment used on the device.

        :return: The deployment of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """
        Sets the deployment of this DeviceDataPostRequest.
        DEPRECATED: The last deployment used on the device.

        :param deployment: The deployment of this DeviceDataPostRequest.
        :type: str
        """

        self._deployment = deployment

    @property
    def mechanism_url(self):
        """
        Gets the mechanism_url of this DeviceDataPostRequest.
        The address of the connector to use.

        :return: The mechanism_url of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._mechanism_url

    @mechanism_url.setter
    def mechanism_url(self, mechanism_url):
        """
        Sets the mechanism_url of this DeviceDataPostRequest.
        The address of the connector to use.

        :param mechanism_url: The mechanism_url of this DeviceDataPostRequest.
        :type: str
        """

        self._mechanism_url = mechanism_url

    @property
    def trust_level(self):
        """
        Gets the trust_level of this DeviceDataPostRequest.
        The device trust level.

        :return: The trust_level of this DeviceDataPostRequest.
        :rtype: int
        """
        return self._trust_level

    @trust_level.setter
    def trust_level(self, trust_level):
        """
        Sets the trust_level of this DeviceDataPostRequest.
        The device trust level.

        :param trust_level: The trust_level of this DeviceDataPostRequest.
        :type: int
        """

        self._trust_level = trust_level

    @property
    def name(self):
        """
        Gets the name of this DeviceDataPostRequest.
        The name of the device.

        :return: The name of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceDataPostRequest.
        The name of the device.

        :param name: The name of this DeviceDataPostRequest.
        :type: str
        """
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")

        self._name = name

    @property
    def device_key(self):
        """
        Gets the device_key of this DeviceDataPostRequest.
        The fingerprint of the device certificate.

        :return: The device_key of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._device_key

    @device_key.setter
    def device_key(self, device_key):
        """
        Sets the device_key of this DeviceDataPostRequest.
        The fingerprint of the device certificate.

        :param device_key: The device_key of this DeviceDataPostRequest.
        :type: str
        """
        if device_key is None:
            raise ValueError("Invalid value for `device_key`, must not be `None`")
        if device_key is not None and len(device_key) > 512:
            raise ValueError("Invalid value for `device_key`, length must be less than or equal to `512`")

        self._device_key = device_key

    @property
    def manifest(self):
        """
        Gets the manifest of this DeviceDataPostRequest.
        DEPRECATED: The URL for the current device manifest.

        :return: The manifest of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """
        Sets the manifest of this DeviceDataPostRequest.
        DEPRECATED: The URL for the current device manifest.

        :param manifest: The manifest of this DeviceDataPostRequest.
        :type: str
        """

        self._manifest = manifest

    @property
    def ca_id(self):
        """
        Gets the ca_id of this DeviceDataPostRequest.
        The certificate issuer's ID.

        :return: The ca_id of this DeviceDataPostRequest.
        :rtype: str
        """
        return self._ca_id

    @ca_id.setter
    def ca_id(self, ca_id):
        """
        Sets the ca_id of this DeviceDataPostRequest.
        The certificate issuer's ID.

        :param ca_id: The ca_id of this DeviceDataPostRequest.
        :type: str
        """
        if ca_id is None:
            raise ValueError("Invalid value for `ca_id`, must not be `None`")
        if ca_id is not None and len(ca_id) > 500:
            raise ValueError("Invalid value for `ca_id`, length must be less than or equal to `500`")

        self._ca_id = ca_id

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
        if not isinstance(other, DeviceDataPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
