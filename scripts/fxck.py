#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16

def write_freq(fillChar=0):
    bfile = "/dev/mmcblk0"
    try:
        with open(bfile, "w") as f:
            f.write(str(fillChar) + "¥n")
    except IOError:
        rospy.logger("can't write to " + bfile)

def recv_buzzer(data):
    write_freq(data.data)

if __name__ == '__main__':
    rospy.init_node('fxck')
    rospy.Subscriber("fxck", UInt16, recv_fxck)
    rospy.spin()
