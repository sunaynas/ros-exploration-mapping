import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


def callback(data):
    rospy.loginfo("Received an image!")
    try:
        # Convert ROS Image message to OpenCV format
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except Exception as e:
        rospy.logerr(e)
        return

    # Display the image
    cv2.imshow("Image window", cv_image)
    cv2.waitKey(1)  # Update window

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", Image, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()