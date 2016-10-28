#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
#pylint: skip-file
from msrest.serialization import Model


class IssuerCredentials(Model):
    """The credentials to be used for the certificate issuer.

    :param account_id: The user name/account name/account id.
    :type account_id: str
    :param password: The password/secret/account key.
    :type password: str
    """ 

    _attribute_map = {
        'account_id': {'key': 'account_id', 'type': 'str'},
        'password': {'key': 'pwd', 'type': 'str'},
    }

    def __init__(self, account_id=None, password=None):
        self.account_id = account_id
        self.password = password