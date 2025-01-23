from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = '-e .' # constant for if statment below
def get_requirements(file_path:str)->List[str]:
    '''
    This will return a list of requirements given the input file_path
    '''
    requirements = [] # empty list
    with open(file_path) as file_obj: # open the file
        requirements = file_obj.readlines() # go through each str and put into a temp file object
        requirements = [req.replace("\n", " ") for req in requirements] # list comprehension, to replace \n bc of readline

        if hyphen_e_dot in requirements: # additional condition to remove '-e .' in requirements
            requirements.remove(hyphen_e_dot)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='JD',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)