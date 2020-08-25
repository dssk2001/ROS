#!/usr/bin/env python
PKG = 'numpy1'
import roslib; roslib.load_manifest(PKG)

import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
from std_msgs.msg import Int16,String
import numpy as np

def  ones_in_num(a):
  new = []
  for i in a: 
    count = 0
    while (i): 
      count += i & 1
      i >>= 1
    new.append(count)
  return new


def talker():
    pub = rospy.Publisher('targaryens', numpy_msg(Floats),queue_size=10)
    rospy.init_node('JonSnow', anonymous=False)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        a = np.random.randint(1,101,10)
        b = ones_in_num(a)
        print(a)
        #print(b)
        pub.publish(np.array(b,dtype=np.float32))
        r.sleep()

if __name__ == '__main__':
    talker()
