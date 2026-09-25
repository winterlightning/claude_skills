"""A flexed arm curls upward into a fist above a rounded biceps.

Kept one coherent arm outline; removed finger and internal muscle creases. The flexed profile is deliberately asymmetric.
Lucide biceps-flexed informed the rounded fist, concave elbow and dominant biceps lobe.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16db6751-7b03-56d8-bdde-9fcaff03d631'
SOURCE_PATH = 'pictographic-primitives/sports/biceps_16db6751-7b03-56d8-bdde-9fcaff03d631.svg'
AUTHOR = 'gpt-6'

class FlexedBiceps(Solo48):
    icon_id = 'flexed-biceps'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('flexed', 'biceps')

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
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        # A flexed arm curls upward into a fist above a rounded biceps.
        self.add_arc('outer-forearm',(4, 32),(14,8),radius_x=10,radius_y=24)
        self.add_line('fist-top',(14,8),(18,8))
        self.add_arc('fist',(18,8),(18,16),radius_x=4)
        self.add_line('inner-forearm',(18,16),(16,26))
        self.add_arc('inner-elbow',(16,26),(24,26),radius_x=6)
        self.add_arc('biceps',(24,26),(44, 26),radius_x=10)
        self.add_arc('lower-arm-right',(44, 26),(24,40),radius_x=20,radius_y=14)
        self.add_arc('lower-arm-left',(24,40),(4, 32),radius_x=20,radius_y=8)
        self.add_contour('arm','outer-forearm','fist-top','fist','inner-forearm','inner-elbow','biceps','lower-arm-right','lower-arm-left',closed=True)
