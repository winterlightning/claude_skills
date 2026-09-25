"""Two long padded handles angle downward and outward from a circular spring at the top. Narrow connecting arms join the handles to the round coil, leaving an open triangular gap.

Circular spring, thin connecting arms and two outward-slanting padded handles retained. Both handles share mirrored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '540c2a81-a817-4e41-aee4-41f47c32e727'
SOURCE_PATH = 'pictographic-primitives/sports/hand grip_540c2a81-a817-4e41-aee4-41f47c32e727.svg'
AUTHOR = 'gpt-6'

class HandGripExerciser(Solo48):
    icon_id = 'hand-grip-exerciser'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('grip', 'hand', 'exerciser', 'strength', 'spring', 'fitness')

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
        self.circle('spring',24,12,6)
        self.add_polyline('left-handle',(12,22),(17,23),(22,24),(16,42),(6,40),closed=True)
        self.add_polyline('right-handle',(26,24),(31,23),(36,22),(42,40),(32,42),closed=True)
        self.add_line('left-stem',(18,12),(17,23));self.add_line('right-stem',(30,12),(31,23))
        for stem in ['left-stem','right-stem']:
         for a in ['spring-top','spring-bottom']:self.relate('connect',stem,a)
        for side in ['left','right']:
         for i in [1,2]:self.relate('connect',side+'-stem',side+'-handle-'+str(i))
