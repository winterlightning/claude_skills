"""A long hairbrush angles upward-right, widening from a narrow rounded handle into a rounded brush head. A row of straight bristles projects from one side of the head.
Symbol plan: Diagonal brush capsule with radius-5 semicircular ends and exact 3:4 tangents. Three bristles share normal (-3,-4) and pitch (8,-6); the radial envelope preserves a long rounded handle.
Keyshape: CIRCLE, centerline extremes radius 20 about (24,24).
Construction reference: brush; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd18a7082-46f1-4dc6-b671-553cb1e5fe2c'
SOURCE_PATH = 'pictographic-primitives/beauty/hair dress brush_d18a7082-46f1-4dc6-b671-553cb1e5fe2c.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'hairbrush-with-long-handle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('hairbrush', 'with', 'long', 'handle')

    def build(self):

        def segments(name, *points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name, cx, cy, r):
            self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        def rect(name, l,t,r,b, radius=0):
            if not radius:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            q=radius
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z: continue
                part=f'{name}-{j}'
                if j%2: self.add_arc(part,a,z,radius_x=q)
                else: self.add_line(part,a,z)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)

        def axes():
            self.add_line('axis-y',(6,6),(6,38))
            self.add_arc('axis-corner',(6,38),(10,42),radius_x=4,sweep=False)
            self.add_line('axis-x',(10,42),(42,42))
            self.add_contour('axes','axis-y','axis-corner','axis-x')

        segments('inner',(9,29),(17,23),(25,17),(33,11))
        self.add_arc('brush-tip',(33,11),(39,19),radius_x=5)
        self.add_line('outer',(39,19),(15,37))
        self.add_arc('grip-end',(15,37),(9,29),radius_x=5)
        self.add_contour('brush','inner-1','inner-2','inner-3','brush-tip','outer','grip-end',closed=True)
        for j in range(3):
         x,y=17+8*j,23-6*j
         self.add_line(f'bristle-{j}',(x,y),(x-3,y-4))
         self.relate('connect',f'bristle-{j}','brush')
