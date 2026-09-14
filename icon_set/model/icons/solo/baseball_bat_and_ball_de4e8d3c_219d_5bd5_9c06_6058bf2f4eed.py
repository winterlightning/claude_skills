"""A diagonal baseball bat stands beside a round baseball.

Kept the rounded barrel, slim handle, end knob and ball; omitted seam detail. The diagonal pose preserves the source.
Source construction; circular ball and a rounded bat end with a connected handle; no useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de4e8d3c-219d-5bd5-9c06-6058bf2f4eed'
SOURCE_PATH = 'pictographic-primitives/sports/baseball bat ball_de4e8d3c-219d-5bd5-9c06-6058bf2f4eed.svg'
AUTHOR = 'gpt-6'

class BaseballBatAndBall(Solo48):
    icon_id = 'baseball-bat-and-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('baseball', 'bat', 'and', 'ball')

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
        # A diagonal baseball bat stands beside a round baseball.
        self.circle('ball',11,11,5)
        self.add_arc('bat-tip',(33,8),(41,14),radius_x=5)
        self.add_line('bat-lower',(41,14),(29,30))
        self.add_line('bat-base-right',(29,30),(25,27))
        self.add_line('bat-base-left',(25,27),(21,24))
        self.add_line('bat-upper',(21,24),(33,8))
        self.add_contour('barrel','bat-tip','bat-lower','bat-base-right','bat-base-left','bat-upper',closed=True)
        self.skeleton([('handle',[(25,27),(16,39)]),('knob',[(12,36),(16,39),(20,42)])])
        for part in ['bat-base-right','bat-base-left']:self.relate('connect','handle-0',part)
