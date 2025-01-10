import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/eugenio/GitHub/cyberPancho_lidar/install/cyberPancho_sim'
