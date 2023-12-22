#! /usr/bin/env python
import rospy
from sensor_msgs.msg  import Image
from cv_bridge import CvBridge
import cv2

def fsm_node(image_msg):
    bridge=CvBridge()
    cv_image=bridge.imgmsg_to_cv2(image_msg,desired_encoding="bgr8")
    gray_image=cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(gray_image,50,200)
    cv2.imshow('edge detection',edges)
    cv2.waitKey(1)

def main():
    rospy.init_node("fsm_node",anonymous=True)
    rospy.Subscriber("camera_image",Image,fsm_node)
    rospy.spin()

if __name__=="__main__":
    main()