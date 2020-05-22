#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x = 0
y = 0
theta = 0

x1 = 0
y1 = 0
theta1 = 0

x2 = 0
y2 = 0
theta2 = 0

x3 = 0
y3 = 0
theta3 = 0

x4 = 0
y4 = 0
theta4 = 0

x6 = 0
y6 = 0
theta6 = 0

def poseCallback(pose_message):
    global x
    global y
    global theta
    
    x = pose_message.x
    y = pose_message.y
    theta = pose_message.theta

def poseCallback1(pose_message):
    global x1
    global y1
    global theta1
    
    x1 = pose_message.x
    y1 = pose_message.y
    theta1 = pose_message.theta

def poseCallback2(pose_message):
    global x2
    global y2
    global theta2
    
    x2 = pose_message.x
    y2 = pose_message.y
    theta2 = pose_message.theta

def poseCallback3(pose_message):
    global x3
    global y3
    global theta3
    
    x3 = pose_message.x
    y3 = pose_message.y
    theta3 = pose_message.theta

def poseCallback4(pose_message):
    global x4
    global y4
    global theta4
    
    x4 = pose_message.x
    y4 = pose_message.y
    theta4 = pose_message.theta

def poseCallback6(pose_message):
    global x6
    global y6
    global theta6
    
    x6 = pose_message.x
    y6 = pose_message.y
    theta6 = pose_message.theta

def orientate (xgoal, ygoal):
    
	global x
	global y
	global theta

	velocity_message = Twist()
	cmd_vel_topic = '/turtle5/cmd_vel'
	dtheta = 1.0

	while(abs(dtheta) > 0.005):
		ka = 1.0
		desired_angle_goal = math.atan2(ygoal-y, xgoal-x)
		
		if desired_angle_goal < 0:
			desired_angle_goal = desired_angle_goal + 2*math.pi
			dtheta = desired_angle_goal - theta
			#print ('theta=', theta)			
			#print ('new_angle=', desired_angle_goal)
		else:
			desired_angle_goal = desired_angle_goal
			dtheta = desired_angle_goal - theta	
			#print ('new_angle=', desired_angle_goal)

		if abs(desired_angle_goal - theta) < abs((desired_angle_goal + 2*math.pi) - theta):	
			dtheta = desired_angle_goal - theta
			#print ('dtheta=', dtheta)
		else:
			dtheta = desired_angle_goal + 2*math.pi - theta
			#print ('dtheta=', dtheta)        

		angular_speed = ka * dtheta

		velocity_message.linear.x = 0.0
		velocity_message.angular.z = angular_speed
		velocity_publisher.publish(velocity_message)
		#print ('x=', x, 'y=', y)
       
