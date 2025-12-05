from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# When you're done, close the simulator
state = "waiting"
on = True

def sim_ready() :
    action = input("Would you like to check the sonar (...), move (m), or quit (q)?")
    if action == "..." :
        print("Left: ", robot.left_sonar())
        print("Right: ", robot.right_sonar())
    elif action == "m" :
        movement_pattern = input("Would you like to control the robot (c), or send it on a predetermined path (p)?")
    elif action == "q" :
        on == False
    



while on == True:
    where = input("Would you like to run the robot in the simulator (s) or in real life (r)?")
    if where == "r" :
        state = "robot_ready"
        robot_ready()
    elif where == "s" :
        state = "sim_ready"
        sim_ready()
    else:
        #TODO



robot.exit()