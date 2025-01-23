from setuptools import find_packages, setup
from typing import List

# Define a string that will be removed from the requirements list if present
hyphen = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Return the list of requirements.

    This function reads the requirements from the given file path and returns them as a list.
    """
    requirements = []
    # Open the requirements file and read its contents
    with open(file_path) as file_obj:
        # Read each line in the file, remove newline characters, and add to the list
        requirements = [req.replace("\n", "") for req in file_obj.readlines()]

        # Remove the hyphen string if it is present in the list
        if hyphen in requirements:
            requirements.remove(hyphen)
    return requirements

# Define the setup configuration for the package
setup(
    name='mlproject',  # Name of the package
    version='0.0.1',  # Version of the package
    author="mawiya",  # Author of the package
    author_email='mawiyamanzar@gmail.com',  # Author's email
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=get_requirements('requirements.txt')  # List of dependencies
)