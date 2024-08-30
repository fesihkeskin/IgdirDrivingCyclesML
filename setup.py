from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .' # 

# Open the README.md file in read mode
# This is used to extract the long description for the package from the README file
with open("README.md", "r") as mdfile:
    long_description = mdfile.read()

# Open the requirements.txt file in read mode
# This file contains a list of all dependencies needed for the package
# Read the file and split the lines to create a list of requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
        
# Setup function to specify package details
setup(
    name="IgdirDrivingCyclesML",  # The name of the package
    version="0.0.1",  # The initial release version
    author="author name",  # The author's name
    author_email="author@gmail.com",  # The author's email
    description="IgdirDrivingCyclesML",  # A short description of the package
    long_description=long_description,  # A long description read from the README file
    long_description_content_type="text/markdown",  # The format of the long description
    url="https://github.com/author",  # The URL of the project's homepage
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=requirements,  # List of dependencies from requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3",  # The package is written in Python 3
        "License :: OSI Approved :: MIT License",  # The license type
        "Operating System :: OS Independent",  # The package is OS independent
    ],
    python_requires='>=3.8',  # Minimum version of Python required
)