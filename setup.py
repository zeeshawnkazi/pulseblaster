# -*- coding: utf-8 -*-
import sys
import re
from setuptools import setup, find_namespace_packages

package_name = 'pulseblaster'
package_source = '.'

VERSIONFILE=f'{package_name}/__version__.py'
verstrline = open(VERSIONFILE, 'rt').read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    __version__ = mo.group(1)
else:
    raise RuntimeError(f'Unable to find version string in{VERSIONFILE}.')

requirements = [
    'numpy',
]

# The README.md file content is included in the package metadata as long description and will be
# automatically shown as project description on the PyPI once you release it there.
with open('README.md', 'r') as file:
    long_description = file.read()


setup(
    name=package_name,  # Choose a custom name
    version=__version__,  # Automatically deduced from "VERSIONFILE" file (see above)
    packages=find_namespace_packages(where=package_source),  # This should be enough for 95% of the use-cases
    package_dir={'': package_source},  # same
    package_data={'': ['README.md'],  # include data files
                  },
    description='Python control code for Pulseblaster pulse generation hardware',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zeeshawnkazi/pulseblaster',

    license='GPLv3',  # License tag
    install_requires=requirements,  # package dependencies
    python_requires='~=3.8',  # Specify compatible Python versions
)
