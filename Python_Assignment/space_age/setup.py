import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="space_age",
    version="1.0.2",
    description="It gives your age in other planets.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/anitabaral/lf_internship_workspace/Python_Assignment/space_age",
    author="Anita Baral",
    author_email="baralanita2@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["space"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "space=space.__main__:main",
        ]
    },
)
