import signal, sys
from time import sleep
from rplidar import RPLidar

LIDAR_PORT = '/dev/ttyUSB0'

while(True):
    print('starting...')
    sleep(2)
    try :
        lidar = RPLidar(LIDAR_PORT)

        for i, scan in enumerate(lidar.iter_scans()):
            for qual, angle, dist in scan:
                print(qual, angle, dist)
            break


        # for (i, val) in enumerate(lidar.iter_measurments()):
        #     _, qual, angle, dist = val
        #     print(qual, angle, dist)
        #     break
        break
    except KeyboardInterrupt:
        lidar.stop()
        lidar.stop_motor()
        lidar.disconnect()
        break
    except SystemExit:
        break
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        try:
            print(str(exc_type) + '\t' + str(exc_value))
        except KeyboardInterrupt:
            lidar = RPLidar(LIDAR_PORT)
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()
