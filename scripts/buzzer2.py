#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16

def recv_buzzer(data):
    rospy.loginfo(type(data))
    rospy.loginfo(data.data)

if __name__ == '__main__':
    rospy.init_node('buzzer_node')
    rospy.Subscriber("buzzer_Subscriber", UInt16, recv_buzzer)
    rospy.spin()
