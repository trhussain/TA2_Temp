from Tello import Tello
from TelloCommand import TelloCommand
from TelloState import TelloState
from TelloCam import TelloCam

def testCallback(state):
    print("callback called: ")
    print(f"{state}\n")
    return None

    
drone = Tello(debug=True, has_video=False, state_callback=testCallback)

drone.connect()
drone.takeoff()

drone.cw(90)
drone.cw(90)
drone.cw(90)
drone.cw(90)

drone.land()
drone.disconnect()