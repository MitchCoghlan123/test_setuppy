from setuptools import *


setup(
        name="Ivan-the-Robot",
        version="1.0.0",
        description="The base game of Ivan the Robot",
        author="Mitch Coghlan",
        python_requires=">=3.10.*",
        packages=find_packages(include=["files"]),
        entry_points={
                'console_scripts': ['launchGame=Ivan_the_Robot:main']
            }
    )
    
    
