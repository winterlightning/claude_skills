"""An upright football player raises one arm and lowers the other beside the torso. One knee bends toward a ball at the lower left while the opposite leg remains extended.

Upright posture, raised arm, bent knee and lower-left ball retained. The ball remains separate from the controlling foot for clear spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48e5cfea-33eb-5928-8f29-422a48899ccf'
SOURCE_PATH = 'pictographic-primitives/sports/player_48e5cfea-33eb-5928-8f29-422a48899ccf.svg'
AUTHOR = 'gpt-6'

class FootballPlayerControllingBall(Solo48):
    icon_id = 'football-player-controlling-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('football', 'soccer', 'player', 'ball', 'control', 'sport')

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
        self.circle('head',24,9,3);self.circle('ball',9,39,3)
        self.skeleton([('body',[(24,22),(24,30)]),('raised-arm',[(24,22),(36,20),(42,12)]),('lowered-arm',[(24,22),(14,24),(10,28)]),('bent-leg',[(24,30),(20,32)]),('straight-leg',[(24,30),(28,42)])])
