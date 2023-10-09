from setuptools import find_packages, setup

package_name = "ament_black"

setup(
    name=package_name,
    version="0.2.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/" + package_name, ["package.xml"]),
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
    ],
    install_requires=[
        "setuptools==56.6.0",
        "unidiff==0.5.5",
        "black==21.12b0",
    ],
    zip_safe=False,
    author="Tyler Weaver",
    author_email="tylerjw@gmail.com",
    maintainer="Ignacio Vizzo",
    maintainer_email="ignacio.vizzo@dexory.com",
    url="https://github.com/botsandus/ament_black",
    download_url="https://github.com/botsandus/ament_black/releases",
    keywords=["ROS"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    description="Check Python code style using black.",
    long_description="""\
The ability to check code against style conventions using black
and generate xUnit test result files.""",
    license="Apache License, Version 2.0, BSD",
    tests_require=["pytest"],
    entry_points={"console_scripts": ["ament_black = ament_black.main:main"]},
)
