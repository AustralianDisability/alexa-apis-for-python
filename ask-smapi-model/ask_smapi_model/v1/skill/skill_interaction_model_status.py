# coding: utf-8

#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.
#

import pprint
import re  # noqa: F401
import six
import typing
from enum import Enum


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime
    from ask_smapi_model.v1.skill.interaction_model_last_update_request import InteractionModelLastUpdateRequest as InteractionModelLastUpdateRequest_f980bda4


class SkillInteractionModelStatus(object):
    """
    Defines the structure for interaction model build status.


    :param last_update_request: 
    :type last_update_request: (optional) ask_smapi_model.v1.skill.interaction_model_last_update_request.InteractionModelLastUpdateRequest
    :param e_tag: An opaque identifier for last successfully updated resource.
    :type e_tag: (optional) str
    :param version: Version for last successfully built model.
    :type version: (optional) str

    """
    deserialized_types = {
        'last_update_request': 'ask_smapi_model.v1.skill.interaction_model_last_update_request.InteractionModelLastUpdateRequest',
        'e_tag': 'str',
        'version': 'str'
    }  # type: Dict

    attribute_map = {
        'last_update_request': 'lastUpdateRequest',
        'e_tag': 'eTag',
        'version': 'version'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, last_update_request=None, e_tag=None, version=None):
        # type: (Optional[InteractionModelLastUpdateRequest_f980bda4], Optional[str], Optional[str]) -> None
        """Defines the structure for interaction model build status.

        :param last_update_request: 
        :type last_update_request: (optional) ask_smapi_model.v1.skill.interaction_model_last_update_request.InteractionModelLastUpdateRequest
        :param e_tag: An opaque identifier for last successfully updated resource.
        :type e_tag: (optional) str
        :param version: Version for last successfully built model.
        :type version: (optional) str
        """
        self.__discriminator_value = None  # type: str

        self.last_update_request = last_update_request
        self.e_tag = e_tag
        self.version = version

    def to_dict(self):
        # type: () -> Dict[str, object]
        """Returns the model properties as a dict"""
        result = {}  # type: Dict

        for attr, _ in six.iteritems(self.deserialized_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else
                    x.value if isinstance(x, Enum) else x,
                    value
                ))
            elif isinstance(value, Enum):
                result[attr] = value.value
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else
                    (item[0], item[1].value)
                    if isinstance(item[1], Enum) else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        # type: () -> str
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        # type: () -> str
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, SkillInteractionModelStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
