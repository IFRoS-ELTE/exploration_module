#!/usr/bin/env python
import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
from tf2_msgs.msg import TFMessage

def transform_callback(transform_msg):
    for transform in transform_msg.transforms:
        if transform.child_frame_id == "robot/base_link":
            # Create a new TransformStamped message for the new frame
            new_transform = TransformStamped()
            new_transform.header = transform.header
            new_transform.child_frame_id = "robot/base_link_fixed"
            new_transform.transform = transform.transform  # Copy the same transformation

            # Set the z-coordinate to 0.2 for the new frame
            new_transform.transform.translation.z = 0.30

            # Publish the modified transformation
            tf_broadcaster.sendTransform(new_transform)

if __name__ == '__main__':
    rospy.init_node('transform_normalizer')

    # Initialize the transform broadcaster
    tf_broadcaster = tf2_ros.TransformBroadcaster()

    # Subscribe to the transformation topic
    rospy.Subscriber("/tf", TFMessage, transform_callback)

    # Spin the node
    rospy.spin()
