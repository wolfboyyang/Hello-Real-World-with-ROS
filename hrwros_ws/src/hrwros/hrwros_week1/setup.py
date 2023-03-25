import os
from glob import glob
from setuptools import setup

package_name = 'hrwros_week1'

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
    description='The hrwros_week1 package',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'counter_with_delay_ac = hrwros_week1.counter_with_delay_ac:main',
            'counter_with_delay_as = hrwros_week1.counter_with_delay_as:main',
            'metres_to_feet_client = hrwros_week1.metres_to_feet_client:main',
            'metres_to_feet_server = hrwros_week1.metres_to_feet_server:main',
            'sensor_info_publisher = hrwros_week1.sensor_info_publisher:main',
            'sensor_info_subscriber = hrwros_week1.sensor_info_subscriber:main',
            'template_publisher_script = hrwros_week1.template_publisher_script:main',
            'template_subscriber_script = hrwros_week1.template_subscriber_script:main',
        ],
    },
)
