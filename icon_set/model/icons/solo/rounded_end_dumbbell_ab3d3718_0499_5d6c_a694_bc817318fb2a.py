"""A horizontal dumbbell consists of two narrow rounded end weights linked by a straight bar. Small bar tips project past the weights on both sides of the balanced silhouette.

Shared capsule end weights, centered bar and projecting tips; fully rounded ends distinguish this source.
Inspected source rendering; Lucide bike, sword, dumbbell and person-standing informed sparse equipment and figure construction where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ab3d3718-0499-5d6c-a694-bc817318fb2a'
SOURCE_PATH = 'pictographic-primitives/sports/fitness weights_ab3d3718-0499-5d6c-a694-bc817318fb2a.svg'
AUTHOR = "gpt-6"

class RoundedEndDumbbell(Solo48):
    icon_id = 'rounded-end-dumbbell'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
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
        self.weight('left',8,8,10,32,5)
        self.weight('right',30,8,10,32,5)
        self.add_line('bar',(18,24),(30,24))
        self.add_line('left-tip',(4,24),(8,24))
        self.add_line('right-tip',(40,24),(44,24))
        for p in ['left-2','left-3','right-7','right-8']:self.relate('connect','bar',p)
        for p in ['left-7','left-8']:self.relate('connect','left-tip',p)
        for p in ['right-2','right-3']:self.relate('connect','right-tip',p)
