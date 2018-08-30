import warnings

from mbed_cloud.sdk import Config
from mbed_cloud.sdk.common.client import Client


global_sdk = None
has_warned = None


class SDK(object):
    def __init__(self, config=None, **config_overrides):
        """Create a new SDK instance

        [Beta] this section of the SDK is at a `beta` release level
               and is subject to change without notice

        :param config: An SDK config object
        :type config: Config

        :param config_overrides: Key-value updates to apply to the config
        :type config_overrides: dict(str, str)
        """
        beta_warning(self.__class__)
        self._config = Config()
        if config:
            self._config.update(config.to_dict())
        self._config.update(**config_overrides)
        self._client = Client(self._config)

        from mbed_cloud.sdk.common._entities import InstanceFactory

        self.entities = InstanceFactory(self.client)

    @property
    def client(self):
        return self._client

    @property
    def config(self):
        return self._config


def get_or_create_global_sdk_instance():
    """For simple use cases, a single global SDK is sufficient"""
    global global_sdk
    if global_sdk is None:
        global_sdk = SDK()
    return global_sdk


def beta_warning(header, category=FutureWarning):
    global has_warned
    if not has_warned:
        warnings.warn(
"""
`%s`
[Beta] this section of the SDK is at a `beta` release level
       and is subject to change without notice
""" % header,
            category=category,
            stacklevel=3  # make the trace log from two levels above this `warnings.warn` line
        )
        has_warned = True