if __name__ == '__main__':
	try:

		rospy.init_node('turtlesim_motion_pose', anonymous = True)

		cmd_vel_topic = '/turtle5/cmd_vel'
		velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

		position_topic = "/turtle5/pose"
		pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)

		position_topic1 = "/turtle1/pose"
        	pose_subscriber1 = rospy.Subscriber(position_topic1, Pose, poseCallback1)

        	position_topic2 = "/turtle2/pose"
        	pose_subscriber2 = rospy.Subscriber(position_topic2, Pose, poseCallback2)

        	position_topic3 = "/turtle3/pose"
        	pose_subscriber3 = rospy.Subscriber(position_topic3, Pose, poseCallback3)

		position_topic4 = "/turtle4/pose"
        	pose_subscriber4 = rospy.Subscriber(position_topic4, Pose, poseCallback4)

        	position_topic6 = "/turtle6/pose"
        	pose_subscriber6 = rospy.Subscriber(position_topic6, Pose, poseCallback3)
		
		xgoal = 2.5
		ygoal = 10		

		time.sleep(1.0)		
		orientate(xgoal,ygoal)
		time.sleep(0.5)
		
		velocity_message = Twist()
		cmd_vel_topic = '/turtle5/cmd_vel'
		d = 1.0

		while(True):

			d = math.sqrt(((xgoal-x)**2)+((ygoal-y)**2))
			d1 = math.sqrt(((x-x1)**2)+((y-y1)**2))
			d2 = math.sqrt(((x-x2)**2)+((y-y2)**2))
			d3 = math.sqrt(((x-x3)**2)+((y-y3)**2))
			d4 = math.sqrt(((x-x4)**2)+((y-y4)**2))
			d6 = math.sqrt(((x-x6)**2)+((y-y6)**2))
			flag = 0.0
			time.sleep(1.0)
			
			if d1 < 1.0 or  d2 < 1.0 or d3 < 1.0 or d4 < 1.0 or d6 < 1.0:
				flag = 1.0

			if flag == 1:
				if d1 < 1.0:
					if y < y1 and x > x1:
						linear_speed = math.sqrt(((xgoal-x)**2)+((ygoal-y)**2))/1.5
						angular_speed = 4 * (math.atan2(ygoal-y, xgoal-x) - (1/math.sqrt(((x1-x)**2)+((y1-y)**2))))
					else:
						linear_speed = math.sqrt(((xgoal-x)**2)+((ygoal-y)**2))/3
						angular_speed = 4 * (math.atan2(ygoal-y, xgoal-x) + (1/math.sqrt(((x1-x)**2)+((y1-y)**2))))
				if d2 < 1.0:
					if y < y2 and x > x2:
						linear_speed = math.sqrt(((xgoal-x)**2)+((ygoal-y)**2))/1.5
						angular_speed = 4 * (math.atan2(ygoal-y, xgoal-x) - (1/math.sqrt(((x2-x)**2)+((y2-y)**2))))
					else:
						linear_speed = math.sqrt(((xgoal-x)**2)+((ygoal-y)**2))/3
						angular_speed = 4 * (math.atan2(ygoal-y, xgoal-x) + (1/math.sqrt(((x2-x)**2)+((y2-y)**2))))
				if d3 < 1.0:
					if y < y3 and x > x3:
						linear_speed = math.sqrt(((xgoal-x)**2)+((ygoal-y)**2))/1.5
						angular_speed = 4 * (math.atan2(ygoal-y, xgoal-x) - (1/math.sqrt(((x3-x)**2)+((y3-y)**2))))
					else:
						linear_speed = math.sqrt(((xgoal-x)**2)+((ygoal-y)**2))/3
						angular_speed = 4 * (math.atan2(ygoal-y, xgoal-x) + (1/math.sqrt(((x3-x)**2)+((y3-y)**2))))
				if d4 < 1.0:
					if y < y4 and x > x4:
						linear_speed = math.sqrt(((xgoal-x)**2)+((ygoal-y)**2))/1.5
						angular_speed = 4 * (math.atan2(ygoal-y, xgoal-x) - (1/math.sqrt(((x4-x)**2)+((y4-y)**2))))
					else:
						linear_speed = math.sqrt(((xgoal-x)**2)+((ygoal-y)**2))/3
						angular_speed = 4 * (math.atan2(ygoal-y, xgoal-x) + (1/math.sqrt(((x4-x)**2)+((y4-y)**2))))
				if d6 < 1.0:
					if y < y6 and x > x6:
						linear_speed = math.sqrt(((xgoal-x)**2)+((ygoal-y)**2))/1.5
						angular_speed = 4 * (math.atan2(ygoal-y, xgoal-x) - (1/math.sqrt(((x6-x)**2)+((y6-y)**2))))
					else:
						linear_speed = math.sqrt(((xgoal-x)**2)+((ygoal-y)**2))/3
						angular_speed = 4 * (math.atan2(ygoal-y, xgoal-x) + (1/math.sqrt(((x6-x)**2)+((y6-y)**2))))
			else :
				time.sleep(0.5)		
				orientate(xgoal,ygoal)
				time.sleep(0.5)
				linear_speed = math.sqrt((xgoal-x) ** 2 + (ygoal-y) ** 2)/3
           			desired_angle_goal = math.atan2(ygoal+0.01-y, xgoal+0.01-x)
				if (desired_angle_goal < 0.0):	
					desired_angle_goal = desired_angle_goal + 6.2831
				angular_speed = 4*(desired_angle_goal-theta)
				if (abs(angular_speed) < 0.5):	
					angular_speed = angular_speed
				else:
					angular_speed = 0.0
				

			#Manda los datos para el movimiento de la pieza
			
			velocity_message.linear.x = linear_speed
			velocity_message.angular.z = angular_speed
			velocity_publisher.publish(velocity_message)
			time.sleep(1.0)
			
			if d < 0.1:
				break

	except rospy.ROSInterruptException:        
		pass
