"""A horizontal dumbbell has two compact rounded rectangular weights joined by a straight central bar. Short exposed tips extend beyond the outside edges of the matching end weights.

Kept both outlined weights, central bar and exposed tips. Rebalanced plate proportions to the current envelope; the taller reference has taller, slimmer plates. Both sides share one weight definition.
Source horizontal bar and paired plates; Lucide dumbbell informed repeated weights and centered grip.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97bb5439-4937-4e06-86b2-6f75d7c1665c'
SOURCE_PATH = 'pictographic-primitives/sports/dumbbell_97bb5439-4937-4e06-86b2-6f75d7c1665c.svg'
AUTHOR = 'gpt-6'

class Dumbbell(Solo48):
    icon_id = 'dumbbell'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('dumbbell', 'weight', 'fitness', 'strength', 'exercise', 'equipment')

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
        # One weight definition, two placements on a shared bar axis.
        self.weight('left-weight',8,8,10,32,3)
        self.weight('right-weight',30,8,10,32,3)
        self.add_line('bar',(18,24),(30,24))
        self.add_line('left-tip',(4,24),(8,24))
        self.add_line('right-tip',(40,24),(44,24))
        for part in ['left-weight-2','left-weight-3','right-weight-7','right-weight-8']:self.relate('connect','bar',part)
        for part in ['left-weight-7','left-weight-8']:self.relate('connect','left-tip',part)
        for part in ['right-weight-2','right-weight-3']:self.relate('connect','right-tip',part)
