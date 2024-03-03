#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

rospy.init_node("dylinder_input") # nombre de nodo
#/radius es el nombre del topic
# esto se asigna a la variable radios_pub
# Float64 es el tipo de dato d ela libreria std_msgs.msg
radius_pub = rospy.Publisher("/radius", Float64, queue_size=10)
height_pub = rospy.Publisher("/height", Float64, queue_size=10)
density_pub = rospy.Publisher("/density", Float64, queue_size=10)

# pedir los datos al usuario
radius = float(input("Ingrese el Radio: "))
height = float(input("Ingrese la altura: "))
density = float(input("Ingrese la densidad: "))

# cuando roscore esté corriendo (True parece no ser buena opción)
while not rospy.is_shutdown():
    radius_pub.publish(radius)    #Publicar radius
    height_pub.publish(height)    #Publicar height
    density_pub.publish(density)    #Publicar height
    rospy.sleep(0.1)
    
