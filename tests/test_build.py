#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import multiprocessing
import os
import sys

from mock import patch
from oslo_log import fixture as log_fixture
from oslo_log import log as logging
from oslotest import base
import testtools

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../tools')))
from kolla.image import build

LOG = logging.getLogger(__name__)


class BuildTest(object):
    excluded_images = []

    def setUp(self):
        super(BuildTest, self).setUp()
        self.useFixture(log_fixture.SetLogLevel([__name__],
                                                logging.logging.INFO))

        self.threads = multiprocessing.cpu_count()
        if self.threads < 4:
            self.threads = 4

        self.build_args = [__name__, '--threads', str(self.threads)]

    @testtools.skipUnless(os.environ.get('DOCKER_BUILD_TEST'),
                          'Skip the docker build test')
    def runTest(self):
        with patch.object(sys, 'argv', self.build_args):
            LOG.info("Running with args %s", self.build_args)
            (bad_results, good_results, unmatched_results,
             skipped_results) = build.run_build()

        failures = 0
        for image, result in bad_results.items():
            if result is not 'error':
                continue
            failures = failures + 1
            LOG.critical(">>> Expected image '%s' to succeed!", image)

        for image in unmatched_results.keys():
            LOG.warning(">>> Image '%s' was not matched", image)

        self.assertEqual(failures, 0, "%d failure(s) occurred" % failures)


class BuildTestCentosBinary(BuildTest, base.BaseTestCase):

    def setUp(self):
        super(BuildTestCentosBinary, self).setUp()
        self.build_args.extend(["--base", "centos",
                                "--type", "binary"])


class BuildTestCentosSource(BuildTest, base.BaseTestCase):

    def setUp(self):
        super(BuildTestCentosSource, self).setUp()
        self.build_args.extend(["--base", "centos",
                                "--type", "source"])


class BuildTestUbuntuBinary(BuildTest, base.BaseTestCase):

    def setUp(self):
        super(BuildTestUbuntuBinary, self).setUp()
        self.build_args.extend(["--base", "ubuntu",
                                "--type", "binary"])


class BuildTestUbuntuSource(BuildTest, base.BaseTestCase):

    def setUp(self):
        super(BuildTestUbuntuSource, self).setUp()
        self.build_args.extend(["--base", "ubuntu",
                                "--type", "source"])


class BuildTestDebianBinary(BuildTest, base.BaseTestCase):

    def setUp(self):
        super(BuildTestDebianBinary, self).setUp()
        self.build_args.extend(["--base", "debian",
                                "--type", "binary"])


class BuildTestDebianSource(BuildTest, base.BaseTestCase):

    def setUp(self):
        super(BuildTestDebianSource, self).setUp()
        self.build_args.extend(["--base", "debian",
                                "--type", "source"])


class BuildTestOracleLinuxBinary(BuildTest, base.BaseTestCase):

    def setUp(self):
        super(BuildTestOracleLinuxBinary, self).setUp()
        self.build_args.extend(["--base", "oraclelinux",
                                "--type", "binary"])


class BuildTestOracleLinuxSource(BuildTest, base.BaseTestCase):

    def setUp(self):
        super(BuildTestOracleLinuxSource, self).setUp()
        self.build_args.extend(["--base", "oraclelinux",
                                "--type", "source"])


class DeployTestCentosBinary(BuildTestCentosBinary):

    def setUp(self):
        super(DeployTestCentosBinary, self).setUp()
        self.build_args.extend(["--profile", "gate"])


class DeployTestCentosSource(BuildTestCentosSource):

    def setUp(self):
        super(DeployTestCentosSource, self).setUp()
        self.build_args.extend(["--profile", "gate"])


class DeployTestOracleLinuxBinary(BuildTestOracleLinuxBinary):

    def setUp(self):
        super(DeployTestOracleLinuxBinary, self).setUp()
        self.build_args.extend(["--profile", "gate"])


class DeployTestOracleLinuxSource(BuildTestOracleLinuxSource):

    def setUp(self):
        super(DeployTestOracleLinuxSource, self).setUp()
        self.build_args.extend(["--profile", "gate"])


class DeployTestUbuntuBinary(BuildTestUbuntuBinary):

    def setUp(self):
        super(DeployTestUbuntuBinary, self).setUp()
        self.build_args.extend(["--profile", "gate"])


class DeployTestUbuntuSource(BuildTestUbuntuSource):

    def setUp(self):
        super(DeployTestUbuntuSource, self).setUp()
        self.build_args.extend(["--profile", "gate"])
