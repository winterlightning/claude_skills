"""A football runner cradles a ball on the left while driving forward.

Kept the cradled oval ball and bent running legs; omitted internal hand and uniform outlines.
Lucide person-standing informs the head and joined limbs; source fixes the carrying pose.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c02a4b99-c4e8-5846-965a-355dd5ba36d9'
SOURCE_PATH = 'pictographic-primitives/sports/american football run ball_c02a4b99-c4e8-5846-965a-355dd5ba36d9.svg'
AUTHOR = 'gpt-6'

class FootballRunnerCradlingBall(Solo48):
    icon_id = 'football-runner-cradling-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('football', 'runner', 'cradling', 'ball')

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
        # A football runner cradles a ball on the left while driving forward.
        self.circle('head',28,9,3)
        self.oval('football',11,24,5,4)
        self.skeleton([
         ('torso',[(24,21),(28,30)]),
         ('carrying-arm',[(24,21),(16,24)]),
         ('free-arm',[(24,21),(35,19),(40,26)]),
         ('front-leg',[(28,30),(38,34),(42,34)]),
         ('back-leg',[(28,30),(22,38),(22,42)])])
        self.relate('connect','carrying-arm-0','football-top')
        self.relate('connect','carrying-arm-0','football-bottom')
