"""A front-facing athlete lifts both arms in celebration while crossing a broad horizontal finish ribbon. The ribbon passes across the waist, with two straight legs continuing below.

Raised arms, broad outlined finish ribbon and two legs retained. The head is reduced to a small complete circular mark to clear the arms.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '16b9f2ab-9387-51cc-9d12-6908f0e5c10e'
SOURCE_PATH = 'pictographic-primitives/sports/marathon running finished goal_16b9f2ab-9387-51cc-9d12-6908f0e5c10e.svg'
AUTHOR = 'gpt-6'

class RunnerFinishRibbon(Solo48):
    icon_id = 'runner-finish-ribbon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('runner', 'finish', 'race', 'marathon', 'ribbon', 'victory')

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
        self.circle('head',24,8,2)
        self.skeleton([('arms',[(6,6),(10,16),(18,20),(24,20),(30,20),(38,16),(42,6)]),('torso',[(24,20),(24,28)]),('left-leg',[(18,36),(18,42)]),('right-leg',[(30,36),(30,42)])])
        self.add_polyline('ribbon',(6,28),(24,28),(42,28),(42,36),(30,36),(18,36),(6,36),closed=True)
        for p in ['ribbon-1','ribbon-2']:self.relate('connect','torso-0',p)
        for p in ['ribbon-5','ribbon-6']:self.relate('connect','left-leg-0',p)
        for p in ['ribbon-4','ribbon-5']:self.relate('connect','right-leg-0',p)
