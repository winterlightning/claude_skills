"""A figure with raised arms hangs beside a rope curving upward on the right. A horizontal harness crosses the waist, with one leg extended down-left and the other bent outward.

Kept the raised grip, rope curve and waist harness; simplified the limbs to coherent strokes.
Source rope-to-harness relationship; Lucide person-standing supplies the sparse figure construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c734cba9-11d1-47ef-9193-480b63d4bd96'
SOURCE_PATH = 'pictographic-primitives/sports/climbing sports_c734cba9-11d1-47ef-9193-480b63d4bd96.svg'
AUTHOR = 'gpt-6'

class RopeClimber(Solo48):
    icon_id = 'rope-climber'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('climbing', 'rope', 'harness', 'athlete', 'ascent', 'sport')

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
        self.circle('head',18,11,3)
        self.skeleton([
         ('rope-top',[(42,6),(42,18)]),
         ('torso',[(20,24),(20,32)]),
         ('left-arm',[(20,24),(10,24),(6,17)]),
         ('right-arm',[(20,24),(30,18),(42,18)]),
         ('harness',[(12,32),(20,32),(30,32)]),
         ('extended-leg',[(20,32),(10,42)]),
         ('bent-leg',[(20,32),(32,36),(32,42)])])
        self.add_arc('rope-curve',(42,18),(30,32),radius_x=12,radius_y=14)
        for part in ['rope-top-0','right-arm-1','harness-1']:self.relate('connect','rope-curve',part)
