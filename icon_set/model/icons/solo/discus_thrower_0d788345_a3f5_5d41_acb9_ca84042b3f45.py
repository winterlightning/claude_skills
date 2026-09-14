"""An athlete twists in a wide stepping stance with one arm extended diagonally to the right. The opposite arm bends back on the left, holding a small round discus beside the head.

Kept the smaller held discus distinct from the larger head, with a twisting stance and extended opposite arm.
Source throwing orientation; Lucide person-standing informed the head and jointed limbs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d788345-a3f5-5d41-acb9-ca84042b3f45'
SOURCE_PATH = 'pictographic-primitives/sports/discus throwing_0d788345-a3f5-5d41-acb9-ca84042b3f45.svg'
AUTHOR = 'gpt-6'

class DiscusThrower(Solo48):
    icon_id = 'discus-thrower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('discus', 'throw', 'athletics', 'athlete', 'field', 'sport')

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
        self.circle('head',24,10,4)
        self.add_arc('discus-right',(9,17),(9,23),radius_x=3)
        self.add_arc('discus-left',(9,23),(9,17),radius_x=3)
        self.add_contour('discus','discus-right','discus-left',closed=True)
        self.skeleton([
         ('torso',[(22,25),(22,32)]),
         ('holding-arm',[(22,25),(12,29),(9,23)]),
         ('extended-arm',[(22,25),(42,16)]),
         ('rear-leg',[(22,32),(14,38),(6,42)]),
         ('front-leg',[(22,32),(30,38),(28,42)])])
        for part in ['discus-right','discus-left']:self.relate('connect','holding-arm-1',part)
