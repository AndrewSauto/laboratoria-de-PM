#!/usr/bin/env python

import rospy
import time
import sys
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def poseCallback(pose_message):

    global theta
    theta = pose_message.theta

def circle(radius):
    global theta

    rospy.init_node('move_circle', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
    if (radius > 0):
	zeta = 1.0
	cond1 = True
	cond2 = False 
    else :
	zeta = -1.0
	cond1 = False
	cond2 = True
    move_cmd = Twist()
    move_cmd.linear.x = radius
    move_cmd.angular.z = zeta
    cond = True
    now = rospy.Time.now()
    rate = rospy.Rate(60)

    while (cond1):
	print ('angulo =', theta)
	if (theta <  1.0 and theta > 0.565 and rospy.Time.now() > now + rospy.Duration.from_sec(2)):
		break
	pub.publish(move_cmd)
	rate.sleep()

    while (cond2):
        print ('angulo =', theta)
	if(theta <  2.575 and theta > 2.0 and rospy.Time.now() > now + rospy.Duration.from_sec(2)):
		break

        pub.publish(move_cmd)
        rate.sleep()


if __name__ == '__main__':
    try:
	
        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
	
	circle(4.5)
	time.sleep(1)
	circle(-4.5)
	
    except rospy.ROSInterruptException:
        pass
