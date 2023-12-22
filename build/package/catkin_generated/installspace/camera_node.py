#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def camera_node():
    rospy.init_node("camera_node", anonymous=True)
    rate = rospy.Rate(10) # 10Hz

    cap = cv2.VideoCapture(0)
    pub = rospy.Publisher("camera_image", Image, queue_size=10)
    bridge = CvBridge()

    while not rospy.is_shutdown():
        ret, frame = cap.read()

        if ret:
            cv2.imshow("Camera Image", frame)
            cv2.waitKey(1) 

            image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            pub.publish(image_msg)
        rate.sleep()

    cap.release()
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    try:
        camera_node()
    except rospy.ROSInterruptException:
        pass

