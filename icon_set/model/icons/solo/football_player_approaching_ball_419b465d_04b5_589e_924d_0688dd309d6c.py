"""A running player moves toward a round ball at the lower right. One leg bends backward, the other drops forward, and both arms curve outward to balance the stride.

Forward approach, trailing bent leg and lower-right ball retained; limbs reduced to joined strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '419b465d-04b5-589e-924d-0688dd309d6c'
SOURCE_PATH = 'pictographic-primitives/sports/player ball_419b465d-04b5-589e-924d-0688dd309d6c.svg'
AUTHOR = 'gpt-6'

class FootballPlayerApproachingBall(Solo48):
    icon_id = 'football-player-approaching-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('football', 'soccer', 'player', 'ball', 'running', 'sport')

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def skeleton(self,branches):
        parts=[]
        for name,points in branches:
            members=[]
            for index,(a,b) in enumerate(zip(points,points[1:])):
                key=f'{name}-{index}';members.append(key)
                self.add_line(key,a,b);parts.append((key,a,b))
            if len(members)>1:self.add_contour(name,*members)
        for index,(a,p,q) in enumerate(parts):
            for b,r,s in parts[index+1:]:
                if p in (r,s) or q in (r,s):self.relate('connect',a,b)

    def rounded(self,name,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for index,a in enumerate(pts):
            b=pts[(index+1)%8];key=f'{name}-{index}';members.append(key)
            if index%2:self.add_arc(key,a,b,radius_x=r)
            else:self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def weight(self,name,x,y,w,h,r):
        # Expose bar attachment nodes at the midpoint of each vertical wall.
        middle=y+h//2
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,middle),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,middle),(x,y+r)]
        members=[]
        for index,a in enumerate(pts):
            b=pts[(index+1)%len(pts)];key=f'{name}-{index}';members.append(key)
            if index in [1,4,6,9]:self.add_arc(key,a,b,radius_x=r)
            else:self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        self.circle('head',26,9,3);self.circle('ball',38,40,2)
        self.skeleton([('body',[(24,22),(20,30)]),('left-arm',[(24,22),(14,22),(10,28)]),('right-arm',[(24,22),(34,28),(42,28)]),('back-leg',[(20,30),(12,36),(6,36)]),('front-leg',[(20,30),(28,36),(26,42)])])
