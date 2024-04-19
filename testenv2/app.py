from rktellolib import Tello

drone = Tello(debug=True, has_video=False)

drone.connect()
drone.takeoff()

drone.cw(90)
drone.cw(90)
drone.cw(90)
drone.cw(90)

drone.land()
drone.disconnect()