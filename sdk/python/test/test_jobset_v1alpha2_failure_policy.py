# coding: utf-8

"""
    JobSet SDK

    Python SDK for the JobSet API  # noqa: E501

    The version of the OpenAPI document: v0.1.4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# Kubernetes imports
from kubernetes.client.models.v1_job_template_spec import V1JobTemplateSpec
# Kubernetes imports
from kubernetes.client.models.v1_job_template_spec import V1JobTemplateSpec
import unittest
import datetime

import jobset
from jobset.models.jobset_v1alpha2_failure_policy import JobsetV1alpha2FailurePolicy  # noqa: E501
from jobset.rest import ApiException

class TestJobsetV1alpha2FailurePolicy(unittest.TestCase):
    """JobsetV1alpha2FailurePolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobsetV1alpha2FailurePolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jobset.models.jobset_v1alpha2_failure_policy.JobsetV1alpha2FailurePolicy()  # noqa: E501
        if include_optional :
            return JobsetV1alpha2FailurePolicy(
                max_restarts = 56
            )
        else :
            return JobsetV1alpha2FailurePolicy(
        )

    def testJobsetV1alpha2FailurePolicy(self):
        """Test JobsetV1alpha2FailurePolicy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
