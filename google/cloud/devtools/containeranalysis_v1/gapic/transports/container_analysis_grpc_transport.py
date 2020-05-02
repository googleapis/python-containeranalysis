# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import google.api_core.grpc_helpers

from google.cloud.devtools.containeranalysis_v1.proto import containeranalysis_pb2_grpc


class ContainerAnalysisGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.devtools.containeranalysis.v1 ContainerAnalysis API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self,
        channel=None,
        credentials=None,
        address="containeranalysis.googleapis.com:443",
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive."
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "container_analysis_stub": containeranalysis_pb2_grpc.ContainerAnalysisStub(
                channel
            )
        }

    @classmethod
    def create_channel(
        cls, address="containeranalysis.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def set_iam_policy(self):
        """Return the gRPC stub for :meth:`ContainerAnalysisClient.set_iam_policy`.

        If set, all the classes from the .proto file are wrapped in a single
        outer class with the given name. This applies to both Proto1 (equivalent
        to the old "--one_java_file" option) and Proto2 (where a .proto always
        translates to a single class, but you may want to explicitly choose the
        class name).

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["container_analysis_stub"].SetIamPolicy

    @property
    def get_iam_policy(self):
        """Return the gRPC stub for :meth:`ContainerAnalysisClient.get_iam_policy`.

        Specifies the identities requesting access for a Cloud Platform
        resource. ``members`` can have the following values:

        -  ``allUsers``: A special identifier that represents anyone who is on
           the internet; with or without a Google account.

        -  ``allAuthenticatedUsers``: A special identifier that represents
           anyone who is authenticated with a Google account or a service
           account.

        -  ``user:{emailid}``: An email address that represents a specific
           Google account. For example, ``alice@example.com`` .

        -  ``serviceAccount:{emailid}``: An email address that represents a
           service account. For example,
           ``my-other-app@appspot.gserviceaccount.com``.

        -  ``group:{emailid}``: An email address that represents a Google group.
           For example, ``admins@example.com``.

        -  ``domain:{domain}``: The G Suite domain (primary) that represents all
           the users of that domain. For example, ``google.com`` or
           ``example.com``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["container_analysis_stub"].GetIamPolicy

    @property
    def test_iam_permissions(self):
        """Return the gRPC stub for :meth:`ContainerAnalysisClient.test_iam_permissions`.

        Optional. The relative resource name pattern associated with this
        resource type. The DNS prefix of the full resource name shouldn't be
        specified here.

        The path pattern must follow the syntax, which aligns with HTTP binding
        syntax:

        ::

            Template = Segment { "/" Segment } ;
            Segment = LITERAL | Variable ;
            Variable = "{" LITERAL "}" ;

        Examples:

        ::

            - "projects/{project}/topics/{topic}"
            - "projects/{project}/knowledgeBases/{knowledge_base}"

        The components in braces correspond to the IDs for each resource in the
        hierarchy. It is expected that, if multiple patterns are provided, the
        same component name (e.g. "project") refers to IDs of the same type of
        resource.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["container_analysis_stub"].TestIamPermissions
