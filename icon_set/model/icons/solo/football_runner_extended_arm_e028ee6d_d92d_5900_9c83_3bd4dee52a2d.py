"""A football runner extends the free arm while holding a ball at the right.

Kept the extended arm, held ball and split stride; omitted uniform and hand details.
Lucide person-standing informs the head and joined limbs; source fixes the distinct extended-arm pose.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e028ee6d-d92d-5900-9c83-3bd4dee52a2d'
SOURCE_PATH = 'pictographic-primitives/sports/american football run ball_e028ee6d-d92d-5900-9c83-3bd4dee52a2d.svg'
AUTHOR = 'gpt-6'

class FootballRunnerExtendedArm(Solo48):
    icon_id = 'football-runner-extended-arm'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('football', 'runner', 'extended', 'arm')

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
        # A football runner extends the free arm while holding a ball at the right.
        self.circle('head',22,9,3)
        self.oval('football',37,24,5,4)
        self.skeleton([
         ('torso',[(24,21),(22,30)]),
         ('extended-arm',[(24,21),(14,23),(6,18)]),
         ('carrying-arm',[(24,21),(32,24)]),
         ('back-leg',[(22,30),(14,34),(10,42)]),
         ('front-leg',[(22,30),(30,42),(42,38)])])
        self.relate('connect','carrying-arm-0','football-top')
        self.relate('connect','carrying-arm-0','football-bottom')
