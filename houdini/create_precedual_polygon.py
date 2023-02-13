from math import cos, sin, radians

node = hou.pwd()
geo = node.geometry()

def create_polygon(p, q, r):
    f = geo.createPolygon()
    f.addVertex(p)
    f.addVertex(q)
    f.addVertex(r)




# Add code to modify contents of geo.
# Use drop down menu to select examples.

num = node.parm('number').eval()

orgin_pnt = geo.createPoint()

points = []
for i in range(0, num):

    angle = radians(i*(360 / num))
    
    x = cos(angle)
    z = sin(angle)
    
    pos = (x, 0, z)
    
    pnt = geo.createPoint()
    pnt.setPosition(pos)
    
    points.append(pnt)

    
for i, pnt in enumerate(points):
    create_polygon(orgin_pnt, points[i], points[(i+1)%num])



