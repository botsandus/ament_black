from setuptools import find_packages
from setuptools import setup

package_name = 'ament_black'

setup(
    name=package_name,
    version='0.2.7',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ],
    install_requires=[
        # black is a formatter, so its version controls output. Bound it to the
        # 2026 stable-style year: >=26.3 picks up Python 3.14 wheels and matches the
        # image's black, while <27 caps black's once-a-year stable-style change so
        # this pip install path (the pre-commit hook) can't silently format
        # differently from the image's black used by the colcon/deb lint, which is
        # governed by package.xml rather than setup.py. The old black==21.12b0 pin
        # had no Python 3.14 wheel. uvloop is left unpinned below (optional
        # accelerator, no effect on formatting; the old uvloop==0.17.0 pin had no
        # py3.14 wheel either). The maybe_install_uvloop/maybe_use_uvloop rename
        # across black versions is handled by the fallback in main.py.
        'black>=26.3,<27',
        'packaging>=20.3',
        'setuptools>=56',
        'unidiff>=0.5',
        'uvloop',
    ],
    zip_safe=False,
    author='Tyler Weaver',
    author_email='tylerjw@gmail.com',
    maintainer='Guillaume Doisy',
    maintainer_email='guillaume@dexory.com',
    url='https://github.com/botsandus/ament_black',
    download_url='https://github.com/botsandus/ament_black/releases',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Check Python code style using black.',
    long_description="""\
The ability to check code against style conventions using black
and generate xUnit test result files.""",
    license='Apache License, Version 2.0, BSD',
    entry_points={
        'console_scripts': ['ament_black = ament_black.main:main'],
        'pytest11': [
            'ament_black = ament_black.pytest_marker',
        ],
    },
)
