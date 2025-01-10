from setuptools import find_packages, setup

package_name = 'cyberPancho_sim'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))

#carpeta launch
data_files.append(('share/' + package_name + '/launch', ['launch/robot_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/robot_rviz_launch.py']))

#carpeta world
data_files.append(('share/' + package_name + '/worlds', ['worlds/cyberPancho_World.wbt']))

#carpeta resource
data_files.append(('share/' + package_name + '/resource', ['resource/robot.urdf']))
data_files.append(('share/' + package_name + '/resource', ['resource/lidar.urdf']))
data_files.append(('share/' + package_name + '/resource', ['resource/urdf_view.rviz']))

data_files.append(('share/' + package_name, ['package.xml']))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user.name@mail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'webots_robot_driver = cyberPancho_sim.webots_robot_driver:main',
        ],
    },
)