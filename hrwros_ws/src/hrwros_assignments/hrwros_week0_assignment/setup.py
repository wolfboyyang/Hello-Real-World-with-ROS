from setuptools import setup

package_name = 'hrwros_week0_assignment'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'week0_assignment = hrwros_week0_assignment.week0_assignment:main',
        ],
    },
)
