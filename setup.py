# Hadoop Configuration File Linter.
# Copyright (C) 2015 Ewan Higgs
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from os.path import join as mkpath
import sys
import subprocess
from setuptools import setup, Command

class BaseCommand(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass

class TestCommand(BaseCommand):
    description = "Run unit tests."

    def run(self):
        ret = subprocess.call("python -m unittest discover -b -s test/unit -v".split(' '))
        sys.exit(ret)


class CoverageCommand(BaseCommand):
    description = "Run unit tests."

    def run(self):
        ret = subprocess.call(["coverage", "run", "--omit", "*/.virtualenvs/*",
            "-m", "unittest", "discover", "-v", "-b", "-s", "test/unit/"])
        if not ret:
            ret = subprocess.call(["coverage", "report"])
        sys.exit(ret)


def find_files(*dirs):
    results = []
    for src_dir in dirs:
        for root, dirs, files in os.walk(src_dir):
            results.append((root, map(lambda f: mkpath(root, f), files)))
    return results

PACKAGE = {
    'name': 'hadoop-config-lint',
    'version': '0.1',
    'author': ['ewan.higgs@ugent.be'],
    'license': "GPL v3",
    'install_requires': [ ],
    'tests_require': ['tox', 'coveralls', 'mock'],
    'packages': [
        'hadoop_config_lint',
    ],
    'data_files': find_files('etc'),
    'scripts': ['bin/hadoop-lint'],
    'cmdclass' : {'test': TestCommand, 'cov': CoverageCommand},
    'long_description': open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
}

if __name__ == '__main__':
    setup(**PACKAGE)

