#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def callback(data):
    radius = data.data
    squared_radius = radius*radius
    #otras formas de hacer log https://wiki.ros.org/rospy_tutorials/Tutorials/Logging
    #rospy.loginfo("radius: %f,squared_radius: %f", radius, squared_radius)
    pub.publish(squared_radius)

rospy.init_node("radius_squarer")
pub = rospy.Publisher("/radius_squared", Float64, queue_size=10)

# rospy.Suscriber crea un subscritor al
# topic /radius y
# llama la funcion callback llamada callback, cualquier mensaje enviado por /radios será enviado a esta función
rospy.Subscriber("/radius", Float64, callback)

rospy.spin() # Mantiene al nodo funcionando(vivo), es un loop infinito
