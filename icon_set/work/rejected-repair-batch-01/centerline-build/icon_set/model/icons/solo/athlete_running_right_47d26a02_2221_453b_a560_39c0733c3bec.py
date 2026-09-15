"""A runner leans forward with bent arms and an extended rear leg.

Reduced doubled limb outlines to a jointed silhouette. The rightward running direction is deliberate.
Lucide person-standing: circular head, spare limbs and shared joints.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47d26a02-2221-453b-a560-39c0733c3bec'
SOURCE_PATH = 'pictographic-primitives/sports/athletics running 1_47d26a02-2221-453b-a560-39c0733c3bec.svg'
AUTHOR = 'gpt-6'

class AthleteRunningRight(Solo48):
    icon_id = 'athlete-running-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('athlete', 'running', 'right')

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
        # A runner leans forward with bent arms and an extended rear leg.
        self.circle('head',29,9,3)
        self.skeleton([
         ('torso',[(23,21),(18,29)]),
         ('back-arm',[(23,21),(13,20),(7,26)]),
         ('front-arm',[(23,21),(34,27),(42,19)]),
         ('back-leg',[(18,29),(12,38),(6,38)]),
         ('front-leg',[(18,29),(30,34),(26,42)])])
