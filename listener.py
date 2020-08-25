#!/usr/bin/env python
PKG = 'numpy1'
import roslib; roslib.load_manifest(PKG)

import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import Int16,String

def callback(data):
    print (str(data.data))

def listener():
    rospy.init_node('Dany')
    rospy.Subscriber("targaryens", numpy_msg(Floats), callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
