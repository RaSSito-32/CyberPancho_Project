import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rassito/Documents/ros_projects/CyberPancho_Project/CyberPancho_Laberinth/src/my_package/install/my_package'
