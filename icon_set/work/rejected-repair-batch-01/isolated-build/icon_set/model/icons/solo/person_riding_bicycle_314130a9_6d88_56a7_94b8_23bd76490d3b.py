"""A cyclist leans over two separated bicycle wheels.

Kept both wheels and the bent rider; omitted the bicycle frame, matching the source emphasis. Directional posture is intentional.
Lucide bike informed equal wheels, a small circular head and one bent rider contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '314130a9-6d88-56a7-94b8-23bd76490d3b'
SOURCE_PATH = 'pictographic-primitives/sports/biking person_314130a9-6d88-56a7-94b8-23bd76490d3b.svg'
AUTHOR = 'gpt-6'

class PersonRidingBicycle(Solo48):
    icon_id = 'person-riding-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('person', 'riding', 'bicycle')

    def circle(self, name, x, y, radius):
        self.add_arc(name+'-top',(x-radius,y),(x+radius,y),radius_x=radius)
        self.add_arc(name+'-bottom',(x+radius,y),(x-radius,y),radius_x=radius)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def skeleton(self, branches):
        # Declare only actual shared endpoints in the physical figure.
        segments=[]
        for name,points in branches:
            for index,(a,b) in enumerate(zip(points,points[1:])):
                key=f'{name}-{index}'
                self.add_line(key,a,b);segments.append((key,a,b))
            if len(points)>2:self.add_contour(name,*[f'{name}-{i}' for i in range(len(points)-1)])
        for index,(a,p,q) in enumerate(segments):
            for b,r,s in segments[index+1:]:
                if p in (r,s) or q in (r,s):self.relate('connect',a,b)

    def oval(self,name,x,y,rx,ry):
        self.add_arc(name+'-top',(x-rx,y),(x+rx,y),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(x+rx,y),(x-rx,y),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self):
        # A cyclist leans over two separated bicycle wheels.
        # Shared wheel radius and baseline; body rebalanced above the wheels.
        for name,x in [('rear',9),('front',39)]:self.circle(name+'-wheel',x,35,5)
        self.circle('head',28,11,3)
        self.skeleton([('rider',[(24,23),(18,25),(24,30),(24,36)]),('arms',[(24,23),(32,22),(39,21)])])
