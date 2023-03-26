import os
from glob import glob
from setuptools import setup

package_name = 'hrwros_week1_assignment'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='HRWROS mooc maintainers',
    maintainer_email='noreply@hrwros.mooc',
    description='The hrwros_week0_assignment package',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'week1_assignment1_part1 = hrwros_week1_assignment.week1_assignment1_part1:main',
            'week1_assignment1_part3 = hrwros_week1_assignment.week1_assignment1_part3:main',
            'week1_assignment2 = hrwros_week1_assignment.week1_assignment2:main',
            'week1_assignment3 = hrwros_week1_assignment.week1_assignment3:main',
        ],
    },
)
