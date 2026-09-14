"""Two running figures move side by side, with one slightly behind and to the left. Both have circular heads, bent swinging arms, and legs separated into active strides.

Two distinct heads and active strides retained. The figures use joined strokes with staggered arms and legs, preserving a pair rather than merging bodies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4d3f2c4a-8660-5fc7-a78c-9ed22cef045e'
SOURCE_PATH = 'pictographic-primitives/sports/group running_4d3f2c4a-8660-5fc7-a78c-9ed22cef045e.svg'
AUTHOR = 'gpt-6'

class PairOfRunners(Solo48):
    icon_id = 'pair-of-runners'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('running', 'runner', 'pair', 'group', 'athlete', 'fitness')

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
        self.circle('left-head',14,9,3);self.circle('right-head',34,9,3)
        self.skeleton([('left-body',[(14,22),(14,30)]),('left-back-arm',[(14,22),(6,22),(6,28)]),('left-front-arm',[(14,22),(20,26)]),('left-back-leg',[(14,30),(6,40)]),('left-front-leg',[(14,30),(18,36),(16,42)]),('right-body',[(34,22),(32,30)]),('right-front-arm',[(34,22),(42,18)]),('right-back-arm',[(34,22),(28,24),(28,27)]),('right-back-leg',[(32,30),(26,40)]),('right-front-leg',[(32,30),(40,36),(42,42)])])
