"""A figure lunges with the front knee bent at a right angle and the rear leg extended diagonally backward. One arm rises overhead while the other follows the side of the upright torso.

Kept the upright torso, overhead arm, right-angle front knee and extended rear leg. Omitted the secondary arm alongside the torso.
Source lunge posture; Lucide person-standing supplies the circular head and spare jointed limbs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a860d136-343f-4827-85ad-e36b66cfa52a'
SOURCE_PATH = 'pictographic-primitives/sports/crescent lunge pose_a860d136-343f-4827-85ad-e36b66cfa52a.svg'
AUTHOR = 'gpt-6'

class CrescentLungePose(Solo48):
    icon_id = 'crescent-lunge-pose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('yoga', 'lunge', 'crescent', 'stretch', 'exercise', 'pose')

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
        self.circle('head',20,14,3)
        self.skeleton([
         ('raised-arm',[(24,26),(32,18),(32,6)]),
         ('torso',[(24,26),(24,32)]),
         ('rear-leg',[(24,32),(6,42)]),
         ('front-leg',[(24,32),(42,32),(42,42)])])
