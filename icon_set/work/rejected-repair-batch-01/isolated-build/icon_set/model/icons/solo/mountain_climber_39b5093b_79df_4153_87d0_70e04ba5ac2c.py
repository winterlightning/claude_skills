"""A backpacked figure raises one knee beside a jagged rock face on the right. One arm reaches toward the cliff while the other bends near the shoulder above the extended supporting leg.

Kept the jagged cliff, hand contact and climbing stance; the backpack is reduced to an angular strap. The right-facing ascent remains asymmetric.
Source cliff and backpacked figure; Lucide person-standing, inspected in batch 01, informs the circular head and joined limbs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39b5093b-79df-4153-87d0-70e04ba5ac2c'
SOURCE_PATH = 'pictographic-primitives/sports/climbing mountain_39b5093b-79df-4153-87d0-70e04ba5ac2c.svg'
AUTHOR = 'gpt-6'

class MountainClimber(Solo48):
    icon_id = 'mountain-climber'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('climbing', 'mountain', 'climber', 'rock', 'athlete', 'ascent')

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
        self.circle('head',14,12,3)
        self.skeleton([
         ('cliff',[(42,6),(36,14),(36,20),(32,24),(36,32),(36,42),(42,42)]),
         ('torso',[(16,24),(12,36)]),
         ('reaching-arm',[(16,24),(24,24),(32,24)]),
         ('pack-strap',[(16,24),(6,22),(6,25)]),
         ('supporting-leg',[(12,36),(6,42)]),
         ('raised-leg',[(12,36),(24,32),(26,40)])])
