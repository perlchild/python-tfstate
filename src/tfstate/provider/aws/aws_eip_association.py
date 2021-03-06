# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsEipAssociation(AwsResource):
    """
    Provides a resource to create an AWS VPC routing table.

    Usage::

        AwsEipAssociation(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_eip_association":
            raise InvalidResource("AwsEipAssociation must be of 'aws_eip_association' type")
        attributes = self.primary_data['attributes']
        self.allocation_id = attributes.get('allocation_id', None)
        self.instance_id = attributes.get('instance_id', None)
        self.network_interface_id = attributes.get('network_interface_id', None)
        self.private_ip_address = attributes.get('private_ip_address', None)
        self.public_ip = attributes.get('public_ip', None)
