# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "communication email domain list",
)
class List(AAZCommand):
    """List requests to list all Domains resources under the parent EmailServices resource.

    :example: Get all domains from a email resource
        az communication email domain list --email-service-name ResourceName -g ResourceGroup
    """

    _aaz_info = {
        "version": "2023-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.communication/emailservices/{}/domains", "2023-04-01-preview"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.email_service_name = AAZStrArg(
            options=["--email-service-name"],
            help="The name of the EmailService resource.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]+$",
                max_length=63,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DomainsListByEmailServiceResource(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class DomainsListByEmailServiceResource(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Communication/emailServices/{emailServiceName}/domains",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "emailServiceName", self.ctx.args.email_service_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-04-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.data_location = AAZStrType(
                serialized_name="dataLocation",
                flags={"read_only": True},
            )
            properties.domain_management = AAZStrType(
                serialized_name="domainManagement",
                flags={"required": True},
            )
            properties.from_sender_domain = AAZStrType(
                serialized_name="fromSenderDomain",
                flags={"read_only": True},
            )
            properties.mail_from_sender_domain = AAZStrType(
                serialized_name="mailFromSenderDomain",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.user_engagement_tracking = AAZStrType(
                serialized_name="userEngagementTracking",
            )
            properties.verification_records = AAZObjectType(
                serialized_name="verificationRecords",
                flags={"read_only": True},
            )
            properties.verification_states = AAZObjectType(
                serialized_name="verificationStates",
                flags={"read_only": True},
            )

            verification_records = cls._schema_on_200.value.Element.properties.verification_records
            verification_records.dkim = AAZObjectType(
                serialized_name="DKIM",
            )
            _ListHelper._build_schema_dns_record_read(verification_records.dkim)
            verification_records.dkim2 = AAZObjectType(
                serialized_name="DKIM2",
            )
            _ListHelper._build_schema_dns_record_read(verification_records.dkim2)
            verification_records.dmarc = AAZObjectType(
                serialized_name="DMARC",
            )
            _ListHelper._build_schema_dns_record_read(verification_records.dmarc)
            verification_records.domain = AAZObjectType(
                serialized_name="Domain",
            )
            _ListHelper._build_schema_dns_record_read(verification_records.domain)
            verification_records.spf = AAZObjectType(
                serialized_name="SPF",
            )
            _ListHelper._build_schema_dns_record_read(verification_records.spf)

            verification_states = cls._schema_on_200.value.Element.properties.verification_states
            verification_states.dkim = AAZObjectType(
                serialized_name="DKIM",
            )
            _ListHelper._build_schema_verification_status_record_read(verification_states.dkim)
            verification_states.dkim2 = AAZObjectType(
                serialized_name="DKIM2",
            )
            _ListHelper._build_schema_verification_status_record_read(verification_states.dkim2)
            verification_states.dmarc = AAZObjectType(
                serialized_name="DMARC",
            )
            _ListHelper._build_schema_verification_status_record_read(verification_states.dmarc)
            verification_states.domain = AAZObjectType(
                serialized_name="Domain",
            )
            _ListHelper._build_schema_verification_status_record_read(verification_states.domain)
            verification_states.spf = AAZObjectType(
                serialized_name="SPF",
            )
            _ListHelper._build_schema_verification_status_record_read(verification_states.spf)

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_dns_record_read = None

    @classmethod
    def _build_schema_dns_record_read(cls, _schema):
        if cls._schema_dns_record_read is not None:
            _schema.name = cls._schema_dns_record_read.name
            _schema.ttl = cls._schema_dns_record_read.ttl
            _schema.type = cls._schema_dns_record_read.type
            _schema.value = cls._schema_dns_record_read.value
            return

        cls._schema_dns_record_read = _schema_dns_record_read = AAZObjectType()

        dns_record_read = _schema_dns_record_read
        dns_record_read.name = AAZStrType(
            flags={"read_only": True},
        )
        dns_record_read.ttl = AAZIntType(
            flags={"read_only": True},
        )
        dns_record_read.type = AAZStrType(
            flags={"read_only": True},
        )
        dns_record_read.value = AAZStrType(
            flags={"read_only": True},
        )

        _schema.name = cls._schema_dns_record_read.name
        _schema.ttl = cls._schema_dns_record_read.ttl
        _schema.type = cls._schema_dns_record_read.type
        _schema.value = cls._schema_dns_record_read.value

    _schema_verification_status_record_read = None

    @classmethod
    def _build_schema_verification_status_record_read(cls, _schema):
        if cls._schema_verification_status_record_read is not None:
            _schema.error_code = cls._schema_verification_status_record_read.error_code
            _schema.status = cls._schema_verification_status_record_read.status
            return

        cls._schema_verification_status_record_read = _schema_verification_status_record_read = AAZObjectType()

        verification_status_record_read = _schema_verification_status_record_read
        verification_status_record_read.error_code = AAZStrType(
            serialized_name="errorCode",
            flags={"read_only": True},
        )
        verification_status_record_read.status = AAZStrType(
            flags={"read_only": True},
        )

        _schema.error_code = cls._schema_verification_status_record_read.error_code
        _schema.status = cls._schema_verification_status_record_read.status


__all__ = ["List"]
